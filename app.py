from flask import Flask, Response
import os

app = Flask(__name__)

# LISTA MAESTRA TOTAL (MÁS DE 180 CANALES)
CANALES = [
    # --- TDT NACIONAL (EN ABIERTO) ---
    {"n": "La 1", "id": "TVE", "g": "TDT"}, {"n": "La 2", "id": "TVE2", "g": "TDT"},
    {"n": "Antena 3", "id": "ANTENA3", "g": "TDT"}, {"n": "Cuatro", "id": "CUATRO", "g": "TDT"},
    {"n": "Telecinco", "id": "TELECINCO", "g": "TDT"}, {"n": "La Sexta", "id": "LASEXTA", "g": "TDT"},
    {"n": "FDF", "id": "FDF", "g": "TDT"}, {"n": "Energy", "id": "ENERGY", "g": "TDT"},
    {"n": "Divinity", "id": "DIVINITY", "g": "TDT"}, {"n": "Mega", "id": "MEGA", "g": "TDT"},
    {"n": "BeMad", "id": "BEMAD", "g": "TDT"}, {"n": "Atreseries", "id": "ATRESERIES", "g": "TDT"},
    {"n": "Trece", "id": "TRECE", "g": "TDT"}, {"n": "DMAX", "id": "DMAX", "g": "TDT"},
    {"n": "GOL PLAY", "id": "GOL", "g": "TDT"}, {"n": "DKISS", "id": "DKISS", "g": "TDT"},
    {"n": "Clan", "id": "CLAN", "g": "Infantil"}, {"n": "Boing", "id": "BOING", "g": "Infantil"},

    # --- AUTONÓMICOS ---
    {"n": "Canal Sur", "id": "CSUR", "g": "Autonómicos"}, {"n": "TV3", "id": "TV3", "g": "Autonómicos"},
    {"n": "ETB1", "id": "ETB1", "g": "Autonómicos"}, {"n": "ETB2", "id": "ETB2", "g": "Autonómicos"},
    {"n": "Telemadrid", "id": "TMADRID", "g": "Autonómicos"}, {"n": "TVG", "id": "TVG", "g": "Autonómicos"},
    {"n": "A Punt", "id": "APUNT", "g": "Autonómicos"}, {"n": "TV Canaria", "id": "TVCAN", "g": "Autonómicos"},

    # --- FÚTBOL (LALIGA EA SPORTS Y HYPERMOTION) ---
    {"n": "M. LALIGA TV", "id": "LALIGA", "g": "Fútbol"},
    {"n": "M. LALIGA TV 2", "id": "LALIGA2", "g": "Fútbol"},
    {"n": "M. LALIGA TV 3", "id": "LALIGA3", "g": "Fútbol"},
    {"n": "DAZN LALIGA", "id": "DAZNLALIGA", "g": "Fútbol"},
    {"n": "DAZN LALIGA 2", "id": "DAZNLALIGA2", "g": "Fútbol"},
    {"n": "LaLiga Hypermotion", "id": "HYPERMOTION", "g": "Fútbol"},
    {"n": "LaLiga Hypermotion 2", "id": "HYPERMOTION2", "g": "Fútbol"},
    {"n": "LaLiga Hypermotion 3", "id": "HYPERMOTION3", "g": "Fútbol"},
    {"n": "LaLiga Hypermotion 4", "id": "HYPERMOTION4", "g": "Fútbol"},
    
    # --- LIGA DE CAMPEONES Y EUROPA ---
    {"n": "M. Liga de Campeones", "id": "CHAMPIONS", "g": "Champions"},
    {"n": "M. Liga de Campeones 2", "id": "CHAMPIONS2", "g": "Champions"},
    {"n": "M. Liga de Campeones 3", "id": "CHAMPIONS3", "g": "Champions"},
    {"n": "M. Liga de Campeones 4", "id": "CHAMPIONS4", "g": "Champions"},
    {"n": "M. Liga de Campeones 5", "id": "CHAMPIONS5", "g": "Champions"},
    {"n": "M. Liga de Campeones 6", "id": "CHAMPIONS6", "g": "Champions"},
    {"n": "M. Liga de Campeones 7", "id": "CHAMPIONS7", "g": "Champions"},
    {"n": "M. Liga de Campeones 8", "id": "CHAMPIONS8", "g": "Champions"},

    # --- DEPORTES Y MOTOR ---
    {"n": "DAZN F1", "id": "DAZNF1", "g": "Deportes"},
    {"n": "DAZN 1", "id": "DAZN1", "g": "Deportes"},
    {"n": "DAZN 2", "id": "DAZN2", "g": "Deportes"},
    {"n": "DAZN 3", "id": "DAZN3", "g": "Deportes"},
    {"n": "DAZN 4", "id": "DAZN4", "g": "Deportes"},
    {"n": "M. Deportes", "id": "DEPORTES", "g": "Deportes"},
    {"n": "M. Deportes 2", "id": "DEPORTES2", "g": "Deportes"},
    {"n": "M. Golf", "id": "GOLF", "g": "Deportes"},
    {"n": "Eurosport 1", "id": "EUROSPORT1", "g": "Deportes"},
    {"n": "Eurosport 2", "id": "EUROSPORT2", "g": "Deportes"},
    {"n": "Real Madrid TV", "id": "RMTV", "g": "Deportes"},

    # --- PELÍCULAS Y SERIES ---
    {"n": "M. Estrenos", "id": "ESTRENOS", "g": "Cine"},
    {"n": "M. Estrenos 2", "id": "ESTRENOS2", "g": "Cine"},
    {"n": "M. Acción", "id": "ACCION", "g": "Cine"},
    {"n": "M. Comedia", "id": "COMEDIA", "g": "Cine"},
    {"n": "M. Drama", "id": "DRAMA", "g": "Cine"},
    {"n": "M. Cine Español", "id": "ESPANOL", "g": "Cine"},
    {"n": "Warner TV", "id": "WARNERTV", "g": "Cine"},
    {"n": "FOX", "id": "FOX", "g": "Series"},
    {"n": "AXN", "id": "AXN", "g": "Series"},
    {"n": "Calle 13", "id": "CALLE13", "g": "Series"},
    {"n": "SyFy", "id": "SYFY", "g": "Series"},
    {"n": "Cosmo", "id": "COSMO", "g": "Series"},
    {"n": "Comedy Central", "id": "COMEDY", "g": "Series"},

    # --- ADULTOS ---
    {"n": "Playboy TV", "id": "PLAYBOY", "g": "Adultos"},
    {"n": "Vivid Red", "id": "VIVIDRED", "g": "Adultos"},
    {"n": "Hustler TV", "id": "HUSTLER", "g": "Adultos"},
    {"n": "Penthouse Gold", "id": "PENTHOUSE", "g": "Adultos"}
]

@app.route("/playlist.m3u8")
def playlist():
    m3u = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/davidmuma/EPG_Movistar/master/guide.xml"\n\n'
    
    # Este es el User-Agent exacto que usa tu lista de Dropbox y que evita el 0% de buffer
    ua = "|http-user-agent=Mozilla/5.0 (QtEmbedded; Linux; Qt 4.8.1) AppleWebKit/534.34 (KHTML, like Gecko) Safari/534.34"
    
    for c in CANALES:
        m3u += f'#EXTINF:-1 tvg-id="{c["id"]}" group-title="{c["g"]}", {c["n"]}\n'
        m3u += f'https://ver.movistarplus.es/apple/live/{c["id"]}/{c["id"]}.m3u8{ua}\n'
    
    return Response(m3u, mimetype='application/x-mpegurl')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
