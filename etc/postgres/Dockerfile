FROM postgres:16

# Install build dependencies and pg_cron extension
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-server-dev-16 \
    postgresql-16-cron \
    build-essential \
    ca-certificates \
    git \
    && rm -rf /var/lib/apt/lists/*

# Add pg_cron to shared_preload_libraries
RUN echo "shared_preload_libraries = 'pg_cron'" >> /usr/share/postgresql/postgresql.conf.sample

# Create initialization script directly in the Dockerfile
RUN mkdir -p /docker-entrypoint-initdb.d
RUN echo '#!/bin/bash\nset -e\n\necho "Creating pg_cron extension..."\n\n# Set the cron.database_name parameter to the current database\npsql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -c "ALTER SYSTEM SET cron.database_name TO \047$POSTGRES_DB\047;"\n\n# Reload the configuration\npsql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -c "SELECT pg_reload_conf();"\n\n# Create the extension\npsql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -c "CREATE EXTENSION IF NOT EXISTS pg_cron;"\n\necho "pg_cron extension has been installed and configured."' > /docker-entrypoint-initdb.d/10_pg_cron.sh
RUN chmod +x /docker-entrypoint-initdb.d/10_pg_cron.sh

COPY ./etc/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN find /usr/local/bin/maintenance/ -type f -exec  sed -i 's/\r$//g' {} \;
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance
