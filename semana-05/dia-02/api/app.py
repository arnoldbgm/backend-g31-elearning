from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Conexion con nuestra BD
# Configuracion de las credenciales de la bd
# DIALECT://USER:PASSWORD@HOST:PORT/DATABASE
# EJEMPLO
# postgresql://postgres:root@localhost:5432/canciones

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/canciones"

# Integrar SQLAlchemy en todo mi servidor
db = SQLAlchemy(app)

# Definir nuestro Modelos (Tablas)
# db.Model => La clase es una Tabla
class Artistas(db.Model):
    # db.Column(TIPO, Configuracion)
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    pais_origen = db.Column(db.String(50))
    activo = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, server_default=db.func.now())

    # Especificar el nombre de tu tabla
    __tablename__ = "artistas"

    def to_dic(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "pais_origen": self.pais_origen,
            "activo": self.activo
        }

class Canciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    album = db.Column(db.String(150))
    duracion_segundos = db.Column(db.Integer)
    anio_lanzamiento = db.Column(db.Integer)
    artistas_id = db.Column(db.Integer, db.ForeignKey("artistas.id"), nullable=False)

    __tablename__ = "canciones"

# Se solicita crear un endpoint, para obtener todos los artistas
# SELECT * FROM artistas; [GET]
@app.route("/api/artistas", methods=["GET"])
def get_artistas():
    # 01. Hacer la consulta
    artistas = Artistas.query.all()

    # [Artistas1, Artistas2]
    # print(artistas[2].nombre)

    resultado_formateado = []
    for elm in artistas:
        # formato = {
        #     "id": elm.id,
        #     "nombre": elm.nombre,
        #     "genero": elm.genero
        # }
        resultado_formateado.append(elm.to_dic())


    return {
        "data": resultado_formateado
    }

app.run(debug=True)