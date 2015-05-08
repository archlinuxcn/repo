# Maintainer in AUR: Jiachen Yang <farseerfc@gmail.com>
# Contributor to AUR by: Llumex03
# Maintainer in Chakra: gnastyle
# Contributor in Chakra: FranzMari from Chakra
# Contributor in Chakra: danyf90 <daniele.formihelli@gmail.com>
# Contributor in Chakra: totoloco <totoloco@gmx.com>

pkgname=cutegram-cn
_pkgname=Cutegram
pkgver=2.2.0
pkgrel=2
pkgdesc="A different telegram client from Aseman team, with Chinese translations"
arch=('i686' 'x86_64')
url="http://aseman.co/en/"
license=('GPL')
depends=('qt5-base' 'qt5-declarative' 'qt5-multimedia' 'qt5-quick1'
'qt5-graphicaleffects' 'qt5-quickcontrols' 'libqtelegram-ae-git')
makedepends=('gcc' 'cmake')
conflicts=('cutegram-git' 'sigram-git' 'sigram' 'cutegram')
provides=('cutegram')

source=("https://github.com/Aseman-Land/Cutegram/archive/v$pkgver-stable.tar.gz")

sha256sums=('4a61a96a87ce015bb4fd18a7ccfa6df7ea978938507168b4dbf491a8cd068188')

prepare() {
  cd "${srcdir}/${_pkgname}-$pkgver-stable"
  sed -i 's/webkitwidgets //' Cutegram/Cutegram.pro
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
