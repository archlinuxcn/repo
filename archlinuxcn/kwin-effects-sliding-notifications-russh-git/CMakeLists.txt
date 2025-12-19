cmake_minimum_required(VERSION 4.0)
project(kwin-effects-sliding-notifications)

set(KF_MIN_VERSION "6.0.0")
set(QT_MIN_VERSION "6.6.0")

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(ECM ${KF_MIN_VERSION} REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${ECM_MODULE_PATH})

include(FeatureSummary)
include(KDEInstallDirs)
include(KDECMakeSettings)
include(KDECompilerSettings NO_POLICY_SCOPE)

find_package(Qt6 ${QT_MIN_VERSION} REQUIRED COMPONENTS
    Core
    Gui
)

find_package(KF6 ${KF_MIN_VERSION} REQUIRED COMPONENTS
    Config
    ConfigWidgets
    CoreAddons
    WindowSystem
)

find_package(epoxy REQUIRED)
find_package(XCB REQUIRED COMPONENTS
    XCB
)

find_package(KWin 6.0.0 REQUIRED COMPONENTS
    kwin
)

kcoreaddons_add_plugin(slidingnotifications INSTALL_NAMESPACE "kwin/effects/plugins")

target_sources(slidingnotifications PRIVATE
    SlidingEffect.cpp
)

target_link_libraries(slidingnotifications
    Qt6::Core
    Qt6::Gui

    KF6::ConfigCore
    KF6::ConfigGui
    KF6::CoreAddons
    KF6::WindowSystem

    KWin::kwin
)

feature_summary(WHAT ALL FATAL_ON_MISSING_REQUIRED_PACKAGES)
