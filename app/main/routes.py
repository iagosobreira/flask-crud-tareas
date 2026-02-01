from flask import Blueprint, render_template

main_bd=Blueprint("main", __name__)

@main_bd.route("/")
def inicio():
    return render_template("index.html")

@main_bd.route("/registro")
def registro():
    return render_template("registro.html")