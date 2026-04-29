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
        cursor.execute("SELECT id, nome_pet, tipo, raca, idade, id_cliente FROM pets ORDER BY id")
        pets = cursor.fetchall()
        cursor.close()
        conexao.close()
    return jsonify (pets)

@app.route("/servicos", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        id_pet = request.form["id_pet"]
        tipo = request.form["tipo"]
        data = request.form["data"]
        valor = request.form["valor"]

        conexao = conectar_bd()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO servicos (id_pet, tipo, data, valor)",
                (id_pet, tipo, data, valor)
            )
        conexao.commit()
        conexao.close()
        conexao.close()

    servicos = []
    conexao = conectar_bd()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, id_pet, tipo, data, valor FROM servicos ORDER BY id")
        servicos = cursor.fetchall()
        cursor.close()
        conexao.close()
    return jsonify (servicos)

@app.route("/produtos", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        preco = request.form["preco"]
        quantidade = request.form["quantidade"]

        conexao = conectar_bd()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO produtos (nome, descricao, preco, quantidade)",
                (nome, descricao, preco, quantidade)
            )
        conexao.commit()
        conexao.close()
        conexao.close()

    produtos = []
    conexao = conectar_bd()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, descricao, preco, quantidade FROM produtos ORDER BY id")
        produtos = cursor.fetchall()
        cursor.close()
        conexao.close()
    return jsonify (produtos)

@app.route("/fornecedores", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        email = request.form["email"]
        id_produto = request.form["id_produto"]

        conexao = conectar_bd()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO produtos (nome, descricao, preco, quantidade)",
                (nome, telefone, email, id_produto)
            )
        conexao.commit()
        conexao.close()
        conexao.close()

    fornecedores = []
    conexao = conectar_bd()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, telefone, email, id_produto FROM fornecedores ORDER BY id")
        fornecedores = cursor.fetchall()
        cursor.close()
        conexao.close()
    return jsonify (fornecedores)

@app.route("/vendas", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        id_cliente = request.form["id_cliente"]
        id_produto = request.form["id_produto"]
        data = request.form["data"]
        quantidade = request.form["quantidade"]
        valor = request.form["valor"]

        conexao = conectar_bd()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO vendas (id_cliente, id_produto, data, quantidade, valor)",
                (id_cliente, id_produto, data, valor, quantidade)
            )
        conexao.commit()
        conexao.close()
        conexao.close()

    vendas = []
    conexao = conectar_bd()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, id_cliente, id_produto, data, quantidade, valor FROM vendas ORDER BY id")
        vendas = cursor.fetchall()
        cursor.close()
        conexao.close()
    return jsonify (vendas)

