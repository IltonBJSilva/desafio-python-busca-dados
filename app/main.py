from flask import Flask, jsonify


main = Flask(__name__)

@main.route('/')
def home():
    return jsonify({"Mensagem": "Flask rodando com sucesso"})


if __name__ =='__main__':
    main.run(debug=True)