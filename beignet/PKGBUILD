# Maintainer: Bruno Pagani (a.k.a. ArchangeGabriel) <bruno.n.pagani@gmail.com>
# Contributor: Antoine Lubineau <antoine@lubignon.info>
# Contributor: Leopold Bloom <blinxwang@gmail.com>
# Contributor: Michal Krenek (a.k.a. Mikos) <m.krenek@gmail.com>

pkgname=beignet
pkgver=1.3.0
pkgrel=1
pkgdesc="An open source OpenCL implementation for Intel IvyBridge+ iGPUs"
arch=('x86_64')
url="https://01.org/${pkgname}"
license=('LGPL')
depends=('glu' 'llvm' 'mesa' 'ocl-icd' 'opencl-headers')
makedepends=('clang' 'cmake' 'python')
provides=('opencl-intel')
conflicts=('opencl-intel')
source=("https://01.org/sites/default/files/${pkgname}-${pkgver}-source.tar.gz")
sha256sums=('63d98b4fe8fba3dbc0299d29fef84560625e5ac51b16b8fed453021d4afb5cd5')

prepare() {
    cd ${pkgname^}-${pkgver}-Source
    mkdir -p build
}

build() {
    cd ${pkgname^}-${pkgver}-Source/build

    cmake .. \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=/usr/lib \
        -DCMAKE_BUILD_TYPE=RELEASE
    make
}

package() {
    cd ${pkgname^}-${pkgver}-Source/build

    make DESTDIR="${pkgdir}" install

    # Remove headers already provided by 'opencl-headers'
    cd "${pkgdir}/usr/include/CL"
    rm cl.h cl_egl.h cl_ext.h cl_gl.h cl_gl_ext.h cl_platform.h opencl.h
}
