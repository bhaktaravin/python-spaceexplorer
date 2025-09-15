# python-spaceexplorer
# My Streamlit App (Docker Desktop)

This is a Streamlit app packaged with Docker, ready to run on Docker Desktop.  
It uses a `.env` file for configurable settings like the port number.

---

## Quick Start (3 Commands)

1. **Clone the repository**

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

2. **Create .env file (optional, for custom port)**
PORT=8501

3. ** Run the app**
docker-compose up


open your browser at http://localhost:<PORT>(default 8501)

Prerequisites

Docker Desktop ->  installed and running
Docker Compose -> comes with Docker Desktop

Setup Details
Option 1: Run with Docker Compose (Recommended)
docker-compose up

Docker builds the image (first time) and starts the container.

Streamlit available at http://localhost:<PORT> (default 8501).

To stop:

docker-compose down

Option 2: Build and run manually

1. Build the image
docker build -t my-streamlit-app .

2. Run with Port Mapping
docker run -p 8501:8501 my-streamlit-app
    With Custom Port
    docker run -p 8080:8501 my-streamlit-app
    Open browser at http://localhost:8080


3. Stop the Container 
docker ps
docker stop <container_id>
