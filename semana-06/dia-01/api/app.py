# Aqui vamos a crear nuestro archivo base (cerebro) 🧠
# Crear el servidor
from flask import Flask
from db import db  # SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# ⚙️ 03. Configuraciones
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# Integracion de SQLAlchemy en mi proyecto
db.init_app(app)
# Ejecuccion de Flask Migrate
migrate = Migrate(app, db)

# Importacion de los modelos
from models.clientes import ClientesModel
from models.pedidos import PedidosModel
from models.platos import PlatosModel

if __name__ == "__main__":
   app.run(debug=True)