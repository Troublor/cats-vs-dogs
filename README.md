# Dogs VS. Cat Classification

A demo image classifier trained with convolutional neural network to classify dogs and cats images. 
The classifier can be deployed as a RESTful service in docker.  

Source code of this docker image is located on Github: [https://github.com/Troublor/cats-vs-dogs](https://github.com/Troublor/cats-vs-dogs)
The docker image has been published at [Docker Hub](https://hub.docker.com/repository/docker/troublor/cats-vs-dogs).

## Dependency

- python: `3.8`

Python package dependencies are defined in `requirements.txt`. 
```bash
pip3 install -r requirements.txt
```

## Model Training

### Training Dataset

We use the `Dogs vs. Cats` dataset on Kaggle: [https://www.kaggle.com/c/dogs-vs-cats/data](https://www.kaggle.com/c/dogs-vs-cats/data) for training.
The data need to be preprocessed to separate cats images from dog images. 
The expected folder structure should be: 
```bash
data
└── large_set
    ├── cat
    │   ├── cat0.jpg
    │   ├── cat1.jpg
    │   ...
    └── dog
        ├── cat0.jpg
        ├── cat1.jpg
        ...
```
You may need to manually download the data from Kaggle and separate the images with a script. 

### Training Script

The python script to train a CNN model is in `train.ipynb`.
It should be executed in the [Jupyter Notebook](https://jupyter.org/) and the script will leverage GPU (if it is available, otherwise CPU) to train a model.
After training, the model will be saved to `model/classifier.h5`.

Note that the model is not finely tuned, so the classification accuracy may not be satisfactory.

## RESTful API

We use python [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework to build a simple RESTful API for the use of the image classifier.
The Flask app can be found in `app.py`, which will load the trained model at `model/classifier.h5` and expose an API at `http://0.0.0.0:5000/classify`.

### Usage

Start RESTful API service:
```bash
python3 -m flask run --host=0.0.0.0
```

Call the RESTful API: 
- Http POST method
- Url: `http://localhost:5000/classify`
- Form-data: image - upload the image to classify

## Service in Docker

Install docker with official [documentation](https://docs.docker.com/get-docker/).
This section requires that the model has already been trained and saved at `model/classifier.h5`.

### Build Docker Image

```bash
docker build -t troublor/cats-vs-dogs:latest .
```
The docker image has been published at [Docker Hub](https://hub.docker.com/repository/docker/troublor/cats-vs-dogs).
You can directly run the container by pulling from docker hub.

### Run Docker Container

```bash
docker run -p 5000:5000 --name cats-vs-dogs troublor/cats-vs-dogs:latest
```
This command will create a container based on the docker image built previously and forward port `5000` in container to host machine.

### Stop and Remove Container

See docker [documentation](https://docs.docker.com/engine/reference/commandline/rm/).