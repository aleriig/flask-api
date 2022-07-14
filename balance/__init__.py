from flask import Flask

app = Flask(__name__)
# configuramos para abrir ruta y secret key en un objeto, en este caso la carpeta "config". La carpeta config-ejemplo.py es un template para poner en el repo
app.config.from_object("config")