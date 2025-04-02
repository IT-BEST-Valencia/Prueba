from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    email = request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")

    if not email:
        return redirect("/.auth/login/google")

    if not email.endswith("@bestvalencia.com"):
        return "Acceso denegado: solo permitido para @bestvalencia.com", 403

    return f"<h1>Bienvenido, {email}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

