FROM python:3.8

# install python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy the app
COPY src .
