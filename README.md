# flask-prometheus

## Configuration

~~~
$ conda create -name flask-prometheus python=3.10
$ conda activate flask-prometheus
$ pip install -r requirements.txt
~~~

## Run using docker-compose

Ensure ".env" file exists and contains "SRC_PATH" variable
~~~
$ cd docker
$ docker-compose up
~~~

## Usage

### In browser

* http://localhost:5050/
* http://localhost:5050/greetings/johnwick
* http://localhost:5050/greetings/johnwick/json
* http://localhost:5050/metrics
* http://localhost:9090 - prometheus
* http://localhost:3000 - grafana

## References

* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [Loguru](https://github.com/Delgan/loguru)
* [Flask Prometheus Exporter](https://pypi.org/project/prometheus-flask-exporter/)