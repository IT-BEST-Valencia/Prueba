from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    email = request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")
    headers = dict(request.headers)
    
    if not email:
        return redirect("/.auth/login/google")

    if not email.endswith("@bestvalencia.com"):
        return "<pre>" + "\n".join(f"{k}: {v}" for k, v in headers.items()) + "</pre>", 403
    
    
    print( "<pre>" + "\n".join(f"{k}: {v}" for k, v in headers.items()) + "</pre>")

    return f"<h1>Bienvenido, {email}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
