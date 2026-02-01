from sqlalchemy import text
from extensions import db

def obtener_tareas_usuario(user_id):
    sql = text("""
        SELECT * FROM tareas
        WHERE id_usuario = :id_usuario
    """)
    return db.session.execute(sql, {
        "id_usuario": user_id
    }).fetchall()
