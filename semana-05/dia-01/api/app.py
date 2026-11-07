from flask import Flask, jsonify, request
import psycopg2 # Este es mi motor

app = Flask(__name__) # La creacion de tu servidor

# Vamos a conectar nuestro servidor (API) con la bd
# Debes de tener instalado psycopg2 => PostgreSQL
#                          mysqlclient => MySQL
# pip install psycopg2

# CONEXION 🔌
# Vamos a crear un funcion para poder conectarnos a nuestra BD
# Informacion o los daots que vas a enviar son los siguientes:
#  host     => Es el lugar donde esta alojado tu bd (localhost, 157.15.65.68)
#  database => Es el nombre de la bd a la que quieres conectarte (canciones)
#  user     => El usuario de tu bd (postgres)
#  password => La contraseña de tu bd (root)
#  port     => Es el puerto donde corre la bd (5432)
def get_db_conection():
   conexion = psycopg2.connect(
                        host='localhost',
                        database='canciones',
                        user='postgres',
                        password='root',
                        port='5432'
                     )

   return conexion

@app.route("/api/artistas", methods=["GET"])
def get_artistas():
   # 01. Conectarte a la BD
   conn = get_db_conection() # Me conecto y guardo la conexion
   # 02. Crear un cursor => Donde podemos ejecutar SQL
   cur = conn.cursor()
   # 03. Vamos a ejecutar la consulta SQL
   cur.execute("SELECT * FROM artistas")
   # 04. Guardar la respuesta
   filas = cur.fetchall()
   # 05. Vamos a cerrar el cursor y la conexion
   cur.close() # Cierro el cursor
   conn.close() # Cierro la conexion

   # filas  (Esta son las filas que guade)
   # [(1, 'Grupo 5', 'Cumbia', 'Perú', True, datetime.datetime(2026, 11, 6, 19, 20, 22, 486835)), 
   # (2, 'Agua Marina', 'Cumbia', 'Perú', True, datetime.datetime(2026, 11, 6, 19, 20, 22, 486835)),
   #  (3, 'Armonía 10', 'Cumbia', 'Perú', True, datetime.datetime(2026, 11, 6, 19, 20, 22, 486835)),
   # ]

   # id, nombre, genero, pais_origen, activo, fecha_creacion

   # 06. Formateo
   resultados_transformados = []
   for elmt in filas:
      formato = {
         "id": elmt[0],
         "nombre": elmt[1],
         "genero": elmt[2],
         "pais_origen": elmt[3],
         "activo": elmt[4]
      }
      resultados_transformados.append(formato)

   # 07. Retonar informacion o responder
   # 🏅 SIEMPRE debe retonar una respuesta
   # El formato de la respuesta es en JSON
   # Para transformar la respuesta en JSON debes de importar
   # from flask import jsonify (va en la parte superior)
   return jsonify(resultados_transformados)

# RETO 01: 
# Crear un endpoint del tipo GET, llamado /api/canciones
# Este endpoint debe de devolver todas las canciones de la tabla
# canciones
# La respuesta debe ser todas las canciones en JSON
@app.route("/api/canciones", methods=["GET"])
def get_canciones():
   conn = get_db_conection()
   cur = conn.cursor()
   cur.execute("SELECT * FROM canciones")
   filas = cur.fetchall()
   cur.close()
   conn.close()

   # (1, 'La Cumbia de las Aventuras', 'Grupo 5', 210, 2005, 1)
   # id, titulo, albun, duracion_segundos, anio_lanzamiento
   resultado_formateado = []
   for elmt in filas:
      formato = {
         "id": elmt[0],
         "titulo": elmt[1],
         "albun": elmt[2],
         "duracion": elmt[3],
         "anio": elmt[4]
      }
      resultado_formateado.append(formato)

   return jsonify(resultado_formateado)

# Necesitamos que se devuelva a un solo artista
# Se cree un endpoint el cual devuelva al artista segun el id
#  /api/artistas/<id>
# este endpoint tiene que ser del tipo GET

@app.route("/api/artistas/<int:id>", methods=["GET"])
def get_single_artist(id):
   conn = get_db_conection() # Conexion
   cur = conn.cursor() # Cursor
   # ✖️  cur.execute(f"SELECT * FROM artistas WHERE id = {id}")
   cur.execute("SELECT * FROM artistas WHERE id = %s", (id,))
   fila = cur.fetchone()
   cur.close()
   conn.close()
   # (2, 'Agua Marina', 'Cumbia', 'Perú', True, datetime.datetime(2026, 11, 6, 19, 20, 22, 486835))

   if fila is None:
      return {
         "msg": "Artista no encontrado"
      }, 404

   return {
      "id": fila[0],
      "nombre": fila[1],
      "genero": fila[2],
      "pais_origen": fila[3],
      "activo": fila[4]
   }

# Necesitamos que se registre informacion de los artistas
# Se solicita que se cree un endpoint => /api/add-artistas
# Tiene que ser del tipo POST => Insertar informacion
@app.route("/api/add-artistas", methods=["POST"])
def add_artistas():
   # Vas a capturar el JSON que te va enviar el frontend
   # {
   #    "nombre": "Rafaga",
   #    "genero": "Cumbia",
   #    "pais_origen": "Argentina"
   # }
   # Para capturar el JSON que te envia el cliente (frontend)
   # Tu debes de importar 
   # from flask import request
   # 01. Capturar la informacion
   data = request.json
   # 02. Validaciones
   # El json este vacio
   if not data:
      return {
         "msg": "Debes de enviar la informacion"
      }

   if "nombre" not in data:
      return {
         "msg": "Debes de enviar el nombre del artista"
      }

   if "genero" not in data:
      return {
         "msg": "Debes de enviar el genero"
      }
   # 03. Vamos a conectarnos y crear el cursor
   conn = get_db_conection()
   cur = conn.cursor()
   # {
   #    "nombre": "Rafaga",
   #    "genero": "Cumbia",
   #    "pais_origen": "Argentina"
   # }
   # 04. Ejecutar tu inserccion y grabar 
   cur.execute("""INSERT INTO artistas (nombre, genero, pais_origen) 
                  VALUES (%s, %s, %s) """,
                  (data["nombre"], data["genero"], data["pais_origen"]))

   conn.commit() # Graba tu inserccion en la bd

   cur.close()
   conn.close()

   return {
      "msg": "Creacion exitosa"
   }, 201

# RETO 02:
# Necesitamos que se registre informacion en las canciones
# Se solicita que se cree un endpoint => "/api/add-canciones"
# Este tiene que ser del tipo POST
# # {
#    titulo: "No te vayas",
#    albun: "Rafaga",
#    duracion_segundos: 230,
#    anio_lanzamiento: 2016,
#    artista_id: 9
# #}



# Encendiendo el servidor
# Buscas evitar prender y apgar el servidor por cada cambio
# Debes de usar debug=True
# El servidor ser reiniciara solo cuando vea un cambio
# tambien nos indicara los errores que existieran
app.run(debug=True)