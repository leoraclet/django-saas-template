# Pull official base image
FROM grafana/grafana:11.0.0

# See Grafana provisioning for additionnal informations
# https://grafana.com/docs/grafana/latest/administration/provisioning/

# Copy configuration files
COPY ./config/postgres.yml /etc/grafana/provisioning/datasources/postgres.yml
COPY ./config/dashboards.yml /etc/grafana/provisioning/dashboards/dashboards.yml

# Copy dashboards
COPY ./dashboards/django-overview.json /var/lib/grafana/dashboards/django-overview.json
COPY ./dashboards/django-requests-by-view.json /var/lib/grafana/dashboards/django-requests-by-view.json
COPY ./dashboards/django-requests-overview.json /var/lib/grafana/dashboards/django-requests-overview.json
COPY ./dashboards/celery-monitoring.json /var/lib/grafana/dashboards/celery-monitoring.json
