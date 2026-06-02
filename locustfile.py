from locust import HttpUser, task, between
import random

"""class WebUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def main(self):
        self.client.get("/")
"""

class APIUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://127.0.0.1:8000"

    @task(3)
    def listar_usuarios(self):
        self.client.get("/api/users/")

    @task(1)
    def crear_usuario(self):
        numero = random.randint(1, 99)
        self.client.post(
            "/api/users/", 
            json={
                "username": f"testjavi_{numero}",
                "email": f"testjavi_{numero}@example.com",
                "password":"123"
            }
        )