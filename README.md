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

docker run -it --rm --network myinvestor-manager_dev_network --link db:postgres postgres psql -h postgres -d myinvestordb  -U myinvestor

```

## References

* [Debugging a Python Flask app in Docker Compose](https://github.com/trstringer/python-flask-docker-compose-debugging)