from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
        <head>
            <title>CI/CD Success</title>
        </head>
        <body style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; margin: 0;">
            <h1>CI/CD Pipeline</h1>
            <p>Deployed Successfully with Python!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
