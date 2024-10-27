from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Conectar ao banco de dados MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="compra_online"
    )

# Endpoint para criar um novo cliente
@app.route('/clientes', methods=['POST'])
def criar_cliente():
    dados = request.json
    nome = dados['nome']
    email = dados['email']
    telefone = dados['telefone']
    endereco = dados['endereco']
    
    conn = connect_db()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO Clientes (nome, email, telefone, endereco) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nome, email, telefone, endereco))
        conn.commit()
        return jsonify({"message": "Cliente criado com sucesso"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoint para adicionar um produto
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    dados = request.json
    nome_produto = dados['nome_produto']
    preco = dados['preco']
    estoque = dados['estoque']
    
    conn = connect_db()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO Produtos (nome_produto, preco, estoque) VALUES (%s, %s, %s)"
        cursor.execute(query, (nome_produto, preco, estoque))
        conn.commit()
        return jsonify({"message": "Produto adicionado com sucesso"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoint para registrar um pedido
@app.route('/pedidos', methods=['POST'])
def registrar_pedido():
    dados = request.json
    id_cliente = dados['id_cliente']
    id_produto = dados['id_produto']
    data_pedido = dados['data_pedido']
    quantidade = dados['quantidade']
    valor_total = dados['valor_total']
    
    conn = connect_db()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO Pedidos (id_cliente, id_produto, data_pedido, quantidade, valor_total) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (id_cliente, id_produto, data_pedido, quantidade, valor_total))
        conn.commit()
        return jsonify({"message": "Pedido registrado com sucesso"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
