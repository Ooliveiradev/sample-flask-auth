from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user
from models.user import User
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
# view login

# Session <- conexao ativa(sempre que abro uma sessao de banco de dados)

@app.route('/login', methods=["POST"])
def login():
  data = request.json
  if not data:
    return jsonify({"message": "JSON inválido"}), 400

  username = data.get('username')
  password = data.get('password')
  
  if username and password:
    # Login
    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
      login_user(user)
      print(current_user.is_authenticated)
      return jsonify({"message": "Autenticacao realizada com sucesso"})

  return jsonify({"message": "Credenciais invalidas"}), 400

@app.route('/hello-world', methods=["GET"])
def hello_world():
  return 'Hello world'

if __name__ == '__main__':
  app.run(debug=True)
  