
<p align="center">

<a href="https://github.com/philippabele/pythonic-api-design/actions/workflows/pytest.yaml" target="_blank">
    <img src="https://github.com/philippabele/pythonic-api-design/workflows/Test/badge.svg" alt="Test">
</a>

<img src="https://img.shields.io/badge/Python-3.6%7C3.7%7C3.8%7C3.9-brightgreen" alt="Python">


</p>

# pythonic-api-design

## Docker:
First, please install Docker Desktop from this [LINK](https://docs.docker.com/desktop/#download-and-install).
### Build Docker containers:
`docker-compose up -d --build`

## Grafana

### Log-In
Visit Grafana's UI in your browser: `http://localhost:3000`.
The username is: `admin` and password: `GrafanaPW` by default. This can be changed in the file `config.monitoring`.

#### Open the explore tab
![img.png](03_grafana_monitoring/grafana_explore.png)

#### Choose Prometheus as the datasource
![img_1.png](03_grafana_monitoring/grafana_datasource.png)

#### Choose your metric
Then click `Use query`. A new Graph is created below with all your selected parameters.
![img_2.png](03_grafana_monitoring/grafana_metric.png)