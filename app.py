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
        {"n": "LaLiga Hypermotion", "g": "Fútbol", "id": "HYPERMOTION"},
        {"n": "Copa del Rey", "g": "Fútbol", "id": "COPA"},
        {"n": "M. LALIGA TV 2", "g": "Fútbol", "id": "LALIGA2"},
        {"n": "M. Liga de Campeones 2", "g": "Fútbol", "id": "CHAMPIONS2"},
        
        # --- DEPORTES Y MOTOR ---
        {"n": "DAZN F1", "g": "Motor", "id": "DAZNF1"},
        {"n": "DAZN 1", "g": "Deportes", "id": "DAZN1"},
        {"n": "DAZN 2", "g": "Deportes", "id": "DAZN2"},
        {"n": "Eurosport 1", "g": "Deportes", "id": "EUROSPORT1"},
        {"n": "Eurosport 2", "g": "Deportes", "id": "EUROSPORT2"},
        {"n": "Golf TV", "g": "Deportes", "id": "GOLF"},

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
        {"n": "Paramount", "g": "TDT", "id": "PARAMOUNT"},
        {"n": "GOL PLAY", "g": "TDT", "id": "GOL"},
        {"n": "Disney Channel", "g": "Infantil", "id": "DISNEY"},
        {"n": "Boing", "g": "Infantil", "id": "BOING"},
        {"n": "Clan", "g": "Infantil", "id": "CLAN"},

        # --- CINE Y SERIES ---
        {"n": "M. Estrenos", "g": "Cine", "id": "ESTRENOS"},
        {"n": "M. Estrenos 2", "g": "Cine", "id": "ESTRENOS2"},
        {"n": "M. Acción", "g": "Cine", "id": "ACCION"},
        {"n": "M. Comedia", "g": "Cine", "id": "COMEDIA"},
        {"n": "M. Drama", "g": "Cine", "id": "DRAMA"},
        {"n": "Warner TV", "g": "Series", "id": "WARNERTV"},
        {"n": "FOX", "g": "Series", "id": "FOX"},
        {"n": "AXN", "g": "Series", "id": "AXN"},
        {"n": "Calle 13", "g": "Series", "id": "CALLE13"},
        {"n": "SyFy", "g": "Series", "id": "SYFY"},

        # --- ADULTOS ---
        {"n": "Playboy TV", "g": "Adultos",
