FROM alpine:3.19

# install python3 and pip3 on alpine
RUN apk add --no-cache python3 py3-pip

# install python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt