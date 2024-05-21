#include "base_api_client.h"

class RouteAPIClient: BaseAPIClient {
public:
    string getServiceName();
    int connect();
    int get(string url);
    int disconnect();
};
