#pragma once
#include <iostream>

using namespace std;

class BaseAPIClient {
public:
    virtual ~BaseAPIClient();
    virtual string getServiceName()=0;
    virtual int connect()=0;
    virtual int get(string url)=0;
    virtual int disconnect()=0;
};

