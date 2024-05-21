

class CWAAPIClient:

    def get_service_name(self):
        return "Cloud Web App"

    def connect(self):
        print(f"Connecting to {self.get_service_name()}...")
        print("Connected!")
        return 0

    def get(self, url):
        print(f"Sending HTTP-GET request to {self.get_service_name()}: {url}")
        return 200

    def disconnect(self):
        print(f"Disconnecting from {self.get_service_name()}...")
        print("Disconnected!")
        return 0
