from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/result', methods=['POST'])
def result():
    city = request.form['city']
    if not len(city) > 0:
        city = "Niš"
    url = "http://api.weatherstack.com/current/?access_key=de6a7ea4c895493e82b7e597ab0ed72a&query=" + city
    r = requests.get(url)
    json_obj = r.json()
    if 'location' not in json_obj:
        return "There is no such location!"
    country = str(json_obj['location']['country'])
    region = str(json_obj['location']['region'])
    localtime = str(json_obj['location']['localtime'])
    last_updated = str(json_obj['current']['last_updated'])
    temp = str(json_obj['current']['temp_c'])
    pa = str(json_obj['current']['pressure_mb'])
    wind_kph = str(json_obj['current']['wind_kph'])
    wind_dir = str(json_obj['current']['wind_dir'])
    wind_deg = str(json_obj['current']['wind_degree'])
    hum = str(json_obj['current']['humidity'])
    vis_km = str(json_obj['current']['vis_km'])
    precip_mm = str(json_obj['current']['precip_mm'])
    icon = str(json_obj['current']['condition']['icon'])
    return render_template('result.html',
                           city=city, country=country, region=region, localtime=localtime,
                           temp=temp, pa=pa, vis_km=vis_km,
                           wind_kph=wind_kph, wind_dir=wind_dir, wind_deg=wind_deg,
                           hum=hum, precip_mm=precip_mm, last_updated=last_updated, icon=icon)

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
