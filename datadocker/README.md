# DataDocker

__DataDocker__ is a (docker image)[link here] with a collections of packages to have a ready environment with a lot of stuff.

Based on Ubuntu Xenial

## Command to build the IMAGE
__./build_data_docker.sh__ $PYTHON_VERSION

* $PYTHON_VERSION is the PYTHON_VERSION of your image, must must 2 or 3

## Command to run the CONTAINER
__./run_data_docker.sh__ $LOCAL_FOLDER_NAME $PYTHON_VERSION

* $LOCAL_FOLDER_NAME is the path to the directory that you want to mount with "/home/datadocker" inside your container
* $PYTHON_VERSION, as above

You can see the running container with
* sudo docker ps

and stop the container with
* sudo docker stop CONTAINER_ID

**Main and only requirement:**

* [__docker__](https://docs.docker.com/engine/installation/)

## About running the CONTAINER

The command inside inside run_data_docker.sh is:

docker run -d __-p 127.0.0.1:8888:8888__ -v $FOLDER:/home/datadocker datadocker_python_$PYTHON

The bold part means that the port 8888 of the container is bound with your localhost:8888 and you can access the jupyter notebook only from your computer.


If for any reason you want to make the container available also to other computers inside your network you just need to remove the ip from the command:

docker run -d __-p 8888:8888__ -v $FOLDER:/home/datadocker datadocker_python_$PYTHON

__Remember that if your network is _internet_ everyone can access your jupyter notebook__

[List of the Python libraries](https://github.com/barrachri/datadocker/blob/master/packages/requirements/requirements.txt)

[List image libraries](https://github.com/barrachri/datadocker/blob/master/packages/image-packages.txt)

[List R libraries](https://github.com/barrachri/datadocker/blob/master/dockerfile_dir/python_3/Dockerfile#L48)
