from flask import Flask, request, Response
import requests
import json
import re


app = Flask(__name__)

# API keys - you should replace these with your own
WEATHER_API_KEY = "22857147ffc79d0982bc8a00d8acd40b"  # OpenWeatherMap API key
ALPHAVANTAGE_API_KEY = "4MAQNE6AUSXC5B75"  # AlphaVantage API key for stocks


@app.route('/api', methods=['GET'])
def process_request():
    # Get query parameters
    airport_code = request.args.get('queryAirportTemp')
    stock_id = request.args.get('queryStockPrice')
    expression = request.args.get('queryEval')

    # Check that exactly one parameter is provided
    params_count = sum(1 for param in [airport_code, stock_id, expression] if param is not None)
    if params_count != 1:
        return Response("Error: Exactly one of the three parameters should be provided.", status=400)

    # Process airport temperature request
    if airport_code:
        if not re.match(r'^[A-Z]{3}$', airport_code):
            return Response("Error: Airport code should be exactly 3 uppercase letters.", status=400)
        return get_airport_temperature(airport_code.lower())

    # Process stock price request
    elif stock_id:
        if not re.match(r'^[A-Z]{1,4}$', stock_id):
            return Response("Error: Stock ID should be 1-4 uppercase letters.", status=400)
        return get_stock_price(stock_id)

    # Process expression evaluation
    elif expression:
        return evaluate_expression(expression)

    # This should never happen due to the earlier check
    return Response("Error: No valid parameter provided.", status=400)


def get_airport_temperature(iata_code):
    """Get the temperature for a given airport IATA code."""
    try:
        # First, get the airport location information
        airport_api_url = f"https://www.flightradar24.com/data/airports/{iata_code}/weather"
        airport_response = requests.get(airport_api_url)
        airport_data = airport_response.json()

        if not airport_data or 'status' in airport_data and airport_data['status'] == 'ERROR':
            return Response(json.dumps("Airport not found"), status=404, content_type="application/json")

        # Extract latitude and longitude
        latitude = airport_data['latitude']
        longitude = airport_data['longitude']

        # Now get the weather information using OpenWeatherMap
        weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={WEATHER_API_KEY}"
        weather_response = requests.get(weather_api_url)
        weather_data = weather_response.json()

        if weather_response.status_code != 200:
            return Response(json.dumps("Weather information not available"), status=503,
                            content_type="application/json")

        # Extract temperature in Celsius
        temperature = weather_data['main']['temp']

        # Return the temperature as JSON
        return Response(json.dumps(temperature), content_type="application/json")

    except Exception as e:
        return Response(json.dumps(f"Error: {str(e)}"), status=500, content_type="application/json")


def get_stock_price(stock_symbol):
    """Get the current price of a given stock symbol."""
    try:
        # Using Alpha Vantage API for stock prices
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={ALPHAVANTAGE_API_KEY}"
        response = requests.get(url)
        data = response.json()

        if "Global Quote" not in data or not data["Global Quote"]:
            return Response(json.dumps("Stock not found"), status=404, content_type="application/json")

        # Extract the current price
        price = float(data["Global Quote"]["05. price"])

        # Return the price as JSON
        return Response(json.dumps(price), content_type="application/json")

    except Exception as e:
        return Response(json.dumps(f"Error: {str(e)}"), status=500, content_type="application/json")


def evaluate_expression(expr):
    """Evaluate an arithmetic expression."""
    try:
        # Clean and validate the expression
        expr = expr.strip()

        # Simple validation to check if expression contains only allowed characters
        if not re.match(r'^[\d\s\+\-\*\/\(\)\.]+$', expr):
            return Response(json.dumps("Invalid expression"), status=400, content_type="application/json")

        # Evaluate the expression
        print(expr)
        result = eval(expr)

        # For the XML format response
        xml_result = f"<result>{result}</result>"

        # Determine which format to return based on Accept header
        accept_header = request.headers.get('Accept', '')

        if 'application/xml' in accept_header or 'text/xml' in accept_header:
            return Response(xml_result, content_type="application/xml")
        else:
            # Default to JSON
            return Response(json.dumps(result), content_type="application/json")

    except Exception as e:
        return Response(json.dumps(f"Error evaluating expression: {str(e)}"), status=400,
                        content_type="application/json")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)