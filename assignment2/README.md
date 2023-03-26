# README
## Assignment 2

### The required python version for assignment1 is python=3.11.

#### A `requirements.txt` file is in the assignment1 folder that contains all of the necessary modules to install

### Flask webserver
To start the Flask webserver, run the following code block in the terminal: `python flask_webserver.py`  

Next, access the webpage by putting <http://127.0.0.1:5000> in your browser.  
  
### Dockerizing the application
First, build the Docker image by running the command in the terminal: `docker build -t <image_name> .`
Next, run the Docker container by entering this command in the terminal: `docker run --rm -dp 5000:5000 <image_name>`
