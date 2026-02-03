from flask import Flask, request
import yaml
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Aplicação vulnerável do Atila!"

# Vulnerabilidade 1 — Execução remota
@app.route("/cmd")
def cmd():
    comando = request.args.get("c")
    return os.popen(comando).read()

# Vulnerabilidade 2 — YAML insecure load (RCE)
@app.route("/yaml")
def yaml_vuln():
    data = request.args.get("data", "a: b")
    return str(yaml.load(data, Loader=yaml.Loader))

if __name__ == "__main__":
    app.run(debug=True)
