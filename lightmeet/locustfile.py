import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    # Page principale : Visiteur de niveau 1
    @task
    def principal(self):
        self.client.get("")

    # Footer : Visiteur cliquant sur "Préférences des cookies"
    @task
    def preferences_cookies(self):
        self.client.get("legal_PC")

    # Footer : Visiteur cliquant sur "Mentions légales"
    @task
    def mentions_legales(self):
        self.client.get("legal_mentions_legales")

    # Visiteur cliquant sur "Comparer" ou "Rencontres"
    @task
    def recherche_rencontres(self):
        self.client.get("recherche_rencontres")

    # Visiteur cliquant sur "Thérapeutes"
    @task
    def recherche_therapeutes(self):
        self.client.get("recherche_therapeutes")
