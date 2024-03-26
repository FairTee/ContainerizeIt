#!/usr/bin/python3

from container_management import create_container, list_containers
import pytest

@pytest.fixture
def client():
    from app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_container(client):
    response = client.get('/containers/create?image=nginx&name=my-nginx')
    assert response.status_code == 201
    assert b"Container 'my-nginx' created successfully." in response.data

def test_list_containers(client):
    response = client.get('/containers/list')
    assert response.status_code == 200
    assert b"my-nginx" in response.data
