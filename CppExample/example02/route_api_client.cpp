#include "route_api_client.h"
#include <iostream>

using namespace std;

string RouteAPIClient::getServiceName() {
    return "Route";
}

int RouteAPIClient::connect() {
    cout << "Connecting to " << this->getServiceName() << "..." << endl;
    cout << "Connected!" << endl;
    return 0;
};

int RouteAPIClient::get(std::string url) {
    cout << "Sending HTTP-GET request to " << this->getServiceName() << ": " << url << endl;
    return 200;
}

int RouteAPIClient::disconnect() {
    cout << "Disconnecting from " << this->getServiceName() << "..." << endl;
    cout << "Disconnected!" << endl;
    return 0;
}
