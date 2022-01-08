#!/bin/bash

mkdir tempdir
mkdir tempdir/crop_app

cp -r crop_app/* tempdir/crop_app/.
cp run.py tempdir/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask-WTF" >> tempdir/Dockerfile
echo "RUN pip install Flask-Login" >> tempdir/Dockerfile
echo "RUN pip install Flask-Bcrypt" >> tempdir/Dockerfile
echo "RUN pip install pillow" >> tempdir/Dockerfile
echo "RUN pip install requests" >> tempdir/Dockerfile
echo "RUN pip install email_validator" >> tempdir/Dockerfile
echo "COPY ./crop_app /home/myapp/crop_app" >> tempdir/Dockerfile
echo "COPY run.py /home/myapp" >> tempdir/Dockerfile

echo "EXPOSE 7070" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/run.py" >> tempdir/Dockerfile

cd tempdir
docker build -t cr_web_app .

docker run -t -d -p 7070:7070 --name cr_web_app_running cr_web_app

docker ps -a