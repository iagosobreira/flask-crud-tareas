from flask import Blueprint, render_template, request, session, redirect, url_for
from sqlalchemy import text 
from extensions import db
from tareas.services import obtener_tareas_usuario
from functools import wraps
from usuario.services import comprobarEmail

user_db=Blueprint("users", __name__)

@user_db.route("/crear_registro",methods=['POST'])

def crear_registro():
    
    if request.method=='POST':
        nombre=request.form['nombre']
        email=request.form['email']
        password=request.form['password']
        
        if comprobarEmail(email):
        
            sql=text('INSERT INTO usuarios (correo, contrasena, nombre) values (:email, :password, :nombre)')
            
            db.session.execute(sql,{
                "email":email,
                "password": password,
                "nombre": nombre
            })
            
            db.session.commit()
            
            return redirect(url_for("main.inicio"))
        
        else:
            
            return redirect(url_for("main.registro"))
    
@user_db.route("/login", methods=["POST"])
def login():
    correo = request.form['email']
    password = request.form['password']

    sql = text("SELECT * FROM usuarios WHERE correo = :correo")
    result = db.session.execute(sql, {'correo': correo}).fetchone()

    if result and password == result.contrasena:
        session['user_id'] = result.id
        session['user_name'] = result.nombre

        return redirect(url_for("users.area"))  # 👈 CLAVE

    return redirect(url_for("main.inicio"))

@user_db.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("main.inicio"))

@user_db.route('/volver')
def volver():
    return redirect(url_for("main.inicio"))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


@user_db.route("/area")
@login_required
def area():
    if "user_id" not in session:
        return redirect(url_for("users.login"))

    tareas = obtener_tareas_usuario(session["user_id"])

    return render_template(
        "area.html",
        usuario=session["user_name"],
        tareas=tareas
    )
    


