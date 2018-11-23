# myInvestor-manager

## Overview

Application for stock portfolio management, analysis and prediction.

## Prerequisites

* python 3
* Docker

## Development

Start the docker instances

```bash

docker-compose up --build -d

```

Connect to postgresql instance

```bash

docker run -it --rm --network dev_network postgres psql -h postgres -U postgres


```


## References

* [Debugging a Python Flask app in Docker Compose](https://github.com/trstringer/python-flask-docker-compose-debugging)