# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: Ronald van Haren <ronald@archlinux.org>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: damir <damir@archlinux.org>

pkgname=amarok
pkgver=2.9.71
pkgrel=2
pkgdesc="The powerful music player for KDE"
arch=("x86_64")
url="http://${pkgname}.kde.org/"
license=("FDL" "GPL2" "LGPL2.1")
depends=("kcmutils" "kdoctools" "kdnssd" "kirigami2" "knewstuff" "ktexteditor" "liblastfm-qt5" "libofa" "mariadb" "phonon-qt5" "qt5-script" "qt5-tools" "qt5-webengine" "taglib-extras" "threadweaver")
makedepends=("extra-cmake-modules" "gdk-pixbuf2" "git" "knotifyconfig" "loudmouth")
optdepends=(
  "ifuse: support for Apple iPod Touch and iPhone"
  "loudmouth: backend needed by mp3tunes for syncing"
)
source=(
  "https://download.kde.org/unstable/${pkgname}/${pkgver}/${pkgname}-${pkgver}.tar.xz"
  "ffmpeg5_cmakelist_configure.patch::https://invent.kde.org/multimedia/amarok/-/merge_requests/45.diff"
)
sha256sums=(
  "6a404829d336f69415fb6bb4ea1d5566759fb95e3e84f904ee9ef82a7be4e84f"
  "77a1f8cbc7f786e5616fbb5922dcf193614dbdf2a1d3fa2b2196c3fdb2f0387b"
)

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  # Patching to fix FFMPEG5 and CMakeLists bug with config.h definition position https://invent.kde.org/multimedia/amarok/-/merge_requests/45
  patch -Np1 -i "${srcdir}/ffmpeg5_cmakelist_configure.patch"

  mkdir -p "${srcdir}/${pkgname}-${pkgver}/build"
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  cmake "${srcdir}/${pkgname}-${pkgver}" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DBUILD_TESTING=OFF
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  make DESTDIR="${pkgdir}" install
}
