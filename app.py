from flask import Flask, Response, redirect
import os

app = Flask(__name__)

@app.route("/playlist.m3u8")
def playlist():
    base_url = "https://movistar-proxy.onrender.com"
    canales = [
        # --- FÚTBOL TOTAL ---
        {"n": "M. LALIGA TV", "g": "Fútbol", "id": "LALIGA"},
        {"n": "DAZN LALIGA", "g": "Fútbol", "id": "DAZNLALIGA"},
        {"n": "M. Liga de Campeones", "g": "Fútbol", "id": "CHAMPIONS"},
        {"n": "LaLiga Hypermotion (2ª)", "g": "Fútbol", "id": "HYPERMOTION"},
        {"n": "Copa del Rey", "g": "Fútbol", "id": "COPA"},
        {"n": "M. LALIGA TV 2", "g": "Fútbol", "id": "LALIGA2"},
        {"n": "DAZN LALIGA 2", "g": "Fútbol", "id": "DAZNLALIGA2"},
        
        # --- DEPORTES ---
        {"n": "DAZN F1", "g": "Deportes", "id": "DAZNF1"},
        {"n": "DAZN 1", "g": "Deportes", "id": "DAZN1"},
        {"n": "Eurosport 1", "g": "Deportes", "id": "EUROSPORT1"},
        {"n": "Eurosport 2", "g": "Deportes", "id": "EUROSPORT2"},

        # --- TDT ESPAÑA ---
        {"n": "La 1", "g": "TDT", "id": "TVE"},
        {"n": "Antena 3", "g": "TDT", "id": "ANTENA3"},
        {"n": "Cuatro", "g": "TDT", "id": "CUATRO"},
        {"n": "Telecinco", "g": "TDT", "id": "TELECINCO"},
        {"n": "La Sexta", "g": "TDT", "id": "LASEXTA"},
        {"n": "FDF", "g": "TDT", "id": "FDF"},
        {"n": "Mega", "g": "TDT", "id": "MEGA"},
        {"n": "Energy", "g": "TDT", "id": "ENERGY"},
        {"n": "Divinity", "g": "TDT", "id": "DIVINITY"},
        {"n": "Boing", "g": "TDT", "id": "BOING"},

        # --- CINE Y SERIES ---
        {"n": "M. Estrenos", "g": "Cine", "id": "ESTRENOS"},
        {"n": "M. Acción", "g": "Cine", "id": "ACCION"},
        {"n": "M. Comedia", "g": "Cine", "id": "COMEDIA"},
        {"n": "Warner TV", "g": "Series", "id": "WARNERTV"},
        {"n": "Fox", "g": "Series", "id": "FOX"},

        # --- ADULTOS ---
        {"n": "Playboy TV", "g": "Adultos", "id": "PLAYBOY"},
        {"n": "Vivid Red", "g": "Adultos", "id": "VIVIDRED"}
    ]
    m3u = "#EXTM3U\n"
    for c in canales:
        m3u += f'#EXTINF:-1 group-title="{c["g"]}", {c["n"]}\n'
        m3u += f'{base_url}/v/{c["id"]}.m3u8\n'
    # Esta línea arregla el error de tu foto
    return Response(m3u, mimetype='application/x-mpegurl')

@app.route("/v/<chid>.m3u8")
def stream(chid):
    return redirect(f"https://ver.movistarplus.es/apple/live/{chid}/{chid}.m3u8")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
