import requests
import pytest # have to install via command "pip3 install -U pytest"
from uuid import uuid4

def test_health_check():
    r = requests.get('http://localhost:8085')
    assert(r.status_code == 404)

def test_name_input():
    name = str(uuid4())
    r = requests.get('http://localhost:8085/hello-world?name={name}'.format(name=name))
    assert('Hello, {name}!'.format(name=name) == r.json().get('content'))

def test_id_increment():
    r = requests.get('http://localhost:8085/hello-world?name={name}'.format(name=str(uuid4())))
    previous_id = r.json().get('id')
    r = requests.get('http://localhost:8085/hello-world?name={name}'.format(name=str(uuid4())))
    assert( previous_id + 1 == r.json().get('id'))
