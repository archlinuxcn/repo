# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: speps <speps at aur dot archlinux dot org>

_plugins_ver=3.16
pkgname=nomacs
pkgver=3.21.1
pkgrel=1
pkgdesc="A Qt image viewer"
arch=(x86_64)
url="https://github.com/nomacs/nomacs"
license=(GPL-3.0-only)
depends=(exiv2 gcc-libs glibc libraw libtiff opencv qt6-base qt6-svg quazip-qt6)
#depends+=(libopencv_imgproc.so)
makedepends=(cmake git git-lfs qt6-tools python)
optdepends=('qt6-imageformats: support additional image formats'
            'kimageformats: support QOI (Quite OK Image Format)')
source=("git+https://github.com/nomacs/nomacs.git#tag=${pkgver}"
        #"nomacs-plugins-qt6_01.patch::https://github.com/nomacs/nomacs-plugins/pull/40/commits/1b87f615ce0e7125ec739bc3e40d8ff7f6783587.patch"
        #"nomacs-plugins-qt6_02.patch::https://github.com/nomacs/nomacs-plugins/pull/40/commits/a869962f051504dd2c1dedeb3bc3d266c17070c1.patch"
        #"nomacs-plugins-${_plugins_ver}.tar.gz::https://github.com/nomacs/nomacs-plugins/archive/${_plugins_ver}.tar.gz"
        )
b2sums=('beb4af1e5a08104cf860f19f156962668ece3f7ec284e7c2d92761a500de26378cb3d5467ad23245b306150b077b61335e9833a17098eea0ee4fb09e48481820')

export GIT_LFS_SKIP_SMUDGE=1

prepare() {
  #cd "nomacs-plugins-${_plugins_ver}"
  #patch -Np1 -i ../nomacs-plugins-qt6_01.patch
  #patch -Np1 -i ../nomacs-plugins-qt6_02.patch

  cd "${srcdir}/nomacs"
  # copy plugin sources into place
  #cp -av "${srcdir}/nomacs-plugins-${_plugins_ver}/"* "ImageLounge/plugins"
}

build() {
  cd nomacs
  cmake -B build -S ImageLounge -Wno-dev \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DQT_VERSION_MAJOR=6 \
    -DUSE_SYSTEM_QUAZIP=ON \
    -DENABLE_AVIF=ON \
    -DENABLE_QUAZIP=ON \
    -DENABLE_TRANSLATIONS=ON

  cmake --build build
}

package() {
  cd nomacs
  DESTDIR="$pkgdir" cmake --install build
}
