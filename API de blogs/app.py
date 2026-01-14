from flask import Flask
from Controllers.controller_usuarios import usuarios_bp
from Controllers.controller_posts import posts_bp

app = Flask(__name__)

app.register_blueprint(usuarios_bp)
app.register_blueprint(posts_bp)

if __name__ == "__main__":
    app.run(debug=True)