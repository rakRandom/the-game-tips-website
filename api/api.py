from flask import send_from_directory, send_file
from config.libs import *
from json import dumps, load

app = Flask(__name__)
app.debug = True
CORS(app)

# from database import db
# from database import models

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

@app.route("/get-index/<int:id>", methods=['GET'])
@cross_origin()
def get_index(id):
    file_content: dict
    
    with open("./data/landing_page/data.json", "r", encoding="UTF-8") as file:
        file_content = load(file)
    
    content = file_content[id]

    return content

@app.route("/<path:filename>", methods=['GET'])
def get_image(filename):
    return send_from_directory("", filename, mimetype="image", as_attachment=False)
