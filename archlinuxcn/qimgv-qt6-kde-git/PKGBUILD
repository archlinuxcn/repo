# Maintainer: gigas002 <gigas002@pm.me>

pkgname=qimgv-qt6-kde-git
_pkgname=qimgv
pkgver=v1.0.3.alpha.r119.g82e6b75
pkgrel=2
pkgdesc="Qt6 image viewer. Fast, configurable, easy to use. Supports video playback."
arch=(x86_64 i686 armv6h armv7h aarch64)
url="https://github.com/easymodo/qimgv"
license=('GPL3')
depends=('qt6-base' 'qt6-imageformats' 'qt6-svg' 'qt6-5compat' 'mpv' 'exiv2' 'opencv')
makedepends=('git' 'cmake' 'pkgconf' 'qt6-tools' 'ccache')
optdepends=('kimageformats: support for more image formats'
            'qt6-jpegxl-image-plugin: JPEG-XL support'
            'qt6-avif-image-plugin: AVIF support'
            )
provides=("qimgv")
conflicts=("qimgv")
patch="556.patch"
source=(git+"${url}".git
        $patch
)
md5sums=('SKIP'
         'baa77b45698b38f63c2e7b9a297196fb')

pkgver() {
    cd ${_pkgname}
    git describe --long --tags --abbrev=7 | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
    cd "${srcdir}/${_pkgname}"
    patch -p1 -i "${srcdir}/$patch"
    install -d build
}

build() {
    cd "${srcdir}/${_pkgname}/build"
    cmake .. \
        -DCMAKE_INSTALL_PREFIX:PATH=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_BUILD_TYPE=Release \
        -DKDE_SUPPORT=ON \
        -DCMAKE_CXX_COMPILER_LAUNCHER='ccache' \
        -DCMAKE_C_COMPILER_LAUNCHER='ccache'
    make
}

package() {
    cd "${srcdir}/${_pkgname}/build"
	make DESTDIR=${pkgdir} install
}
