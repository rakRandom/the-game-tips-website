from config.libs import SQLAlchemy
from api import app
from json import loads


with open("config.json", "r", encoding="UTF-8") as config:
    data = loads(config)["db_connection_settings"]
    DBMS = data["dbms"]
    USER = data["user"]
    PSWD = data["password"]
    HOST = data["host"]
    PORT = data["port"]
    NAME = data["name"]

app.config['SQLALCHEMY_DATABASE_URI'] = f'{DBMS}://{USER}:{PSWD}@{HOST}:{PORT}/{NAME}'
db = SQLAlchemy(app)
