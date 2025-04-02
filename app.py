from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    headers = dict(request.headers)
    email = headers.get("X-MS-CLIENT-PRINCIPAL-NAME")

    if not email:
        return "<h3>❌ No estás autenticado. No se recibió ningún correo.</h3>"

    return f"""
        <h3>✅ Usuario autenticado</h3>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Filtro pasó:</strong> {"Sí" if email.strip().lower().endswith("@bestvalencia.org") else "NO ❌"}</p>
        <p><strong>Raw headers:</strong></p>
        <pre>{"".join(f"{k}: {v}\n" for k, v in headers.items())}</pre>
    """


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
