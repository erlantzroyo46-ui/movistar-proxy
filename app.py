from flask import Flask, Response, redirect
import os

app = Flask(__name__)

@app.route("/playlist.m3u8")
def playlist():
    # Detecta tu dirección de Render automáticamente
    base_url = "https://movistar-proxy.onrender.com"
    
    canales = [
        # --- FÚTBOL Y DEPORTES ---
        {"n": "M. LALIGA TV", "g": "Fútbol", "id": "LALIGA"},
        {"n": "DAZN LALIGA", "g": "Fútbol", "id": "DAZNLALIGA"},
        {"n": "M. Liga de Campeones", "g": "Fútbol", "id": "CHAMPIONS"},
        {"n": "LaLiga Hypermotion", "g": "Fútbol", "id": "HYPERMOTION"},
        {"n": "Copa del Rey", "g": "Fútbol", "id": "COPA"},
        {"n": "DAZN F1", "g": "Motor", "id": "DAZNF1"},
        {"n": "Eurosport 1", "g": "Deportes", "id": "EUROSPORT1"},
        
        # --- TDT ESPAÑA ---
        {"n": "La 1", "g": "TDT", "id": "TVE"},
        {"n": "La 2", "g": "TDT", "id": "TVE2"},
        {"n": "Antena 3", "g": "TDT", "id": "ANTENA3"},
        {"n": "Cuatro", "g": "TDT", "id": "CUATRO"},
        {"n": "Telecinco", "g": "TDT", "id": "TELECINCO"},
        {"n": "La Sexta", "g": "TDT", "id": "LASEXTA"},
        {"n": "FDF", "g": "TDT", "id": "FDF"},
        {"n": "Energy", "g": "TDT", "id": "ENERGY"},
        {"n": "Divinity", "g": "TDT", "id": "DIVINITY"},
        {"n": "Mega", "g": "TDT", "id": "MEGA"},
        {"n": "Neox", "g": "TDT", "id": "NEOX"},
        {"n": "Nova", "g": "TDT", "id": "NOVA"},
        {"n": "Treve", "g": "TDT", "id": "TRECE"},
        
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
    
    # Esta línea arregla el error "None of the available extractors"
    return Response(m3u, mimetype='application/x-mpegurl')

@app.route("/v/<chid>.m3u8")
def stream(chid):
    return redirect(f"https://ver.movistarplus.es/apple/live/{chid}/{chid}.m3u8")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
