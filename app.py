from flask import Flask, Response, request
import os

app = Flask(__name__)

@app.route("/playlist.m3u8")
def playlist():
    # Cabecera con EPG para ver la programación en la tele
    m3u = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/davidmuma/EPG_Movistar/master/guide.xml"\n'
    
    # El "secreto" de la lista perfecta: User-Agent pegado al enlace
    ua = "|User-Agent=AppleTV6,2/18L203"
    
    # LISTA MASIVA COMPLETA (PAQUETE PREMIUM)
    canales = [
        # --- MOTOR Y DEPORTES ---
        {"n": "DAZN F1", "id": "DAZNF1", "g": "Motor"},
        {"n": "DAZN 1", "id": "DAZN1", "g": "Deportes"},
        {"n": "DAZN 2", "id": "DAZN2", "g": "Deportes"},
        {"n": "M. Deportes", "id": "DEPORTES", "g": "Deportes"},
        {"n": "Eurosport 1", "id": "EUROSPORT1", "g": "Deportes"},
        
        # --- FÚTBOL (LALIGA Y SEGUNDA) ---
        {"n": "M. LALIGA TV", "id": "LALIGA", "g": "Fútbol"},
        {"n": "DAZN LALIGA", "id": "DAZNLALIGA", "g": "Fútbol"},
        {"n": "LaLiga Hypermotion", "id": "HYPERMOTION", "g": "Fútbol"},
        
        # --- CHAMPIONS Y EUROPA LEAGUE ---
        {"n": "M. Liga de Campeones", "id": "CHAMPIONS", "g": "Champions"},
        {"n": "M. Liga de Campeones 2", "id": "CHAMPIONS2", "g": "Champions"},
        
        # --- TDT ESPAÑA COMPLETO ---
        {"n": "La 1", "id": "TVE", "g": "TDT"},
        {"n": "Antena 3", "id": "ANTENA3", "g": "TDT"},
        {"n": "Cuatro", "id": "CUATRO", "g": "TDT"},
        {"n": "Telecinco", "id": "TELECINCO", "g": "TDT"},
        {"n": "La Sexta", "id": "LASEXTA", "g": "TDT"},
        {"n": "FDF", "id": "FDF", "g": "TDT"},
        {"n": "Mega", "id": "MEGA", "g": "TDT"},
        {"n": "Energy", "id": "ENERGY", "g": "TDT"},
        
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
        # Esto envía a la tele directamente al servidor de origen con la identidad correcta
        m3u += f'https://ver.movistarplus.es/apple/live/{c["id"]}/{c["id"]}.m3u8{ua}\n'
    
    return Response(m3u, mimetype='application/x-mpegurl')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
