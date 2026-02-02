from sqlalchemy import text
from extensions import db

def comprobarEmail(email):
    
    sql=text('Select * from usuarios where correo = :email')
    
    data=db.session.execute(sql,{
        'email':email
    }).fetchone()
    
    if data:
        return False
    else:
        return True