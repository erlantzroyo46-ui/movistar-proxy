from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/playlist.m3u8")
def playlist():
    m3u = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/davidmuma/EPG_Movistar/master/guide.xml"\n'
    
    # Inyectamos el Referer para que Movistar crea que vienes de su web oficial
    ua = "|User-Agent=AppleTV6,2/18L203|Referer=https://ver.movistarplus.es/"
    
    canales = [
        # --- FÚTBOL TOTAL (LALIGA, CHAMPIONS, MULTIS) ---
        {"n": "M. LALIGA TV", "id": "LALIGA", "g": "Fútbol"},
        {"n": "M. LALIGA TV 2", "id": "LALIGA2", "g": "Fútbol"},
        {"n": "M. LALIGA TV 3", "id": "LALIGA3", "g": "Fútbol"},
        {"n": "DAZN LALIGA", "id": "DAZNLALIGA", "g": "Fútbol"},
        {"n": "DAZN LALIGA 2", "id": "DAZNLALIGA2", "g": "Fútbol"},
        {"n": "M. Liga de Campeones", "id": "CHAMPIONS", "g": "Champions"},
        {"n": "M. Liga de Campeones 2", "id": "CHAMPIONS2", "g": "Champions"},
        {"n": "M. Liga de Campeones 3", "id": "CHAMPIONS3", "g": "Champions"},
        {"n": "M. Liga de Campeones 4", "id": "CHAMPIONS4", "g": "Champions"},
        {"n": "M. Liga de Campeones 5", "id": "CHAMPIONS5", "g": "Champions"},
        {"n": "LaLiga Hypermotion", "id": "HYPERMOTION", "g": "Fútbol"},
        {"n": "Copa del Rey", "id": "COPA", "g": "Fútbol"},
        
        # --- MOTOR Y DEPORTES ---
        {"n": "DAZN F1", "id": "DAZNF1", "g": "Motor"},
        {"n": "DAZN 1", "id": "DAZN1", "g": "Deportes"},
        {"n": "DAZN 2", "id": "DAZN2", "g": "Deportes"},
        {"n": "M. Deportes", "id": "Deportes"},
        {"n": "Eurosport 1", "id": "EUROSPORT1", "g": "Deportes"},
        {"n": "Eurosport 2", "id": "EUROSPORT2", "g": "Deportes"},

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
        {"n": "Neox", "id": "NEOX", "g": "TDT"},
        {"n": "Nova", "id": "NOVA", "g": "TDT"},

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
        m3u += f'https://ver.movistarplus.es/apple/live/{c["id"]}/{c["id"]}.m3u8{ua}\n'
    
    return Response(m3u, mimetype='application/x-mpegurl')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
