cmake_minimum_required(VERSION 3.27)
project(CppExample)

set(CMAKE_CXX_STANDARD 17)

add_executable(CppExample main.cpp
        base_api_client.cpp
        cwa_api_client.cpp
        route_api_client.cpp)
