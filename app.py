from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    headers = dict(request.headers)
    email = request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")
    
    
    if not email:
        return redirect("/.auth/login/google")

    if not email.endswith("@bestvalencia.org"):
        return "<pre>" + "\n".join(f"{k}: {v}" for k, v in headers.items()) + "</pre>", 403
    

    return f"<h1>Bienvenido, {email}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
