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

*Build the necessary Docker images.
*Start the services defined in the docker-compose.yml file in detached mode (-d).
