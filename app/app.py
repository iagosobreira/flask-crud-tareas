from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template
from config import Config
from extensions import db

app=Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from main.routes import main_bd
from usuario.routes import user_db
from tareas.routes import tareas_bd

app.register_blueprint(main_bd)
app.register_blueprint(user_db)
app.register_blueprint(tareas_bd)

if __name__ == "__main__":
    app.run(debug=True)