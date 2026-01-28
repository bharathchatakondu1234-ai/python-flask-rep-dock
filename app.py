from flask import Flask
app = Flask(__name__)
#it is the home route
@app.route('/')
def home():
    return "CI/CD Pipeline Successful! App is Live."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
