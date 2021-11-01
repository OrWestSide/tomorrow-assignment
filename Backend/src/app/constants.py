"""
ATTENTION: Be aware that this file is replaced by k8s configmap in every
deployment. Therefore any variables added here should be also added in the
configmap!
"""
from os import environ

SQLALCHEMY_DATABASE_URL = environ.get(
    'SQLALCHEMY_DATABASE_URL', 'mysql://root:root@172.17.0.1/uber2'
)
