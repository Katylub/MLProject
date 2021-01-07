# About this repository:
This repository contains the solutions for the **Machine Learning and Statistic** Project at GMIT.

This project contains a web service that uses Machine Learning to make predictions based on a Power Production data set. 

## Project
In summary you will see:<br>

	• A Jupyter notebook (train-model)[https://github.com/Katylub/MLProject/blob/master/train-model.ipynb] that trains a model using the data set. 

	• Python script (api.py)[https://github.com/Katylub/MLProject/blob/master/api.py] that runs a web service based on the model, as above.

	• Dockerfile to build and run the web service in a container.


## References
To create this program was necessary to use: 
1. Training Video and material provided during MAchine Learning and Statistic course at GMIT
2. Research 

## How to run the web service - Windows

FLASK
set FLASK_APP=rando.py
python -m flask run
 * Running on http://127.0.0.1:5000/

DOCKER
docker build . -t rando-image
docker run --name rando-container -d -p 5000:5000 rando-image