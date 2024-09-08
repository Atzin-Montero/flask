from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>Hola!</h1> <h2>En esta página podras: </h2>
    <a href="/random_fact">¡Ver un hecho al azar!</a>
    <a href="/random_number">¡Ver un número al azar entre 1 y 100!</a>
    <a href="/random_password">¡Generar una contrasena al azar!
    <a href="/random_meme">¡Ver un meme al azar!
    """
@app.route("/random_fact")
def random_fact():
    facts_list = ["El corazón de una gamba está en su cabeza.",
                  "El primer vuelo en avión fue el 17 de diciembre de 1903",
                  "El teléfono móvil tiene 10 veces más bacterias que un asiento de inodoro promedio.",
                  "México es el principal productor de cerveza del mundo.",
                  "La comida mexicana se considera Patrimonio de la Humanidad.",
                  "Nieva en el desierto del Sahara.",
                  "Macchu Pichu es una ciudad a prueba de terremotos.",
                  "La Reina Isabel II era mecánica de formación.",
                  "Los humanos tenemos huellas en la lengua."]
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/random_number")
def random_number():
    numeros = [0,1,2]
    i = 3
    for i in range(100):
        numeros.append(i)
        i = i+1
    return f'<p>{random.choice(numeros)}</p>'

@app.route("/random_password")
def random_password():
    elements = "+-/*!&$#?=@<>"
    password = ""
    i = 0
    for i in range(8):
        password += random.choice(elements)
        i = i+1
    return f'<p>{password}</p>'

@app.route("/random_meme")
def random_meme():
    meme = [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAqeC9oeIBQZl4Kewq8PCVlcQZJzFzqT6_qQ&s",
        "https://statics.memondo.com/p/s1/crs/2021/12/CR_1216327_3c143e0bd5494830875dce078aebc446_memes_dolorosamente_familiares_sobre_programacion_thumb_fb.jpg?cb=723227",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSM9iGM8VxLLXoF_kyRIv1TSVal6CHxxF4PA&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbi7ZW13mszWyoUusTs2zMZrtvMImMIvCytg&s",
        "https://i.pinimg.com/236x/5a/4d/a4/5a4da48adfcc6bf1fa7ea6d57c4ff0f9.jpg",
        "https://tecnofacts.mx/wp-content/uploads/2018/11/memes-de-programadores-1.jpg",
        "https://www.boredpanda.es/blog/wp-content/uploads/2022/03/03-6228a2ac81c49_hwurhp7crzf81-png__700-622b13a1722c6__700.jpg",
        "https://i.pinimg.com/564x/bd/68/af/bd68af256a4c6fd0ada2f60183e88f39.jpg",
        "https://images7.memedroid.com/images/UPLOADED843/63769ad64c543.jpeg",
        "https://finofilipino.org/wp-content/uploads/2024/03/werfqdecwerwegrtg.jpg"
    ]
    return f'<img src = "{random.choice(meme)}" alt = "Meme">'


app.run(debug=True)
