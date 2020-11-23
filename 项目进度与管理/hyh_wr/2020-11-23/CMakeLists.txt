cmake_minimum_required(VERSION 3.10)
project(rs_test)
set(CMAKE_CXX_STANDARD 11)
#set(CMAKE_CXX_FLAGS "-std=c++11")

#aux_source_directory(. main.cpp)
add_executable(rs_test show_distance.cpp)

#寻找opencv库
find_package(OpenCV REQUIRED)
#message(STATUS ${OpenCV_INCLUDE_DIRS})
#添加头文件
include_directories(${OpenCV_INCLUDE_DIRS})
#链接Opencv库
target_link_libraries(rs_test ${OpenCV_LIBS} )
#添加后可进行调试
set( CMAKE_BUILD_TYPE Debug )
set(DEPENDENCIES realsense2 )
target_link_libraries(rs_test ${DEPENDENCIES})


