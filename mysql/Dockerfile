
FROM mysql


# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup
COPY initscript.sql /docker-entrypoint-initdb.d/


EXPOSE 3306

CMD ["mysqld"]
