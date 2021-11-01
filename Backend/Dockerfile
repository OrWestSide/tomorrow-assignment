FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /opt/project/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY requirements/requirements.txt /opt/project/requirements.txt

# install dependencies
RUN set -eux \
    && pip install -r /opt/project/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . /opt/project

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]