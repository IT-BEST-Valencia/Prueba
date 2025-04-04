from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Ruta base → redirige al login forzado
@app.route("/")
def root():
    return redirect("/login")

# Forzar inicio de sesión: logout + login con Google
@app.route("/login")
def login():
    return redirect("/.auth/logout?post_logout_redirect_uri=/inicio")

# Página principal (protegida)
@app.route("/inicio")
def inicio():
    email = request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")

    if not email:
        return redirect("/.auth/login/google")

    if not email.strip().lower().endswith("@bestvalencia.org"):
        return "Acceso denegado: solo cuentas de @bestvalencia.org", 403

    return render_template("index.html", email=email)

# Cierre de sesión manual
@app.route("/logout")
def logout():
    return redirect("/.auth/logout?post_logout_redirect_uri=/")

# Arranque del servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
