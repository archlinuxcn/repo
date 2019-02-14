#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

int main(int argc, char *argv[]) {
  void *handle;
  const char *(*get_cdm_version)();

  handle = dlopen("./libwidevinecdm.so", RTLD_LAZY);
  if (!handle) {
    fprintf(stderr, "%s\n", dlerror());
    exit(EXIT_FAILURE);
  }

  get_cdm_version = dlsym(handle, "GetCdmVersion");
  if (!get_cdm_version) {
    fprintf(stderr, "%s\n", dlerror());
    exit(EXIT_FAILURE);
  }

  printf("%s\n", get_cdm_version());
  dlclose(handle);
  exit(EXIT_SUCCESS);
}

