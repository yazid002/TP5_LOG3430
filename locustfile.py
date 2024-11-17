from locust import HttpUser, TaskSet, task, between

class SimpleTasks(TaskSet):
    @task(1)
    def home(self):
        # Test the home route
        self.client.get("/")

    @task(2)
    def fast(self):
        # Test the fast route
        self.client.get("/fast")

    @task(3)
    def medium(self):
        # Test the medium route
        self.client.get("/medium")

    @task(4)
    def heavy(self):
        # Test the heavy route
        self.client.get("/heavy")

    @task(1)
    def echo(self):
        # Test the echo route
        payload = {"message": "Hello, Locust!"}
        self.client.post("/echo", json=payload)


class SimpleUser(HttpUser):
    weight = 1 
    tasks = [SimpleTasks]
    wait_time = between(1, 5)  # Simulate a wait time between requests


class HeavyTasks(TaskSet):
    @task(1)
    def heavy_request(self):
        self.client.get("/heavy")

class HeavyUser(HttpUser):
    weight = 49
    tasks = [HeavyTasks]  
    wait_time = between(5, 10)  

