import sqlite3


class DBManager:
    def __init__(self, ruta):
        self.ruta = ruta

    def consulta_SQL(self, consulta):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta)

        self.movimientos = []
        nombres_columnas = []

        for desc_columna in cursor.description:
            nombres_columnas.append(desc_columna[0])
        # nombres_columnas = ['id', 'fecha', 'tipo', 'cantidad']

        datos = cursor.fetchall()
        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre]=dato[indice]
                indice += 1
            self.movimientos.append(movimiento)

        conexion.close()

        return self.movimientos

    def obtenerMovimientoPorId(self, id):
        # TODO: Crear este método y devolver el movimiento cuyo ID sea id
        consulta = "SELECT * FROM movimientos WHERE id=?"
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        # simepre poner una coma seguida del id para que lo detecte como una tupla
        cursor.execute(consulta, (id,))

        datos = cursor.fetchone()
        # preparo un resultado en caso de que no haya datos
        resultado = None
        
        # si hay datos, hacemos un bucle en cada 
        if datos:
            nombres_columnas = []

            for desc_columna in cursor.description:
                nombres_columnas.append(desc_columna[0])

            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre] = datos[indice]
                indice += 1
            resultado = movimiento

        conexion.close()
        return resultado 

    def consulta_con_parametros(self, consulta, params):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = False
        
        try:
            cursor.execute(consulta, params)
            conexion.commit()
            resultado = True
        except Exception as error:
            print("ERROR DB:", error)
            conexion.rollback()
        conexion.close()

        return resultado