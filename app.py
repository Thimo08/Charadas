from flask import Flask, jsonify

app = Flask(__name__)

from flask import Flask, jsonify
import random

app = Flask(__name__)

charadas = [
    {"id": 1, "pergunta": "O que é, o que é? Anda com os pés na cabeça.", "resposta": "Piolho"},
    {"id": 2, "pergunta": "O que é, o que é? Quanto mais se perde, mais se tem.", "resposta": "Sono"},
    {"id": 3, "pergunta": "O que é, o que é? Sobe e desce, mas nunca se move.", "resposta": "Escada"},
    {"id": 4, "pergunta": "O que é, o que é? Tem boca, mas não fala, tem asas, mas não voa e tem rio, mas não água.", "resposta": "Mapa"},
    {"id": 5, "pergunta": "O que é, o que é? Quanto mais se tira, maior fica.", "resposta": "Buraco"},
    {"id": 6, "pergunta": "O que é, o que é? Tem coroa, mas não é rei, tem espinhos, mas não machuca.", "resposta": "Abacaxi"},
    {"id": 7, "pergunta": "O que é, o que é? Tem dentes, mas não morde.", "resposta": "Pente"},
    {"id": 8, "pergunta": "O que é, o que é? Corre a casa toda e depois se esconde em um canto.", "resposta": "Vassoura"},
    {"id": 9, "pergunta": "O que é, o que é? Voa sem ter asas e chora sem ter olhos.", "resposta": "Nuvem"},
    {"id": 10, "pergunta": "O que é, o que é? Fica cheio durante o dia e vazio durante a noite.", "resposta": "Sapato"},
    {"id": 11, "pergunta": "O que é, o que é? Tem pescoço, mas não tem cabeça, tem braços, mas não tem mãos.", "resposta": "Camisa"},
    {"id": 12, "pergunta": "O que é, o que é? Tem cabeça e tem dente, mas não é bicho nem é gente.", "resposta": "Alho"},
    {"id": 13, "pergunta": "O que é, o que é? Quanto mais quente está, mais fresco é.", "resposta": "Pão"},
    {"id": 14, "pergunta": "O que é, o que é? Tem rio, mas não tem água, tem floresta, mas não tem árvore, e tem cidade, mas não tem casa.", "resposta": "Mapa"},
    {"id": 15, "pergunta": "O que é, o que é? Uma casa com quatro cantos, e em cada canto um gato, cada gato vê três gatos, quantos gatos há na casa?", "resposta": "4 gatos"},
    {"id": 16, "pergunta": "O que é, o que é? Quanto mais se enxuga, mais molhado fica.", "resposta": "Toalha"},
    {"id": 17, "pergunta": "O que é, o que é? Tem muitas casas, mas não tem paredes, tem muitas ruas, mas não tem carros, e tem muitas árvores, mas não tem pássaros.", "resposta": "Colmeia"},
    {"id": 18, "pergunta": "O que é, o que é? Tem muitas agulhas, mas não sabe costurar.", "resposta": "Pinheiro"},
    {"id": 19, "pergunta": "O que é, o que é? Tem muitas bocas, mas não come, tem muitas camas, mas não dorme.", "resposta": "Fogão"},
    {"id": 20, "pergunta": "O que é, o que é? Tem muitas cores, mas não tem pincel, tem muitas formas, mas não tem tesoura.", "resposta": "Arco-íris"},
    {"id": 21, "pergunta": "O que é, o que é? Tem muitas janelas, mas não tem portas, tem muitas luzes, mas não tem interruptor.", "resposta": "Cidade"},
    {"id": 22, "pergunta": "O que é, o que é? Tem muitas folhas, mas não é árvore, tem muitas páginas, mas não é livro.", "resposta": "Caderno"},
    {"id": 23, "pergunta": "O que é, o que é? Tem muitas cordas, mas não amarra, tem muitas notas, mas não escreve.", "resposta": "Violino"},
    {"id": 24, "pergunta": "O que é, o que é? Tem muitas chaves, mas não abre portas, tem muitos espaços, mas não guarda nada.", "resposta": "Teclado"},
    {"id": 25, "pergunta": "O que é, o que é? Tem muitas teclas, mas não toca música, tem muitos botões, mas não abotoa.", "resposta": "Calculadora"},
    {"id": 26, "pergunta": "O que é, o que é? Tem muitas palavras, mas não fala, tem muitas histórias, mas não conta.", "resposta": "Livro"},
    {"id": 27, "pergunta": "O que é, o que é? Tem muitas ruas, mas não tem carros, tem muitas casas, mas não tem pessoas.", "resposta": "Tabuleiro"},
    {"id": 28, "pergunta": "O que é, o que é? Tem muitas pernas, mas não anda, tem muitas asas, mas não voa.", "resposta": "Cadeira"},
    {"id": 29, "pergunta": "O que é, o que é? Tem muitas bocas, mas não come, tem muitas línguas, mas não fala.", "resposta": "Sino"},
    {"id": 30, "pergunta": "O que é, o que é? Tem muitas cores, mas não pinta, tem muitas formas, mas não desenha.", "resposta": "Vitral"},
    {"id": 31, "pergunta": "O que é, o que é? Tem muitas folhas, mas não é árvore, tem muitas páginas, mas não é livro.", "resposta": "Calendário"},
    {"id": 32, "pergunta": "O que é, o que é? Tem muitas cordas, mas não amarra, tem muitas notas, mas não escreve.", "resposta": "Piano"},
    {"id": 33, "pergunta": "O que é, o que é? Tem muitas chaves, mas não abre portas, tem muitos espaços, mas não guarda nada.", "resposta": "Mapa"},
    {"id": 34, "pergunta": "O que é, o que é? Tem muitas teclas, mas não toca música, tem muitos botões, mas não abotoa.", "resposta": "Controle remoto"},
    {"id": 35, "pergunta": "O que é, o que é? Tem muitas palavras, mas não fala, tem muitas histórias, mas não conta.", "resposta": "Jornal"},
    {"id": 36, "pergunta": "O que é, o que é? Tem muitas ruas, mas não tem carros, tem muitas casas, mas não tem pessoas.", "resposta": "Mapa"},
    {"id": 37, "pergunta": "O que é, o que é? Tem muitas pernas, mas não anda, tem muitas asas, mas não voa.", "resposta": "Mesa"},
    {"id": 38, "pergunta": "O que é, o que é? Tem muitas bocas, mas não come, tem muitas línguas, mas não fala.", "resposta": "Órgão"},
    {"id": 39, "pergunta": "O que é, o que é? Tem muitas cores, mas não pinta, tem muitas formas, mas não desenha.", "resposta": "Mosaico"},
    {"id": 40, "pergunta": "O que é, o que é? Tem muitas folhas, mas não é árvore, tem muitas páginas, mas não é livro.", "resposta": "Álbum de fotos"},
    {"id": 41, "pergunta": "O que é, o que é? Tem muitas cordas, mas não amarra, tem muitas notas, mas não escreve.", "resposta": "Harpa"},
    {"id": 42, "pergunta": "O que é, o que é? Tem muitas chaves, mas não abre portas, tem muitos espaços, mas não guarda nada.", "resposta": "Partitura"},
    {"id": 43, "pergunta": "O que é, o que é? Tem muitas teclas, mas não toca música, tem muitos botões, mas não abotoa.", "resposta": "Máquina de escrever"},
    {"id": 44, "pergunta": "O que é, o que é? Tem muitas palavras, mas não fala, tem muitas histórias, mas não conta.", "resposta": "Revistas"},
    {"id": 45, "pergunta": "O que é, o que é? Tem muitas ruas, mas não tem carros, tem muitas casas, mas não tem pessoas.", "resposta": "Maquete"},
    {"id": 46, "pergunta": "O que é, o que é? Tem muitas pernas, mas não anda, tem muitas asas, mas não voa.", "resposta": "Poltrona"},
    {"id": 47, "pergunta": "O que é, o que é? Tem muitas bocas, mas não come, tem muitas línguas, mas não fala.", "resposta": "Relógio"},
    {"id": 48, "pergunta": "O que é, o que é? Tem muitas cores, mas não pinta, tem muitas formas, mas não desenha.", "resposta": "Vidro colorido"},
    {"id": 49, "pergunta": "O que é, o que é? Tem muitas folhas, mas não é árvore, tem muitas páginas, mas não é livro.", "resposta": "Bloco de notas"},
    {"id": 50, "pergunta": "O que é, o que é? Tem muitas cordas, mas não amarra, tem muitas notas, mas não escreve.", "resposta": "Violão"}
]
@app.route('/')
def index():
    return 'API TÁ ON PAI 💥'

@app.route('/charadas', methods=['GET'])
def lista():
    return jsonify(charadas), 200

@app.route('/charadas/<campo>/<busca>', methods=['GET'])
def busca(campo, busca):
    if campo not in ['id', 'pergunta', 'resposta']:
        return jsonify({'mensagem': 'Erro - Campo não encontrado!'}), 400

    if campo == 'id':
        try:
            busca = int(busca)
        except ValueError:
            return jsonify({'mensagem': 'Erro - ID deve ser um número!'}), 400

    for cada_charada in charadas:
        if campo == 'pergunta' or campo == 'resposta':
            if cada_charada[campo].lower() == busca.lower():
                return jsonify(cada_charada), 200
        else:
            if cada_charada[campo] == busca:
                return jsonify(cada_charada), 200

    return jsonify({'mensagem': 'Erro - Charada não encontrada!'}), 404

@app.route('/charadas/aleatoria', methods=['GET'])
def charada_aleatoria():
    charada = random.choice(charadas)
    return jsonify(charada), 200    

if __name__ == '__main__':
    app.run(debug=True)