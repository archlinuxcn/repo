# Maintainer : Peter Meier <meier.peter.email@gmail.com>
# Contributor : Bernhard Landauer <oberon@manjaro.org>

pkgname=clipit
_pkgname=ClipIt
pkgver=1.4.5
pkgrel=3
pkgdesc="Lightweight GTK+ clipboard manager (fork of Parcellite)"
arch=('i686' 'x86_64')
url="https://github.com/CristianHenzel/ClipIt/"
license=('GPL3')
depends=('gtk3' 'libappindicator-gtk3')
makedepends=('intltool')
optdepends=('xdotool: for automatic paste')
source=("${_pkgname}-${pkgver}.tar.gz::${url}archive/v${pkgver}.tar.gz")
md5sums=('4BDAC39A13EDBFF09D66959F94CCCAED')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  ./autogen.sh
  ./configure --prefix=/usr --sysconfdir=/etc --with-gtk3
  make
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
}
