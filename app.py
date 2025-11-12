from flask import Flask , render_template , request , redirect , url_for, flash
import requests

app= Flask(__name__)

app.config["SECRET_KEY"] = "una_clave_muy_larga_y_dificil_de_adivinar"

@app.route("/")

def index():
    return render_template('index.html')

@app.route("/search", methods=["POST"])
def search():
    pokemon_name = request.form.get("pokemon_name", "").strip().lower()

    if not pokemon_name:
        flash("Por favor, ingresa el nombre de un Pokémon.", "error")
        return redirect(url_for("index"))
if __name__ == "__main__":
    app.run(debug=True)