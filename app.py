import requests, geocoder
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def location():
    g = geocoder.ip('me')
    return g.latlng 

def restaurants_nearby(latitude, longitude, radius=100, api_key='API key'):
    endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': f"{latitude},{longitude}",
        'radius': radius,
        'type': 'restaurant',
        'key': api_key
    }
    
    response = requests.get(endpoint_url, params=params)
    results = response.json().get('results', [])
    
    return [place['name'] for place in results]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        radius = request.form.get('radius')
        lat, lon = location()
        restaurants = restaurants_nearby(lat, lon, radius)
        return render_template('results.html', restaurants=restaurants)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

