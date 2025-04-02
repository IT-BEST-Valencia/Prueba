from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    email = request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")

    print( "<pre>" + "\n".join(f"{k}: {v}" for k, v in headers.items()) + "</pre>")

    if not email:
        return redirect("/.auth/login/google")

    if not email.endswith("@bestvalencia.com"):
        return "Acceso denegado: solo permitido para @bestvalencia.com", 403
    
    headers = dict(request.headers)
    

    return f"<h1>Bienvenido, {email}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
