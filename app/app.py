from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
import os 
import time

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "mysql-service")
DB_NAME = os.getenv("DB_NAME", "PetShop")
DB_USER = os.getenv("DB_USER", "USER")
DB_PASSWORD = os.getenv ("DB_PASSWORD", "senha123")

def conectar_bd():
    tentativas = 10
    while tentativas > 0:
        try:
            conexao = mysql.connector.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            return conexao
        except mysql.connector.Error:
            tentativas -= 1
            time.sleep(3)
    return None

@app.route("/cliente", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        email = request.form["email"]

        conexao = conectar_bd()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO contatos (nome, telefone, email)",
                (nome, telefone, email)
            )
        conexao.commit()
        conexao.close()
        conexao.close()

    contatos = []
    conexao = conectar_bd()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, telefone, email FROM contatos ORDER BY id")
        contatos = cursor.fetchall()
        cursor.close()
        conexao.close()
    return jsonify (contatos)

@app.route("/pets", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome_pet = request.form["nome_pet"]
        tipo = request.form["tipo"]
        raca = request.form["raca"]
        idade = request.form["idade"]
        id_cliente = request.form["id_cliente"]

        conexao = conectar_bd()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO pets (nome_pet, tipo, raca, idade, id_cliente)",
                (nome_pet, tipo, raca, idade, id_cliente)
            )
        conexao.commit()
        conexao.close()
        conexao.close()

    pets = []
    conexao = conectar_bd()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, telefone, email FROM contatos ORDER BY id")
        pets = cursor.fetchall()
        cursor.close()
        conexao.close()
    return jsonify (pets)
