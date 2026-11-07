from flask import Flask, jsonify
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

# Encendiendo el servidor
# Buscas evitar prender y apgar el servidor por cada cambio
# Debes de usar debug=True
# El servidor ser reiniciara solo cuando vea un cambio
# tambien nos indicara los errores que existieran
app.run(debug=True)