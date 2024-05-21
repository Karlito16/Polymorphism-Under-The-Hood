#include "cwa_api_client.h"
#include "route_api_client.h"

using namespace std;

template<class BaseAPIClient>
void action(BaseAPIClient client, string url) {
    cout << endl;
    client.connect();
    int statusCode = client.get(url);
    cout << "Action completed with status code: " << statusCode << endl;
    client.disconnect();
}

int main() {
    CWAAPIClient cwa;
    RouteAPIClient route;

    action(cwa, "/api/v1/machines");
    action(route, "/api/v1/routes");

    return 0;
}
