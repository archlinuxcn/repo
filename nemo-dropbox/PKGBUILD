# Maintainer: Sebastian Lau <lauseb644 _at_ gmail.com>
# Contributor: twa022 <twa022 at gmail dot com>
# Contributor: American_Jesus <american.jesus.pt AT gmail DOT com>

pkgname=nemo-dropbox
pkgver=3.4.0
pkgrel=2
pkgdesc="Dropbox for Linux - Nemo extension"
arch=('i686' 'x86_64')
url="https://github.com/linuxmint/nemo-extensions"
license=('custom:CC-BY-ND-3' 'GPL')
depends=('nemo>=3.2' 'dropbox')
makedepends=('glib2')
install=${pkgname}.install
options=('!libtool' '!emptydirs')

source=("nemo-extensions-$pkgver.tar.gz::https://github.com/linuxmint/nemo-extensions/archive/$pkgver.tar.gz"
	"01-Remove-python-dependencies.patch")
md5sums=('b8aff74acc98be098fe46a54dcb5c35f'
         '98d2f4a760361e140a09673df42853d1')

prepare() {
  cd "${srcdir}/nemo-extensions-${pkgver}/${pkgname}"
  patch -uNp2 -r- -i ../../01-Remove-python-dependencies.patch
}

build() {
  cd "${srcdir}/nemo-extensions-${pkgver}/${pkgname}"

  autoreconf -fi

  ./configure --prefix=/usr --sysconfdir=/etc
  make
}

package() {
  cd "${srcdir}/nemo-extensions-${pkgver}/${pkgname}"

  make DESTDIR="${pkgdir}" install

  # install the common license
  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}
