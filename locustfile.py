from locust import HttpUser, task, between


class ProjectPerfTest(HttpUser):
    wait_time = between(1, 5)
    @task
    def index_route(self):
        response = self.client.get("/")

    @task
    def pointsDisplay_route(self):
        response = self.client.get("/pointsDisplay")

    @task
    def login_route(self):
        response = self.client.post("/showSummary", {"email": "john@simplylift.com"})

    @task
    def purchasePlaces_route(self):
        reponse = self.client.post("/purchasePlaces", {"competition": ["Winter Competition"], "club": ["Iron Temple"], "places": 1})



""" from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")

    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"}) """