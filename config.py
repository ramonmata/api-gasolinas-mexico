from os import getenv
APP_NAME=getenv('APP_NAME', 'Octanos API v1.0')
JWT_SECRET_KEY = getenv('JWT_SECRET_KEY', 'super-secret')
JWT_ALGORITHM = getenv('JWT_ALGORITHM', 'HS256')
JWT_HEADER_NAME = getenv('JWT_HEADER_NAME', 'Authorization')
JWT_HEADER_TYPE = getenv('JWT_HEADER_TYPE', '')
DB_HOST = getenv('OCTANOS_DB_ENDPOINT','octanosdb.some.url')
DB_PORT = getenv('OCTANOS_DB_PORT',1234)
DB_NAME = getenv('OCTANOS_DB_NAME','database-name')
DB_USERNAME = getenv('OCTANOS_DB_USER','database-user')
DB_PASSWORD = getenv('OCTANOS_DB_PASSWORD','database-password')
DB_CONNECTION_URL = "host=%s port=%s dbname=%s user=%s password=%s" % (
  DB_HOST,
  DB_PORT,
  DB_NAME,
  DB_USERNAME,
  DB_PASSWORD)