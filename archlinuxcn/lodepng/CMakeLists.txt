cmake_minimum_required(VERSION 3.14)
project(lodepng)

set(CMAKE_CXX_VISIBILITY_PRESET     hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN YES)

file(READ "lodepng.cpp" version)
string(REGEX MATCH ".*LODEPNG_VERSION_STRING = \"([0-9]*)\"" _ ${version})
string(SUBSTRING "${CMAKE_MATCH_1}" 0 4 ver_major)
string(SUBSTRING "${CMAKE_MATCH_1}" 4 2 ver_minor)
string(SUBSTRING "${CMAKE_MATCH_1}" 6 2 ver_patch)

if(NOT APPLE)
    set(CMAKE_INSTALL_RPATH $ORIGIN)
endif()

include(GNUInstallDirs)
include(GenerateExportHeader)
include(CMakePackageConfigHelpers)

add_library(lodepng SHARED lodepng.cpp lodepng.h)
generate_export_header(${CMAKE_PROJECT_NAME})

set_target_properties(
    ${CMAKE_PROJECT_NAME} PROPERTIES
    SOVERSION ${ver_major}
    VERSION ${ver_major}.${ver_minor}.${ver_patch}
)

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_PROJECT_NAME}ConfigVersion.cmake
    VERSION ${ver_major}.${ver_minor}.${ver_patch}
    COMPATIBILITY SameMinorVersion
)

install(TARGETS ${CMAKE_PROJECT_NAME} EXPORT ${CMAKE_PROJECT_NAME}Target
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
            COMPONENT ${CMAKE_PROJECT_NAME}_Runtime
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
            COMPONENT ${CMAKE_PROJECT_NAME}_RunTime
            NAMELINK_COMPONENT ${CMAKE_PROJECT_NAME}_Development
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
            COMPONENT ${CMAKE_PROJECT_NAME}_Development
)
install(FILES lodepng.h DESTINATION include)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_PROJECT_NAME}ConfigVersion.cmake
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/${CMAKE_PROJECT_NAME}/cmake
)
install(EXPORT ${CMAKE_PROJECT_NAME}Target
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/${CMAKE_PROJECT_NAME}/cmake
        FILE ${CMAKE_PROJECT_NAME}Config.cmake
)
