import requests
import geocoder

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
    
    for place in results:
        print(place['name'])

if __name__ == "__main__":
    lat, lon = location()
    restaurants_nearby(lat, lon)