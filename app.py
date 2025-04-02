from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    email = request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")

    if not email:
        return "No autenticado", 401

    if not email.strip().lower().endswith("@bestvalencia.org"):
        return "Acceso denegado", 403

    return f"<h1>Bienvenido, {email}. La aplicación está funcionando y deberías solo estar viendo esto con una cuenta bestie.</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)