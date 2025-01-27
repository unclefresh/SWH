from flask import Flask, jsonify, Response
from prometheus_client import start_http_server, Gauge, Counter
import random

# Initialize Flask app
app = Flask(__name__)

# Create a counter to track the number of times the feed event occurs
feed_event_counter = Counter('feed_event_counter', 'Number of times the /solve_world_hunger endpoint is hit')

# Create a gauge to track the total number of people impacted over time
people_impacted_gauge = Gauge('people_impacted', 'Total number of people impacted over time')

# Health check endpoint
@app.route('/health')
def health():
    return "I'm healthy", 200

# Solve Hunger endpoint
@app.route('/solve_world_hunger')
def solve_world_hunger():
    # Increment feed event counter each time the endpoint is hit
    feed_event_counter.inc()

    # Generate random number between 10 and 10,000 for people fed
    people_fed = random.randint(10, 10000)

    # Update total number of people impacted
    people_impacted_gauge.inc(people_fed)

    return jsonify({'status': 'Number of people fed worldwide (allegedly)', 'people_fed': people_fed}), 200

@app.route("/metrics")
def metrics():
    from prometheus_client import generate_latest
    # Return metrics with content type 'text/plain'
    return Response(generate_latest(), mimetype='text/plain')

# Start the server
if __name__ == '__main__':
    # Start http server for Prometheus metrics on port 8000
    start_http_server(8000)
    app.run(debug=True, host='0.0.0.0', port=8000)

