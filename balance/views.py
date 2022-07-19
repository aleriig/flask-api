from flask import jsonify, request

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
db = DBManager(RUTA)

@app.route("/api/v1/movimientos")
def listar_movimientos():
    try:
        sql = "SELECT * from movimientos ORDER BY fecha, id"
        movimientos = db.consulta_SQL(sql)
        resultado = {
            "status": "success",
            "results": movimientos
        }
    except Exception as error:
        resultado = {
            "status": "error",
            "message": str(error)
        }

    return jsonify(resultado)

@app.route('/api/v1/movimientos', methods=['POST'])
def insertar_movimiento():
    try:
        sql = "INSERT INTO movimientos (fecha, concepto, tipo, cantidad) VALUES (:fecha, :concepto, :tipo, :cantidad)"
        ha_ido_bien = db.consulta_con_parametros(sql, request.json)
        if ha_ido_bien: {
            "status": "success"
        }
        else:
            resultado = {
                "status": "error",
                "message": "Error al inserta el movimiento en la base de datos "
            }
    except Exception as error:
        resultado = {
            "status": "success",
            "results": str(error)
        }

    return jsonify(resultado)
    
