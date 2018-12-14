from lilaclib import *

build_prefix = "extra-x86_64"
depends = ['mingw-w64-binutils', 'mingw-w64-headers', ('mingw-w64-winpthreads', 'mingw-w64-headers-bootstrap')]

if __name__ == "__main__":
    single_main('extra-x86_64')
