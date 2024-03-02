# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: speps <speps at aur dot archlinux dot org>

_plugins_ver=3.16
pkgname=nomacs
pkgver=3.17.2295
pkgrel=1
epoch=1
pkgdesc="A Qt image viewer"
arch=(x86_64)
url="https://github.com/nomacs/nomacs"
license=(GPL3)
depends=(exiv2 gcc-libs glibc libraw libtiff opencv qt5-base qt5-svg quazip-qt5)
#depends+=(libopencv_imgproc.so)
makedepends=(cmake git git-lfs qt5-tools python)
optdepends=('qt5-imageformats: support additional image formats'
            'kimageformats5: support QOI (Quite OK Image Format)')
source=("git+https://github.com/nomacs/nomacs.git#tag=${pkgver}"
        "nomacs-plugins-${_plugins_ver}.tar.gz::https://github.com/nomacs/nomacs-plugins/archive/${_plugins_ver}.tar.gz")
b2sums=('SKIP'
        '2bda4f36d56709653f6696af3404e416fd2d9fe7fa11de9636643c728028018ac769df3e2e519799322c5c42006cdc114d0e6406f9f60294234b07d9fd8d8409')

export GIT_LFS_SKIP_SMUDGE=1

prepare() {
  cd "nomacs"
  # copy plugin sources into place
  cp -av "${srcdir}/nomacs-plugins-${_plugins_ver}/"* "ImageLounge/plugins"
}

build() {
  cd nomacs
  cmake -B build -S ImageLounge -Wno-dev \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DUSE_SYSTEM_QUAZIP=ON \
    -DENABLE_AVIF=ON \
    -DENABLE_TRANSLATIONS=ON

  cmake --build build
}

package() {
  cd nomacs
  DESTDIR="$pkgdir" cmake --install build
}
