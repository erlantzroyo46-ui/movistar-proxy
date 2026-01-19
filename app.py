from flask import Flask, Response
import os

app = Flask(__name__)

# Función para generar la lista con el User-Agent incrustado
@app.route("/playlist.m3u8")
def playlist():
    # Sustituye con tu URL real de Render si es distinta
    base_url = "https://movistar-proxy.onrender.com"
    # El "truco" para que la tele no falle es añadir el User-Agent al enlace
    ua = "|User-Agent=AppleTV6,2/18L203"
    
    canales = [
        {"n": "La 1", "g": "TDT", "id": "TVE"},
        {"n": "Antena 3", "g": "TDT", "id": "ANTENA3"},
        {"n": "FDF", "g": "TDT", "id": "FDF"},
        {"n": "Mega", "g": "TDT", "id": "MEGA"},
        {"n": "M. LALIGA TV", "g": "Fútbol", "id": "LALIGA"},
        {"n": "DAZN LALIGA", "g": "Fútbol", "id": "DAZNLALIGA"},
        {"n": "M. Liga de Campeones", "g": "Fútbol", "id": "CHAMPIONS"},
        {"n": "Playboy TV", "g": "Adultos", "id": "PLAYBOY"}
    ]
    
    m3u = "#EXTM3U\n"
    for c in canales:
        m3u += f'#EXTINF:-1 group-title="{c["g"]}", {c["n"]}\n'
        # Añadimos la redirección directa para evitar errores de extractor
        m3u += f'https://ver.movistarplus.es/apple/live/{c["id"]}/{c["id"]}.m3u8{ua}\n'
    
    return Response(m3u, mimetype='application/x-mpegurl')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
