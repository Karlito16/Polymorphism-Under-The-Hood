from cwa_api_client import CWAAPIClient
from route_api_client import RouteAPIClient


def action(client, url):
    print()
    client.connect()
    status_code = client.get(url)
    print(f"Action completed with status code: {status_code}")
    client.disconnect()


def main():
    cwa = CWAAPIClient()
    route = RouteAPIClient()

    action(cwa, "/api/v1/machines")
    action(route, "/api/v1/routes")


main()
