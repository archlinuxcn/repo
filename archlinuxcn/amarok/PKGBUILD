# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: Ronald van Haren <ronald@archlinux.org>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: damir <damir@archlinux.org>

pkgname=amarok
pkgver=2.9.0.r465.df34fd789a
pkgrel=1
pkgdesc="The powerful music player for KDE"
arch=("x86_64")
url="http://${pkgname}.kde.org/"
license=("FDL" "GPL2" "LGPL2.1")
depends=("kcmutils" "kdoctools" "kdnssd" "kirigami2" "knewstuff" "ktexteditor" "liblastfm-qt5" "libofa" "mariadb" "phonon-qt5" "qt5-script" "qt5-webengine" "taglib-extras" "threadweaver")
makedepends=("extra-cmake-modules" "gdk-pixbuf2" "git" "knotifyconfig" "loudmouth")
optdepends=(
  "ifuse: support for Apple iPod Touch and iPhone"
  "loudmouth: backend needed by mp3tunes for syncing"
)
_commit="df34fd789a8cd14bea5482c88c85216b2ef791c9"
source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/KDE/${pkgname}/archive/${_commit}.tar.gz"
  "${pkgname}_mariadb.patch"
)
sha256sums=(
  "2af40c5a4a5628f3cbd21f535cba8d08027d9e418b5d36db15ae275722f189af"
  "d6540427b3a4e81d87c761b5e8ac918b035af8f92b30778f735f6be449889091"
)

#git describe --long --tags 2> /dev/null | sed "s/^[A-Za-z\.\-]*//;s/\([^-]*-\)g/r\1/;s/-/./g"
#git rev-parse HEAD
#source=("http://download.kde.org/stable/${pkgname}/${pkgver}/src/${pkgname}-${pkgver}.tar.xz"{,.sig})
#validpgpkeys=("D81C0CB38EB725EF6691C385BB463350D6EF31EF") # Heiko Becker <heirecka@exherbo.org>

prepare() {
  cd "${srcdir}/${pkgname}-${_commit}"
  patch -Np1 -i "${srcdir}/amarok_mariadb.patch"

  mkdir -p "${srcdir}/${pkgname}-${_commit}/build"
}

build() {
  cd "${srcdir}/${pkgname}-${_commit}/build"
  cmake "${srcdir}/${pkgname}-${_commit}" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DBUILD_TESTING=OFF
  make
}

package() {
  cd "${srcdir}/${pkgname}-${_commit}/build"
  make DESTDIR="${pkgdir}" install
}
