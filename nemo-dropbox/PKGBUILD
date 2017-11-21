# Maintainer: Sebastian Lau <lauseb644 _at_ gmail.com>
# Contributor: twa022 <twa022 at gmail dot com>
# Contributor: American_Jesus <american.jesus.pt AT gmail DOT com>

pkgname=nemo-dropbox
pkgver=3.6.0
pkgrel=1
pkgdesc="Dropbox for Linux - Nemo extension"
arch=('i686' 'x86_64')
url="https://github.com/linuxmint/nemo-extensions"
license=('custom:CC-BY-ND-3' 'GPL')
depends=('nemo>=3.2' 'dropbox')
makedepends=('glib2')
install=${pkgname}.install
options=('!libtool' '!emptydirs')

source=("nemo-extensions-$pkgver.tar.gz::https://github.com/linuxmint/nemo-extensions/archive/$pkgver.tar.gz"
	      "01-Remove-python-dependencies.patch"
        "02-Makefile.patch")
md5sums=('9cb93de02de5fbea0aa9fe3114c551ee'
         '4e607465244108d0eae5422ed04a7ac1'
         'fb0f04ed594b62bc9bf7256d18a4d6c2')

prepare() {
  cd "${srcdir}/nemo-extensions-${pkgver}/${pkgname}"
  patch -uNp2 -r- -i ../../01-Remove-python-dependencies.patch
  patch -uNp2 -r- -i ../../02-Makefile.patch
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
