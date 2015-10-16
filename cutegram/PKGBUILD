# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Contributor: Llumex03
# Maintainer in Chakra: gnastyle
# Contributor in Chakra: FranzMari from Chakra
# Contributor in Chakra: danyf90 <daniele.formihelli@gmail.com>
# Contributor in Chakra: totoloco <totoloco@gmx.com>

pkgname=cutegram
_pkgname=Cutegram
pkgver=2.7.0
pkgrel=3
pkgdesc="A different telegram client from Aseman team"
arch=('i686' 'x86_64')
url="http://aseman.co/en/products/cutegram/"
license=('GPL')
depends=('qt5-imageformats' 'qt5-webkit>=5.5' 'telegramqml>=0.9' 'libqtelegram-ae>=2:6.0')
optdepends=('gst-plugins-bad: audio support'
'gst-plugins-good: audio and notification sound')
conflicts=('cutegram-git' 'sigram-git' 'sigram' 'cutegram')
provides=('cutegram')
replaces=('cutegram-cn')

source=("https://github.com/Aseman-Land/Cutegram/archive/v$pkgver-stable.tar.gz")

sha256sums=('5ff195269f2492c625cca4b8eca6134c938e2b5a759019074e486335046c02d9')

prepare() {
  cd "${srcdir}/${_pkgname}-$pkgver-stable"
  mkdir -p build
}

build() {
  cd "${srcdir}/${_pkgname}-$pkgver-stable/build"
  qmake-qt5 -r .. PREFIX=/usr
  make
}

package() {
  cd "${srcdir}/${_pkgname}-$pkgver-stable/build"
  make INSTALL_ROOT="${pkgdir}" install
}
