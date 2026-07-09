from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "User Management API",
        "status": "running",
        "version": "1.0"
    }

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }

if __name__ == "__main__":
    app.run(debug=True)