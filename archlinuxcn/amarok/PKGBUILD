# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: Ronald van Haren <ronald@archlinux.org>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: damir <damir@archlinux.org>

pkgname=amarok
pkgver=2.9.0.r497.55664bf5ba
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
_commit="55664bf5bab1289b8565a46d916e751191d99db5"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/KDE/${pkgname}/archive/${_commit}.tar.gz")
sha256sums=("905bde932d0a8633357c979f9bf01a004560383ae52119220c8129ef9f4ddd29")

#git describe --long --tags 2> /dev/null | sed "s/^[A-Za-z\.\-]*//;s/\([^-]*-\)g/r\1/;s/-/./g"
#git rev-parse HEAD
#source=("http://download.kde.org/stable/${pkgname}/${pkgver}/src/${pkgname}-${pkgver}.tar.xz"{,.sig})
#validpgpkeys=("D81C0CB38EB725EF6691C385BB463350D6EF31EF") # Heiko Becker <heirecka@exherbo.org>

prepare() {
  cd "${srcdir}/${pkgname}-${_commit}"

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
