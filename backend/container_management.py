#!usr/bin/python3

import docker
from flask import jsonify

client = docker.from_env()

def create_container(image, name):
    try:
        container = client.containers.run(image, detach=True, name=name)
        return jsonify({"message": f"Container '{container.name}' created successfully."}), 201
    except docker.errors.ImageNotFound:
        return jsonify({"error": "Image not found."}), 404
    except docker.errors.APIError as e:
        return jsonify({"error": f"Failed to create container: {str(e)}"}), 500

def list_containers():
    containers = client.containers.list()
    container_info = [{"name": container.name, "status": container.status} for container in containers]
    return jsonify(container_info), 200
