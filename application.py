from flask import Flask, abort, jsonify, request, current_app
from flask_jwt_simple import JWTManager, jwt_required, create_jwt, get_jwt, get_jwt_identity
from psycopg2.pool import ThreadedConnectionPool

import config
import database

application = Flask(__name__)
application.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY
application.config['JWT_ALGORITHM'] = config.JWT_ALGORITHM
application.config['JWT_HEADER_NAME'] = config.JWT_HEADER_NAME
application.config['JWT_HEADER_TYPE'] = config.JWT_HEADER_TYPE

jwt = JWTManager(application)
dbPool = ThreadedConnectionPool(0, 5, config.DB_CONNECTION_URL)

@application.route('/')
def root():
  abort(404)

@application.route('/api/ping')
@jwt_required
def ping():
  return jsonify(message='pong')

@application.route('/api/stations/id/<int:stationId>')
@jwt_required
def findStationId(stationId):
  try:
    conn = dbPool.getconn()
    cursor = conn.cursor()
    results = database.getStationData(cursor, stationId)
    cursor.close()
    dbPool.putconn(conn)
    return jsonify(results)
  except expression as identifier:
    return null

@application.route('/api/stations/latitude/<lat>/longitude/<lon>')
@jwt_required
def findStationsByLatLon(lat, lon):
  try:
    latConverted = float(lat)
    lonConverted = float(lon)
    conn = dbPool.getconn()
    cursor = conn.cursor()
    results = database.getGeoLocationData(cursor, lat, lon)
    cursor.close()
    dbPool.putconn(conn)
    return jsonify(results)
  except expression as identifier:
    return null

@application.route('/api/postalCode/<int:postalCode>')
@jwt_required
def postalCode(postalCode):
  conn = dbPool.getconn()
  cursor = conn.cursor()
  results = database.getPostalCodeData(cursor, postalCode)
  cursor.close()
  dbPool.putconn(conn)
  return jsonify(results)

# run the application.
if __name__ == "__main__":
  # Setting debug to True enables debug output. This line should be
  # removed before deploying a production application.
  application.debug = False
  application.run()
