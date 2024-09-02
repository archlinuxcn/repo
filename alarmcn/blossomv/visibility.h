#pragma once

#if defined(_WIN32) || defined(__CYGWIN__)
  #ifdef interface_EXPORTS
    #ifdef __GNUC__
      #define INTERFACE_EXPORT __attribute__ ((dllexport))
    #else
      #define INTERFACE_EXPORT __declspec(dllexport)
    #endif
  #else
    #ifdef __GNUC__
      #define INTERFACE_EXPORT __attribute__ ((dllimport))
    #else
      #define INTERFACE_EXPORT __declspec(dllimport)
    #endif
  #endif
#else
  #if __GNUC__ >= 4
    #define INTERFACE_EXPORT __attribute__ ((visibility ("default")))
  #else
    #define INTERFACE_EXPORT
  #endif
#endif
