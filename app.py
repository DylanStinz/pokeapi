from flask import Flask , render_template , request , redirect , url_for, flash
import requests


app= Flask(__name__)

app.config["SECRET_KEY"] = "una_clave_muy_larga_y_dificil_de_adivinar"

API = "https://pokeapi.co/api/v2/"

@app.route("/")

def index():
    return render_template('index.html')

@app.route("/search", methods=["POST"])
def search():
    pokemon_name = request.form.get("pokemon_name", "").strip().lower()

    if not pokemon_name:
        flash("Por favor, ingresa el nombre de un Pokémon.", "error")
        return redirect(url_for("index"))
    try:
        resp = requests.get(f"{API}{pokemon_name}")
        if resp.status_code == 200:
            pokemon_data = resp.json()
            pokemon_info = {
                "name": pokemon_data["name"].title(),
                "id": pokemon_data["id"],
                "height": pokemon_data["height"],
                "weight": pokemon_data["weight"],
                "image": pokemon_data["sprites"]["front_default"],
                "types": [t["type"]["name"].title() for t in pokemon_data["types"]],
                "abilities": [a["ability"]["name"].title() for a in pokemon_data["abilities"]],
            }
            return render_template("pokemon.html", pokemon=pokemon_info)
        else:
            flash(f"Pokémon '{pokemon_name}' no encontrado. Intenta con otro nombre.", "error")
            return redirect(url_for("index"))
    except requests.exceptions.RequestException as e:
        flash("Error al buscar el pokemon", "error")
        return redirect(url_for("index"))
if __name__ == "__main__":
    app.run(debug=True)