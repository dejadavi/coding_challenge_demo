FROM python:3.7-slim-buster
WORKDIR /
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN "/app/run_tests.sh" 
CMD [  "/app/entrypoint.sh" ]