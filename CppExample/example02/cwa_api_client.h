#include "base_api_client.h"

class CWAAPIClient: BaseAPIClient {
public:
    string getServiceName();
    int connect();
    int get(string url);
    int disconnect();
};
