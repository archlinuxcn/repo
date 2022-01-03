# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgname=libdispatch
pkgver=5.5.0
pkgrel=1
pkgdesc='Comprehensive support for concurrent code execution on multicore hardware'
arch=(i686 x86_64 arm armv6h armv7h aarch64)
url=https://apple.github.io/swift-corelibs-libdispatch
license=(Apache)
depends=(glibc)
makedepends=(git clang cmake)
conflicts=(libdispatch-git swift swift-development libblocksruntime)
provides=(libblocksruntime)
source=("${pkgname}::git+https://github.com/apple/swift-corelibs-libdispatch.git#tag=swift-${pkgver%.0}-RELEASE"
        remove-werror.patch
        avoid-libkqueue.patch)
sha512sums=('SKIP'
            'd7d05ff6fa2ece40fea51e97f1af04e25ae9c2b55246fa2d753c446cff380262e611f9abb5112b7c7c94730362f0d06e0ccd867477c9470d1154e9c65e540529'
            '9f954538eee6ca63170c9fcf28cbcc090392360157c03bb33783789182102854ab344b432ff9f5603b873cb2540ffecf83458be559757eb094286cb41d9ba9ea')

prepare () {
	cd "${pkgname}"
	patch -p0 < "${srcdir}/remove-werror.patch"
	patch -p0 < "${srcdir}/avoid-libkqueue.patch"
}

build () {
	CC=clang CXX=clang++ cmake -S"${pkgname}" -Bbuild \
		-DCMAKE_BUILD_TYPE=RelWithDebInfo \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DBlocksRuntime_INCLUDE_DIR=/usr/include \
		-DBlocksRuntime_LIBRARIES=/usr/lib/libBlocksRuntime.so
	cmake --build build
}

check () {
	cmake --build build -j 1 --target test
}

package () {
	DESTDIR="${pkgdir}" cmake --install build
}
