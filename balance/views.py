from . import app

@app.route('/')
def inicio():
    # por si una linea es muy larga se puede hacer de esta manera
    return (f"La ruta del archivo de datos es:"
            f"{app.config['RUTA']}")