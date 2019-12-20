# Standard Library
import os
# Additional Modules
from flask import Flask, Markup, render_template, request, url_for
# Project Files
from data_fetcher import DataFetcher
from data_plotter import DataPlotter

ASSET_ID = 'write_the_asset_id_here'
ASPECT = 'write_the_name_of_the_aspect_here'

app = Flask(__name__)

# Use the environment varible 'PORT' or port 5000.
port = int(os.getenv('PORT', 5000))

@app.route('/')
@app.route('/pressure')
def pressure():
    # Extract the token from a request to the backend.
    auth_token = request.headers.get('Authorization')
    # Fetch the time series data from the IoT Time Series Service.
    data = DataFetcher(auth_token, ASSET_ID, ASPECT).fetch_data('pressure')
    # Create the line chart.
    chart = DataPlotter().plot_line_chart(data[0], data[1], 'Air Pressure')
    # Render the web page template.
    return render_template('pressure.html', line_chart=Markup(chart))

@app.route('/temperature')
def temperature():
    auth_token = request.headers.get('Authorization')
    data = DataFetcher(auth_token, ASSET_ID, ASPECT).fetch_data('temperature')
    chart = DataPlotter().plot_line_chart(data[0], data[1], 'Temperature')
    return render_template('temperature.html', line_chart=Markup(chart))

if __name__ == '__main__':
    # Make the server externally visible.
    app.run(host='0.0.0.0', port=port)
