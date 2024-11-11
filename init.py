from flask import Flask
from controller import livro_controllers

app = Flask(__name__)

app.secret_key = 'sua_chave_secreta_aqui'  # Chave secreta para sessão e flash messages

app.register_blueprint(livro_controllers)

if __name__ == "__main__":
    app.run(debug=True)
