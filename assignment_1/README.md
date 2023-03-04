# README
## Assignment 1

### The required python version for assignment1 is python=3.11.

### A `requirements.txt` file is in the assignment1 folder that contains all of the necessary modules to install
> NOTE: There are more modules listed in the `requirements.tx`t file than are necessary-- all of the modules from the environment are listed because I used `pip freeze` rather than just the assignment1 project modules being listed.

### RESTful API
To start the RESTFul API, run the following code block in the terminal: `python RESTful_API.py`  

Next, open a new terminal window and run: `curl http://127.0.0.1:5000/api`  

This will return the output of the `get` method from `RESTful_API.py`, and the output should be: `{"NER task": "Takes a .txt file with as input and returns the corresponding NER information
."}`  

You should also be able to run: `curl -H "Content-Type: text/plain" -X POST -d@input.txt http://127.0.0.1:5000/api` in the second terminal opened  

This will return the output of the `post` method which should be: `{"entities": [[5, 20, "PERSON", "Sebastian Thrun"], [61, 67, "ORG", "Google"], [71, 75, "DATE", "2007"], [173, 181, "NORP", "American"], [271, 276, "PERSON", "Thrun"], [299, 305, "ORG", "
Recode"], [306, 323, "DATE", "earlier this week"]]}`  
  
### Flask webserver
To start the Flask webserver, run the following code block in the terminal: `python Flask_webserver.py`  

Then, you can type your text in the box that you wish to tag with named entities and click "Get Entities" button.  

This pulls up the named entity recognition results page using the `ner.py` `get_entities_with_markup` function.

### Streamlit application

To run the streamlit application, run the following code block in the terminal: `streamlit run streamlit_app.py`.  

This will pull up the streamlit page where you can enter your text to be tagged with named entities and click the "Get Entitites" button when done.  

Then, you will see the outputted named entity recognition results page.  

This page is unique because it has not only color coded the marked-up entities, it has also color coded the side-bar entities as well as the bar graph.  

Additionally, I have added corresponding emojis to the top of each entity bar in the bar graph. These emojis are mapped to entity labels using the `color_map.json` file I created.


