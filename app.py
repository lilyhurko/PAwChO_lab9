import os
import logging
import requests
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Ustawienia API WeatherAPI (zarejestruj się i zdobądź klucz API)
API_KEY = 'aa64086cd4084fc09e3101543253004'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

# Lista krajów i miast (przykładowa)
countries_and_cities = {
    'Polska': ['Warszawa', 'Kraków', 'Gdańsk'],
    'USA': ['Nowy Jork', 'Los Angeles', 'Chicago'],
    'Ukraina': ['Kyiv', 'Rivne', 'Lwów'],
}

# Ustawienia logowania
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Imię i nazwisko autora
author_name = "Lilia Hurko" 

@app.route('/')
def index():
    # Zapisanie daty uruchomienia aplikacji w logach
    logging.info(f'Aplikacja uruchomiona: {datetime.now()}')
    logging.info(f'Autor aplikacji: {author_name}')
    logging.info(f'Aplikacja nasłuchuje na porcie TCP: 5000')  
    return render_template('index.html', countries_and_cities=countries_and_cities)

@app.route('/weather', methods=['POST'])
def weather():
    # Pobranie wybranego kraju i miasta
    country = request.form['country']
    city = request.form['city']

    # Logowanie wybranego kraju i miasta
    logging.info('Wybrano kraj: %s, miasto: %s', country, city)

    # Pobranie danych o pogodzie z WeatherAPI
    params = {
        'key': API_KEY,
        'q': f'{city},{country}',
        'lang': 'pl'  
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        weather_data = response.json()
        weather_description = weather_data['current']['condition']['text']
        temperature = weather_data['current']['temp_c']
        humidity = weather_data['current']['humidity']
        return render_template('weather.html', city=city, country=country,
                               weather_description=weather_description,
                               temperature=temperature, humidity=humidity)
    else:
        return "Błąd pobierania danych pogodowych. Spróbuj ponownie później."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
