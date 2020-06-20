# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: Ronald van Haren <ronald@archlinux.org>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: damir <damir@archlinux.org>

pkgname=amarok
pkgver=2.9.0.r458.3afd3cf638
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
_commit="3afd3cf638a22ff11e4020c6b11de3b9020a3792"
source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/KDE/${pkgname}/archive/${_commit}.tar.gz"
  "${pkgname}_mariadb.patch"
)
sha256sums=(
  "41574f4bafe4ff6205a1b2ff3e4a089ab735b9b128d17c04f4cd7fc340f21eb7"
  "029937d925993fa0b3cbe460f6d0c8f9fd624fc8dffff22acbbd3da600720dab"
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
