from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    email = request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")

    if not email:
        return redirect("/.auth/login/google")  # Redirección por si alguien llega sin sesión

    return render_template("index.html", email=email)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)