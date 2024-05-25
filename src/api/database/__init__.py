from config.libs import SQLAlchemy
from api import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/flask'
db = SQLAlchemy(app)
