#!/bin/bash

mkdir tempdir2

cp CropDatabase.sqlite tempdir2/.
cp crop_api_server.py tempdir2/.

echo "FROM python" >> tempdir2/Dockerfile
echo "RUN pip install flask" >> tempdir2/Dockerfile
echo "RUN pip install Flask-SQLAlchemy" >> tempdir2/Dockerfile
echo "RUN pip install Flask-Marshmallow" >> tempdir2/Dockerfile
echo "RUN pip install marshmallow-sqlalchemy" >> tempdir2/Dockerfile
echo "RUN pip install Flask-Login" >> tempdir2/Dockerfile
echo "COPY crop_api_server.py /home/myapp" >> tempdir2/Dockerfile
echo "COPY CropDatabase.sqlite /home/myapp" >> tempdir2/Dockerfile

echo "EXPOSE 5000" >> tempdir2/Dockerfile
echo "CMD python3 /home/myapp/crop_api_server.py" >> tempdir2/Dockerfile

cd tempdir2
docker build -t cr_web_server .

docker run -t -d -p 5000:5000 --name cr_web_server_running cr_web_server

docker ps -a