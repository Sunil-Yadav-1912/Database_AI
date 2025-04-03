FROM python:3.11-slim-bookworm

RUN apt-get update && \
    apt-get install -y python3-dev python3-mysqldb git curl zip systemd php && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./Database_AI/requirements.txt

RUN pip3 install -r ./Database_AI/requirements.txt

COPY . ./Database_AI

COPY ./init_modified.py ./Database_AI/venv/lib/python3.11/site-packages/vanna/flask/__init__.py
COPY ./base_modified.py ./Database_AI/venv/lib/python3.11/site-packages/vanna/base/base.py

# Set environment variables
ENV FLASK_APP=./Database_AI/app.py
RUN chmod +x ./Database_AI/gunicorn.sh

# Set the entrypoint
ENTRYPOINT ["./Database_AI/gunicorn.sh"]

# Expose the port
EXPOSE 5007