FROM mongo:6.0
WORKDIR /docker-entrypoint-initdb.d
COPY createUser.js /docker-entrypoint-initdb.d/
EXPOSE 27017