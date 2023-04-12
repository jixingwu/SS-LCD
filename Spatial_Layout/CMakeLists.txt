cmake_minimum_required(VERSION 2.8.3)
project(SL)
set(CMAKE_BUILD_TYPE "Release")
set(CMAKE_CXX_FLAGS "-std=c++11")
find_package(Eigen3)

add_executable(SL_node main.cpp)
target_link_libraries(SL_node ${catkin_LIBRARIES})