# ride-math

> Home-to-work, work-to-home Uber fare graph

Know the *optimal* time to leave your house and office based on Uber fares

## TODO

* Dockerize `uber.py`, setup a cron job inside that runs every 2 minutes
* Create `server.py` to serve data and frontend
* Create frontend to graph data - with [Chart.js](http://www.chartjs.org/)
* `docker-compose` setup: app linked to mongodb
* Supply dynamic values through env vars with `docker-compose`

## Notes

`docker run --name uber-ds -P 27017:27017 -d mongo`

> Ben Sarmiento 2016+
