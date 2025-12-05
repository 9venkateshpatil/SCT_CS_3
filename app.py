# app.py
from flask import Flask, render_template, request
from password_utils import check_password_strength

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    password = ""

    if request.method == "POST":
        # Get password from form
        password = request.form.get("password", "")

        if password:
            # Call our logic function
            result = check_password_strength(password)

    # Pass data to the template
    return render_template("index.html", result=result, password=password)


if __name__ == "__main__":
    # Debug mode for local development
    app.run(debug=True)
