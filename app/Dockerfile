# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.12-alpine
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
