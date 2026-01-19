from flask import Flask, Response, request
import requests
import os

app = Flask(__name__)

# User-Agent maestro para engañar a la plataforma
HEADERS = {"User-Agent": "AppleTV6,2/18L203"}

@app.route("/playlist.m3u8")
def playlist():
    base_url = request.host_url.rstrip('/')
    # Lista extendida con los canales solicitados
    canales = [
        # --- FÚTBOL Y DEPORTES ---
        {"n": "M. LALIGA TV", "g": "Fútbol", "id": "LALIGA"},
        {"n": "DAZN LALIGA", "g": "Fútbol", "id": "DAZNLALIGA"},
        {"n": "M. Liga de Campeones", "g": "Fútbol", "id": "CHAMPIONS"},
        {"n": "LaLiga Hypermotion", "g": "Fútbol", "id": "HYPERMOTION"},
        {"n": "Copa del Rey", "g": "Fútbol", "id": "COPA"},
        {"n": "DAZN F1", "g": "Motor", "id": "DAZNF1"},
        {"n": "Eurosport 1", "g": "Deportes", "id": "EUROSPORT1"},
        {"n": "Eurosport 2", "g": "Deportes", "id": "EUROSPORT2"},
        
        # --- TDT ESPAÑA COMPLETO ---
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
        {"n": "Trece", "g": "TDT", "id": "TRECE"},
        {"n": "DMAX", "g": "TDT", "id": "DMAX"},
        {"n": "Paramount Network", "g": "TDT", "id": "PARAMOUNT"},
        {"n": "Disney Channel", "g": "Infantil", "id": "DISNEY"},
        {"n": "Boing", "g": "Infantil", "id": "BOING"},
        {"n": "Clan", "g": "Infantil", "id": "CLAN"},
        
        # --- CINE Y SERIES ---
        {"n": "M. Estrenos", "g": "Cine", "id": "ESTRENOS"},
        {"n": "M. Acción", "g": "Cine", "id": "ACCION"},
        {"n": "M. Comedia", "g": "Cine", "id": "COMEDIA"},
        {"n": "M. Drama", "g": "Cine", "id": "DRAMA"},
        {"n": "Warner TV", "g": "Series", "id": "WARNERTV"},
        {"n": "FOX", "g": "Series", "id": "FOX"},
        {"n": "AXN", "g": "Series", "id": "AXN"},
        {"n": "Calle 13", "g": "Series", "id": "CALLE13"},
        
        # --- ADULTOS ---
        {"n": "Playboy TV", "g": "Adultos", "id": "PLAYBOY"},
        {"n": "Vivid Red", "g": "Adultos", "id": "VIVIDRED"},
        {"n": "Hustler TV", "g": "Adultos", "id": "HUSTLER"}
    ]
    
    m3u = "#EXTM3U\n"
    for c in canales:
        m3u += f'#EXTINF:-1 group-title="{c["g"]}", {c["n"]}\n'
        m3u += f'{base_url}/canal/{c["id"]}.m3u8\n'
    return Response(m3u, mimetype='application/x-mpegurl')

@app.route("/canal/<id>.m3u8")
def proxy_canal(id):
    url = f"https://ver.movistarplus.es/apple/live/{id}/{id}.m3u8"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        # Devolvemos el contenido con el tipo de archivo correcto para la tele
        return Response(r.content, mimetype='application/vnd.apple.mpegurl')
    except:
        return "Error de conexión", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
