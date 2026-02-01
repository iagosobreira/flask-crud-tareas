from flask import Blueprint, render_template, request, session, redirect, url_for
from sqlalchemy import text 
from extensions import db

tareas_bd=Blueprint("tareas", __name__)

@tareas_bd.route('/agregar_tarea', methods=['POST'])
def agregar_tareas():
    if request.method=='POST':
        tarea=request.form['tarea']
        
        sql=text('INSERT INTO tareas (tarea, id_usuario, realizada) VALUES (:tarea, :id_usuario, :realizada);')
        
        db.session.execute(sql,{
            'tarea':tarea,
            'id_usuario':session['user_id'],
            'realizada':False
        })
        
        db.session.commit()
        
    return redirect(url_for("users.area"))


@tareas_bd.route('/eliminar_tarea', methods=['POST'])
def eliminar_tarea():
    
    if request.method=='POST':
        id_tarea=request.form['id_tarea']
        
        sql=text('delete from tareas where id = :id_tarea;')
        
        db.session.execute(sql,{
            'id_tarea':id_tarea
        })
        db.session.commit()
    
    return redirect(url_for('users.area'))

@tareas_bd.route('/realizar_tarea', methods=['POST'])
def realizar_tarea():
    
    if request.method=='POST':
        id_tarea=request.form['id_tarea']
        
        sql=text('UPDATE tareas SET realizada = :realizada WHERE id=:id_tarea;')
        
        db.session.execute(sql,{
            'realizada':True,
            'id_tarea':id_tarea
        })
        db.session.commit()
    
    return redirect(url_for('users.area'))





        
    
    