# Flask

## Synopsis
Run Flask and get weather information from openweathermap.

## Description
The point of this project is to get weather information from openweathermap.  
You could run this in Python directly or create a Docker image and run it without thinking about Python.

### Run with Python
* First you need to create a `.env` file which has the key `API_KEY` and the value should be your own api key from openweathermap.  
    * If you don't want to create a `.env` file you could just set a local environment variable with the key/value as above.
* After that is done you need to create your `.venv`, activate it and install everything in the requirements file.
* Now run the `main.py` file which is located in the `src` directory.

### Run with Docker
* The first part of running this with Python is applied to the Docker section as well so create the file and input your `API_KEY`.
* After that is done you just need to build the image.

## Parameter
If you are running this as a Docker image you need these parameters.
```
-p <LOCAL PORT>:8000
```
If you decide not to include the `.env` file you need to use the `-e` flag as well to set the environment variable within the container.