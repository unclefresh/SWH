# Solve World Hunger (SWH) Project

## Overview
This project is designed to simulate solving world hunger by feeding a random number of people each time a page is reloaded. It uses Docker to deploy various services, including a Flask app, Prometheus for monitoring, and Grafana for visualizing the data. 

## Requirements
- Docker (installed locally)

## Setup and Running Locally

### 1. Clone the Git Repository
First, clone the repository to your local machine:

```
git clone https://github.com/unclefresh/SWH
cd SWH
```

### 2. Add the .env file to your project directory
You should have received a securely sent .env file. Place this .env file in the root directory of the project (same directory as docker-compose.yml). This file contains sensitive environment variables required for the application.

### 3. Start the Services Using Docker
Once Docker is installed and the .env file is in place, run the following command in your terminal to build and start the containers:

```
docker-compose up --build -d
```

This will:

* Build the necessary Docker images.
* Start the services defined in the docker-compose.yml file in detached mode (-d).

### 4. Access the Application Locally
#### Health Check
To verify that everything is running correctly, navigate to the following URL:

* localhost:8000/health
This should return "I'm healthy".

#### Solve World Hunger with the click of a button!
To simulate feeding people and see the number of people fed (which is randomly incremented), navigate to:

* localhost:8000/solve_world_hunger
This page will display a random number of people fed between 10 and 10000. The number will change each time the page is reloaded.

#### Metrics
To view metrics, including the gauge for the number of people fed and the feed event counter, go to:

* localhost:8000/metrics
This page will show Prometheus-compatible metrics. Verify the number of times a feed event was created. (the number of times you refreshed the /solve_world_hunger endpoint)

You can also check the total number of people fed from all events you created.

#### Prometheus
To view Prometheus and confirm that it is scraping data from the /metrics endpoint, visit:

* localhost:9090
You should see the Prometheus interface, where you can query and confirm that it is scraping data from the Flask app’s /metrics endpoint.

#### Grafana
To log into Grafana and view the dashboards, navigate to:

* localhost:3000
You should automatically be logged in with the username and password stored in the .env file that was referenced by the docker-compose file.

This will give you access to the Grafana dashboard, where you can visualize the metrics being scraped by Prometheus. (need to update when applying AWS)

### 5. Stopping the Services
When you’re done, you can stop the services with:

```
docker-compose down
```

### Troubleshooting
* If Docker is not working properly: Ensure Docker is running and that you're using the correct version. Run the following to check:
```
docker --version
```
* If you cannot access the services: Check if Docker is running correctly using the command below to list running containers.
```
docker ps
```
* Ensure no other applications are using ports 8000, 9090, or 3000 on your machine.

### Contributing
Feel free to open issues or create pull requests to contribute to this project.

### License
This project is licensed under the MIT License.
