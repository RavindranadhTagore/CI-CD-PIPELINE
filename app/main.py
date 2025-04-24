from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>CI/CD Deployed Successfully with Python!</h1>
             <p>CI/CD stands for Continuous Integration and Continuous Deployment (or Continuous Delivery). It is a software development practice that automates the integration, testing, and deployment of code changes, enabling faster and more reliable delivery of applications</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
