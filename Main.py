from flask import Flask, render_template, request, redirect, url_for, session, flash
from dotenv import load_dotenv
load_dotenv()

from models.firebase import initialize_firebase
from viewmodels.rutinas_vm import crear_usuario_desde_form, obtener_rutinas_para_usuario

app = Flask(__name__)
app.secret_key = "clave"

initialize_firebase()

@app.route("/")
def index():
    return redirect(url_for("encuesta"))

@app.route("/Encuesta", methods=["GET", "POST"])
def encuesta():
    if request.method == "POST":
        usuario = crear_usuario_desde_form(request.form)
        session["usuario_actual"] = usuario.nombre
        return redirect(url_for("rutina"))

    return render_template("Encuesta.html")


@app.route("/Rutina")
def rutina():
    nombre = session.get("usuario_actual")

    if not nombre:
        flash("Completa la encuesta primero.", "warning")
        return redirect(url_for("encuesta"))

    data = obtener_rutinas_para_usuario(nombre)

    return render_template(
        "Rutina.html",
        rutinas=data["rutinas"],
        deporte=data["deporte"],
        nivel=data["nivel"],
        complicacion=data["complicacion"]
    )


if __name__ == "__main__":
    app.run(debug=True)
