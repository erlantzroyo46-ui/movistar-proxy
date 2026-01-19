from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/playlist.m3u8")
def playlist():
    # Cabecera profesional con guía de canales
    m3u = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/davidmuma/EPG_Movistar/master/guide.xml"\n'
    
    # Este es el User-Agent más compatible con Android TV para evitar el 0% de buffer
    ua = "|User-Agent=Mozilla/5.0 (Viera; rv:45.0) Gecko/20100101 Firefox/45.0 MyVideo/2.0"
    
    canales = [
        # --- FÚTBOL TOTAL (TODOS LOS DIALES) ---
        {"n": "M. LALIGA TV", "id": "LALIGA", "g": "Fútbol"},
        {"n": "M. LALIGA TV 2", "id": "LALIGA2", "g": "Fútbol"},
        {"n": "DAZN LALIGA", "id": "DAZNLALIGA", "g": "Fútbol"},
        {"n": "M. Liga de Campeones", "id": "CHAMPIONS", "g": "Fútbol"},
        {"n": "M. Liga de Campeones 2", "id": "CHAMPIONS2", "g": "Fútbol"},
        {"n": "LaLiga Hypermotion", "id": "HYPERMOTION", "g": "Fútbol"},
        {"n": "Copa del Rey", "id": "COPA", "g": "Fútbol"},
        
        # --- MOTOR Y DEPORTES ---
        {"n": "DAZN F1", "id": "DAZNF1", "g": "Motor"},
        {"n": "DAZN 1", "id": "DAZN1", "g": "Deportes"},
        {"n": "DAZN 2", "id": "DAZN2", "g": "Deportes"},
        {"n": "Eurosport 1", "id": "EUROSPORT1", "g": "Deportes"},
        {"n": "M. Deportes", "id": "DEPORTES", "g": "Deportes"},

        # --- TDT ESPAÑA COMPLETA ---
        {"n": "La 1", "id": "TVE", "g": "TDT"},
        {"n": "La 2", "id": "TVE2", "g": "TDT"},
        {"n": "Antena 3", "id": "ANTENA3", "g": "TDT"},
        {"n": "Cuatro", "id": "CUATRO", "g": "TDT"},
        {"n": "Telecinco", "id": "TELECINCO", "g": "TDT"},
        {"n": "La Sexta", "id": "LASEXTA", "g": "TDT"},
        {"n": "FDF", "id": "FDF", "g": "TDT"},
        {"n": "Energy", "id": "ENERGY", "g": "TDT"},
        {"n": "Mega", "id": "MEGA", "g": "TDT"},
        {"n": "Trece", "id": "TRECE", "g": "TDT"},

        # --- CINE, SERIES Y ADULTOS ---
        {"n": "M. Estrenos", "id": "ESTRENOS", "g": "Cine"},
        {"n": "M. Acción", "id": "ACCION", "g": "Cine"},
        {"n": "Warner TV", "id": "WARNERTV", "g": "Series"},
        {"n": "FOX", "id": "FOX", "g": "Series"},
        {"n": "Playboy TV", "id": "PLAYBOY", "g": "Adultos"},
        {"n": "Vivid Red", "id": "VIVIDRED", "g": "Adultos"}
    ]
    
    for c in canales:
        m3u += f'#EXTINF:-1 tvg-id="{c["id"]}" group-title="{c["g"]}", {c["n"]}\n'
        # El User-Agent pegado al enlace es lo que intentará forzar la imagen
        m3u += f'https://ver.movistarplus.es/apple/live/{c["id"]}/{c["id"]}.m3u8{ua}\n'
    
    return Response(m3u, mimetype='application/octet-stream')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
