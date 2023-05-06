from flask import Flask, render_template, request, Response
from PyPDF2 import PdfReader, PdfWriter
from werkzeug.utils import secure_filename
import os
import tempfile

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pdf_file = request.files["pdf_file"]
        password = request.form["password"]

        if pdf_file and password:
            filename = secure_filename(pdf_file.filename)
            encrypted_pdf_path = encrypt_pdf(pdf_file, password)

            with open(encrypted_pdf_path, "rb") as f:
                response = Response(f.read(), content_type="application/pdf")
                response.headers["Content-Disposition"] = f"attachment; filename=encrypted_{filename}"
                return response

    return render_template("index.html")

def encrypt_pdf(pdf_file, password):
    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    encrypted_pdf_path = os.path.join(tempfile.gettempdir(), f"encrypted_{secure_filename(pdf_file.filename)}")
    with open(encrypted_pdf_path, "wb") as output_file:
        writer.write(output_file)

    return encrypted_pdf_path


if __name__ == "__main__":
    app.run(debug=True)
