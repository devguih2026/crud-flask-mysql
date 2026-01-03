from flask import Flask
from controller import projeto_bp

app = Flask(__name__)

app.register_blueprint(projeto_bp)

if __name__ == "__main__":
    app.run(debug=True)