from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/playlist.m3u8")
def playlist():
    # Usamos la cabecera estándar de las listas que funcionan
    m3u = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/davidmuma/EPG_Movistar/master/guide.xml"\n'
    
    # Probamos con el User-Agent de Android TV, que es más permisivo que el de Apple
    ua = "|User-Agent=Mozilla/5.0 (Linux; Android 10; TV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36"
    
    canales = [
        # --- FÚTBOL TOTAL ---
        {"n": "M. LALIGA TV", "id": "LALIGA", "g": "Fútbol"},
        {"n": "DAZN LALIGA", "id": "DAZNLALIGA", "g": "Fútbol"},
        {"n": "M. Liga de Campeones", "id": "CHAMPIONS", "g": "Champions"},
        {"n": "M. Liga de Campeones 2", "id": "CHAMPIONS2", "g": "Champions"},
        {"n": "LaLiga Hypermotion", "id": "HYPERMOTION", "g": "Fútbol"},
        {"n": "Copa del Rey", "id": "COPA", "g": "Fútbol"},
        
        # --- MOTOR Y DEPORTES ---
        {"n": "DAZN F1", "id": "DAZNF1", "g": "Motor"},
        {"n": "DAZN 1", "id": "DAZN1", "g": "Deportes"},
        {"n": "DAZN 2", "id": "DAZN2", "g": "Deportes"},
        {"n": "Eurosport 1", "id": "EUROSPORT1", "g": "Deportes"},
        {"n": "M. Deportes", "id": "DEPORTES", "g": "Deportes"},

        # --- TDT ESPAÑA ---
        {"n": "La 1", "id": "TVE", "g": "TDT"},
        {"n": "La 2", "id": "TVE2", "g": "TDT"},
        {"n": "Antena 3", "id": "ANTENA3", "g": "TDT"},
        {"n": "Cuatro", "id": "CUATRO", "g": "TDT"},
        {"n": "Telecinco", "id": "TELECINCO", "g": "TDT"},
        {"n": "La Sexta", "id": "LASEXTA", "g": "TDT"},
        {"n": "FDF", "id": "FDF", "g": "TDT"},
        {"n": "Mega", "id": "MEGA", "g": "TDT"},

        # --- CINE Y ADULTOS ---
        {"n": "M. Estrenos", "id": "ESTRENOS", "g": "Cine"},
        {"n": "M. Acción", "id": "ACCION", "g": "Cine"},
        {"n": "Playboy TV", "id": "PLAYBOY", "g": "Adultos"},
        {"n": "Vivid Red", "id": "VIVIDRED", "g": "Adultos"}
    ]
    
    for c in canales:
        m3u += f'#EXTINF:-1 tvg-id="{c["id"]}" group-title="{c["g"]}", {c["n"]}\n'
        # Enlace directo para que la tele no pase por Render al reproducir
        m3u += f'https://ver.movistarplus.es/apple/live/{c["id"]}/{c["id"]}.m3u8{ua}\n'
    
    return Response(m3u, mimetype='application/x-mpegurl')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
