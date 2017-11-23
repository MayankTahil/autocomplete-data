from python:2.7
RUN mkdir /app
COPY ./app /app
RUN apt-get update && \
		apt-get -y install python-mysqldb && \
		pip install MySQL-python && \
		apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 
WORKDIR /app
CMD python app.py