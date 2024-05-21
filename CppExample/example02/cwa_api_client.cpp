#include "cwa_api_client.h"
#include <iostream>

using namespace std;

string CWAAPIClient::getServiceName() {
    return "Cloud Web App";
}

int CWAAPIClient::connect() {
    cout << "Connecting to " << this->getServiceName() << "..." << endl;
    cout << "Connected!" << endl;
    return 0;
};

int CWAAPIClient::get(std::string url) {
    cout << "Sending HTTP-GET request to " << this->getServiceName() << ": " << url << endl;
    return 200;
}

int CWAAPIClient::disconnect() {
    cout << "Disconnecting from " << this->getServiceName() << "..." << endl;
    cout << "Disconnected!" << endl;
    return 0;
}

