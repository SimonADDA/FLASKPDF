from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from pathlib import Path
#from API import session_factory, API
from sqlalchemy import select


# from API import API

def allowed_file(filename: str):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {'pdf'}

# # Information sur le document
# @staticmethod
# def get_document(request, doc_id: int):
#         if request.method == "GET":
#             # Executing the query
#             result = session_factory().execute(select(API).where(API.id == doc_id))
#             # Parsing the result
#             for user_obj in result.scalars():
#                 # We build the JSON response
#                 data = {"author": user_obj.author, "subject": user_obj.subject, "title": user_obj.title,
#                         "number_of_pages": user_obj.number_of_pages, "id": user_obj.id, "status": user_obj.status}
#                 # Converting to JSON string
#                 return jsonify(data)
#             # Else, no document found
#             return jsonify({'message':"No document found"})
#         return jsonify({'message':"Incorrect HTTP method"})


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            file = request.files["file"]
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = Path().joinpath('uploads', filename)
                # Save the file in an upload folder
                file.save(filepath)
                # Extract and persist the file in the database
                # doc_id = AppModel().extract_and_persist(filepath)
                return jsonify({'message':f"The file '{filename}' has been sent successfully! Here's his index:"})

        message = request.args.get("message")
        if None is message:
            message = ""
        return render_template("index.html", title="page", message=message)

    # @app.route("/documents/<int:doc_id>", methods=["GET"])
    # def get_document(doc_id):
    #     return API.get_document(request, doc_id)
    #
    # @app.route("/text/<int:doc_id>", methods=["GET"])
    # def get_text(doc_id):
    #     return API.get_text(request, doc_id)
    #
    # folder = Path("uploads")
    # if False is folder.exists():
    #     folder.mkdir()

    return app
