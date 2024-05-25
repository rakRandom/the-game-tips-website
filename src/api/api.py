from config.libs import *
from json import dumps

app = Flask(__name__)
app.debug = True
CORS(app)

from database import db
from database import models

@app.route("/")
def index():
    return "Index"

@app.route("/get-user/<user_id>", methods=['GET'])
@cross_origin()
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    response = app.response_class(
        response=dumps(user_data),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route("/post-user/<name>")
def post_user(name):
    new_user = models.User(name=name)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    except:
        return "Could not add user"