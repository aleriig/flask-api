from flask import jsonify

from . import app
from .models import DBManager


"""
Verbos y formato de endpoints
    
GET /movimientos -----> LISTAR movimientos
POST /movimientos ----> CREAR movimiento
GET /movimientos/1 ---> LEER movimiento con ID 1
POST /movimiento/1 ---> ACTUALIZAR el movimiento con ID 1 (sobreescribe todo el objeto)
PUT /movimientos/1 ---> ACTUALIZAR el movimiento con ID 1 (sobreescribe parcialmente)
DELETE /movimientos/1 -> ELIMINAR el movimiento con ID 1

IMPORTANTE versionar los endpoints (son un contrato)
/api/v1/.....
"""

RUTA = app.config.get("RUTA")

@app.route('/api/v1/movimientos')
def listar_movimientos():
    db = DBManager(RUTA)
    sql = "SELECT * movimientos ORDER BY fecha, id"
    movmientos = db.consulta_SQL(sql)
    return jsonify(movmientos)
    
