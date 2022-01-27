"""__init__ : creation of the Flask app"""
from pathlib import Path
from werkzeug.utils import secure_filename
from flask import Response, render_template, Blueprint, request, Flask, jsonify
from development.functions import allowed_file, show_text_id, show_metadata_id
from development.extract import store_in_database

def create_app():
    """Creation of Flask API"""
    app = Flask(__name__)
    @app.route("/", methods=["GET", "POST"])
    @app.route("/documents", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            file = request.files["file"]
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = Path().joinpath('uploads', filename)
                # Save the file in an upload folder
                file.save(filepath)
                # Extract and persist the file in the database
                doc_id = store_in_database(filepath)
                return jsonify({'message': f"The file '{filename}' has been sent successfully!"
                                           f"The id of this pdf is {doc_id}"})

        message = request.args.get("message")
        if None is message:
            message = ""
        return render_template("index.html", title="page", message=message)

    @app.route("/documents/<int:doc_id>", methods=["GET"])
    def get_document(doc_id):
        meta_dict = show_metadata_id(doc_id)
        data = dict(meta_dict)
        for key, value in data.items():
            data[key] = str(value)
        # meta_dict = json.load(meta_dict)
        return jsonify(data)

    @app.route("/text/<int:doc_id>", methods=["GET"])
    def get_text(doc_id):
        text = show_text_id(doc_id)
        return jsonify({'text': text[0]})

    
    @app.route("/test/<int:doc_id>", methods=["GET"])
    def test(doc_id):
        return doc_id

    return app
