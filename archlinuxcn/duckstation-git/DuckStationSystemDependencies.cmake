# Downstream Arch Linux dependency discovery.
# DuckStation upstream only supports its prebuilt dependency bundle; this module
# deliberately uses distribution libraries instead.

set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
find_package(PkgConfig REQUIRED)
find_package(Libbacktrace REQUIRED)
find_package(ZLIB REQUIRED)
find_package(zstd 1.5.7 CONFIG REQUIRED)

function(import_shared_library target header library)
  string(MAKE_C_IDENTIFIER "${target}" var)
  find_path(${var}_INCLUDE_DIR NAMES "${header}" REQUIRED)
  find_library(${var}_LIBRARY NAMES "${library}" REQUIRED)
  add_library(${target} SHARED IMPORTED)
  set_target_properties(${target} PROPERTIES
    IMPORTED_LOCATION "${${var}_LIBRARY}"
    INTERFACE_INCLUDE_DIRECTORIES "${${var}_INCLUDE_DIR}")
endfunction()

# Several official Arch packages intentionally do not ship upstream CMake
# package files, while DuckStation expects the targets exported by its bundle.
import_shared_library(WebP::webp webp/decode.h webp)

find_package(PNG 1.6.54 CONFIG REQUIRED)

find_package(libjpeg-turbo 3.1.4.1 CONFIG QUIET)
if(NOT TARGET libjpeg-turbo::jpeg)
  import_shared_library(libjpeg-turbo::jpeg jpeglib.h jpeg)
endif()

find_package(Freetype 2.14.3 REQUIRED)
find_package(harfbuzz CONFIG REQUIRED)

import_shared_library(SQLite3::sqlite3-shared sqlite3.h sqlite3)

# These two dependencies are not available in Arch's official repositories and
# are built into the private prefix supplied through CMAKE_PREFIX_PATH.
find_package(plutosvg 0.0.7 CONFIG REQUIRED)
find_package(DiscordRPC 3.4.0 CONFIG REQUIRED)

import_shared_library(cpuinfo::cpuinfo cpuinfo.h cpuinfo)

find_package(SoundTouch 2.3.3 CONFIG REQUIRED)
set_target_properties(SoundTouch::SoundTouchDLL PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES "${CMAKE_PREFIX_PATH}/include")
find_package(libzip 1.11.4 CONFIG REQUIRED)

find_package(Shaderc 2026.1 CONFIG REQUIRED)
find_path(SPIRV_CROSS_INCLUDE_DIR NAMES spirv_cross_c.h PATH_SUFFIXES spirv_cross REQUIRED)
find_library(SPIRV_CROSS_LIBRARY NAMES spirv-cross-c-shared REQUIRED)
add_library(spirv-cross-c-shared SHARED IMPORTED)
set_target_properties(spirv-cross-c-shared PROPERTIES
  IMPORTED_LOCATION "${SPIRV_CROSS_LIBRARY}"
  INTERFACE_INCLUDE_DIRECTORIES "${SPIRV_CROSS_INCLUDE_DIR}")

find_package(SDL3 3.4.4 CONFIG REQUIRED)

set(QT_NO_PRIVATE_MODULE_WARNING ON)
if(LINUX)
  find_package(Qt6 6.11.1 REQUIRED COMPONENTS Core Gui GuiPrivate Widgets LinguistTools DBus)
else()
  find_package(Qt6 6.11.1 REQUIRED COMPONENTS Core Gui GuiPrivate Widgets LinguistTools)
endif()

find_package(CURL REQUIRED)
if(LINUX)
  find_package(UDEV REQUIRED)
endif()

if(NOT APPLE)
  if(ENABLE_X11)
    find_package(X11 REQUIRED)
    if(NOT X11_xcb_FOUND)
      message(FATAL_ERROR "XCB is required")
    endif()
  endif()

  if(ENABLE_WAYLAND)
    find_package(ECM REQUIRED NO_MODULE)
    list(APPEND CMAKE_MODULE_PATH "${ECM_MODULE_PATH}")
    find_package(Wayland REQUIRED Egl)
  endif()
endif()

find_package(FFMPEG 8.1.1 COMPONENTS avcodec avformat avutil swresample swscale)
if(NOT FFMPEG_FOUND)
  message(WARNING "FFmpeg not found, using bundled headers.")
  set(FFMPEG_INCLUDE_DIRS "${CMAKE_SOURCE_DIR}/dep/ffmpeg/include")
endif()
