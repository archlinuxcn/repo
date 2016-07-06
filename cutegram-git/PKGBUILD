# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Contributor: Llumex03
# Maintainer in Chakra: gnastyle
# Contributor in Chakra: FranzMari from Chakra
# Contributor in Chakra: danyf90 <daniele.formihelli@gmail.com>
# Contributor in Chakra: totoloco <totoloco@gmx.com>

pkgname=cutegram-git
pkgver=2.9.5.dev.r10.g2827175
pkgrel=1
pkgdesc="Telegram client by Aseman Land"
arch=('i686' 'x86_64')
url="http://aseman.co/cutegram"
license=('GPL')
depends=('libqtelegram-ae' 'telegramqml' 'aseman-qt-tools')
optdepends=('gst-plugins-good: for audio and notification support'
            'gst-plugins-bad: for audio support')
makedepends=('git')
source=("${pkgname}"::"git+https://github.com/Aseman-Land/Cutegram.git")
md5sums=('SKIP')

pkgver() {
  cd "${srcdir}/${pkgname}"
  ( set -o pipefail
    git describe --long --tags 2>/dev/null | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
  )
}

prepare() {
  cd "${srcdir}/${pkgname}"
  mkdir -p build
}

build() {
  cd "${srcdir}/${pkgname}/build"
  qmake-qt5 .. QMAKE_CFLAGS_ISYSTEM= PREFIX=/usr
  make
}

package() {
  cd "${srcdir}/${pkgname}/build"
  make INSTALL_ROOT="${pkgdir}" install
}
