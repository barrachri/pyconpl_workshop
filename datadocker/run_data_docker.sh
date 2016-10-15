#! /bin/bash

FOLDER=$1
PYTHON=$2

if [ -z "$FOLDER" ]
  then
    echo "No argument supplied for as a local folder for docker, you need to specify a local dir";
    exit 128;
fi

if [ -z "$PYTHON" ]
  then
    echo "No argument supplied for python version, please indicate 2 or 3";
    exit 128;
fi

if (($PYTHON==2 || $PYTHON==3))
then
	docker run -d -p 127.0.0.1:8888:8888 -v $FOLDER:/home/datadocker datadocker_python_$PYTHON
else
	echo "The argument supplied should be a valid Python version, 2 or 3";
  exit 128;
fi
