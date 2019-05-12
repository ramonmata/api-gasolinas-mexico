"Database Operations"
import psycopg2

def getStationData(db_cursor, stationId):
    "Returns Alexa Skill Data For Specific Station Id"
    query = 'select gas_alexa_skill_station(%s)'
    db_cursor.execute(query, [stationId])
    data = db_cursor.fetchone()
    if data:
      return data[0]
    else:
      return []

def getGeoLocationData(db_cursor, latitude, longitude):
    "Returns Alexa Skill Data for Geo Search of Stations"
    query = 'select gas_alexa_skill_geolocation(%s, %s)'
    db_cursor.execute(query, [latitude, longitude])
    data = db_cursor.fetchone()
    if data:
      return data[0]
    else:
      return []

def getPostalCodeData(db_cursor, postal_code):
    "Returns Alexa Skill Data for Postal Code search"
    query = 'select gas_alexa_skill(%s)'
    db_cursor.execute(query, [postal_code])
    data = db_cursor.fetchone()
    if data:
      return data[0]
    else:
      return []
