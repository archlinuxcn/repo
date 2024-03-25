cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
project(uswitcher)

set(QT_MAJOR_VERSION 6)

find_package(ECM 5.0.0 REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH} ${ECM_KDE_MODULE_DIR})

include(KDEInstallDirs)

find_package(Plasma REQUIRED)

plasma_install_package(package com.dv.uswitcher)
