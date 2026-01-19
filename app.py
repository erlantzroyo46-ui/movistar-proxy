from flask import Flask, Response, request
import os

app = Flask(__name__)

@app.route("/playlist.m3u8")
def playlist():
    # Cabecera profesional con guía de canales (EPG)
    m3u = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/davidmuma/EPG_Movistar/master/guide.xml"\n'
    
    # La "llave" para que Movistar no bloquee la señal
    ua = "|User-Agent=AppleTV6,2/18L203"
    
    canales = [
        # --- FÚTBOL Y DEPORTES ---
        {"n": "M. LALIGA TV", "id": "LALIGA", "g": "Fútbol"},
        {"n": "DAZN LALIGA", "id": "DAZNLALIGA", "g": "Fútbol"},
        {"n": "M. Liga de Campeones", "id": "CHAMPIONS", "g": "Fútbol"},
        {"n": "LaLiga Hypermotion", "id": "HYPERMOTION", "g": "Fútbol"},
        {"n": "Copa del Rey", "id": "COPA", "g": "Fútbol"},
        {"n": "DAZN F1", "id": "DAZNF1", "g": "Motor"},
        {"n": "Eurosport 1", "id": "EUROSPORT1", "g": "Deportes"},
        
        # --- TDT ESPAÑA ---
        {"n": "La 1", "id": "TVE", "g": "TDT"},
        {"n": "Antena 3", "id": "ANTENA3", "g": "TDT"},
        {"n": "Cuatro", "id": "CUATRO", "g": "TDT"},
        {"n": "Telecinco", "id": "TELECINCO", "g": "TDT"},
        {"n": "La Sexta", "id": "LASEXTA", "g": "TDT"},
        {"n": "FDF", "id": "FDF", "g": "TDT"},
        {"n": "Mega", "id": "MEGA", "g": "TDT"},
        {"n": "Energy", "id": "ENERGY", "g": "TDT"},
        {"n": "Divinity", "id": "DIVINITY", "g": "TDT"},
        
        # --- CINE Y SERIES ---
        {"n": "M. Estrenos", "id": "ESTRENOS", "g": "Cine"},
        {"n": "M. Acción", "id": "ACCION", "g": "Cine"},
        {"n": "Warner TV", "id": "WARNERTV", "g": "Series"},
        {"n": "FOX", "id": "FOX", "g": "Series"},
        
        # --- ADULTOS ---
        {"n": "Playboy TV", "id": "PLAYBOY", "g": "Adultos"},
        {"n": "Vivid Red", "id": "VIVIDRED", "g": "Adultos"}
    ]
    
    for c in canales:
        m3u += f'#EXTINF:-1 tvg-id="{c["id"]}" group-title="{c["g"]}", {c["n"]}\n'
        m3u += f'https://ver.movistarplus.es/apple/live/{c["id"]}/{c["id"]}.m3u8{ua}\n'
    
    return Response(m3u, mimetype='application/x-mpegurl')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
