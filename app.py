from flask import Flask, Response, redirect
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor Invisible Activo - Lista Masiva"

@app.route("/playlist.m3u8")
def playlist():
    # Detecta automáticamente la dirección de la nube para que no tengas que poner tu IP
    base_url = "https://" + os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'localhost')
    
    canales = [
        # --- FÚTBOL Y COMPETICIÓN ---
        {"n": "M. LALIGA TV", "g": "Fútbol", "id": "LALIGA"},
        {"n": "DAZN LALIGA", "g": "Fútbol", "id": "DAZNLALIGA"},
        {"n": "M. Liga de Campeones", "g": "Fútbol", "id": "CHAMPIONS"},
        {"n": "LaLiga Hypermotion (2ª)", "g": "Fútbol", "id": "HYPERMOTION"},
        {"n": "Copa del Rey", "g": "Fútbol", "id": "COPA"},
        {"n": "DAZN 1", "g": "Deportes", "id": "DAZN1"},
        {"n": "DAZN 2", "g": "Deportes", "id": "DAZN2"},
        {"n": "DAZN F1", "g": "Deportes", "id": "DAZNF1"},
        {"n": "Eurosport 1", "g": "Deportes", "id": "EUROSPORT1"},
        
        # --- CINE Y SERIES ---
        {"n": "M. Estrenos", "g": "Cine", "id": "ESTRENOS"},
        {"n": "M. Acción", "g": "Cine", "id": "ACCION"},
        {"n": "M. Comedia", "g": "Cine", "id": "COMEDIA"},
        {"n": "M. Drama", "g": "Cine", "id": "DRAMA"},
        {"n": "FOX", "g": "Series", "id": "FOX"},
        {"n": "AXN", "g": "Series", "id": "AXN"},
        {"n": "Warner TV", "g": "Series", "id": "WARNERTV"},
        
        # --- TDT ESPAÑA ---
        {"n": "La 1", "g": "TDT", "id": "TVE"},
        {"n": "Antena 3", "g": "TDT", "id": "ANTENA3"},
        {"n": "Telecinco", "g": "TDT", "id": "TELECINCO"},
        {"n": "laSexta", "g": "TDT", "id": "LASEXTA"},
        
        # --- ADULTOS ---
        {"n": "Playboy TV", "g": "Adultos", "id": "PLAYBOY"},
        {"n": "Vivid Red", "g": "Adultos", "id": "VIVIDRED"},
        {"n": "Hustler TV", "g": "Adultos", "id": "HUSTLER"}
    ]
    
    m3u = "#EXTM3U\n"
    for c in canales:
        m3u += f'#EXTINF:-1 group-title="{c["g"]}", {c["n"]}\n'
        # La tele ya no pide el vídeo a tu casa, lo pide a la nube
        m3u += f'{base_url}/v/{c["id"]}.m3u8\n'
    return Response(m3u, mimetype='text/plain')

@app.route("/v/<chid>.m3u8")
def stream(chid):
    # Redirección directa al flujo de Apple TV (el más estable)
    url = f"https://ver.movistarplus.es/apple/live/{chid}/{chid}.m3u8"
    return redirect(url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
