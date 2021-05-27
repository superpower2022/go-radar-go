cmake_minimum_required(VERSION 3.9)

project(RoboMasterUILib VERSION 0.0.1 DESCRIPTION "RoboMaster UI Library Utility")

add_library(RoboMasterUILib SHARED
    ${CMAKE_CURRENT_SOURCE_DIR}/RM_Client_UI.c
)

include_directories(RoboMasterUILib
    ${CMAKE_CURRENT_SOURCE_DIR}
)

set_target_properties(RoboMasterUILib PROPERTIES VERSION ${PROJECT_VERSION})
set_target_properties(RoboMasterUILib PROPERTIES PUBLIC_HEADER RM_Client_UI.h)