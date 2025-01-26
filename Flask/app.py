from flask import Flask, jsonify
from prometheus_client import start_http_server, Gauge, Counter
import random

# Initialize Flask app
app = Flask(__name__)

# Create a metric to track hunger solutions (Gauge)
hunger_metric = Gauge('solve_world_hunger', 'A metric to track world hunger solutions')

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
    # Increment the feed event counter each time the endpoint is hit
    feed_event_counter.inc()

    # Generate a random number between 10 and 1,000,000 for people fed
    people_fed = random.randint(10, 1000000)

    # Update the hunger metric with the number of people fed
    hunger_metric.set(people_fed)

    # Update the total number of people impacted (this keeps a cumulative count)
    people_impacted_gauge.inc(people_fed)

    # Return the result in JSON
    return jsonify({'status': 'Number of people fed worldwide (allegedly)', 'people_fed': people_fed}), 200

# Start the server
if __name__ == '__main__':
    # Start Prometheus metrics server on port 8002
    start_http_server(8002)

    app.run(debug=True, host='0.0.0.0', port=8000)

