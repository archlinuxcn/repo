#----------------------------------------------------------------
# Generated CMake target import file for configuration "None".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Arcus" for configuration "None"
set_property(TARGET Arcus APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(Arcus PROPERTIES
  IMPORTED_LOCATION_NONE "/usr/lib/libArcus.so.5.1.0"
  IMPORTED_SONAME_NONE "libArcus.so.5"
  )

list(APPEND _IMPORT_CHECK_TARGETS Arcus )
list(APPEND _IMPORT_CHECK_FILES_FOR_Arcus "/usr/lib/libArcus.so.5.1.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
