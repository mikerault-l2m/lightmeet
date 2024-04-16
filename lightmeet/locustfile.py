import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def principal(self):
        self.client.get("")

    @task
    def blog(self):
        self.client.get("blog")

    @task
    def recherche(self):
        self.client.get("recherche")