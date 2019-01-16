# Maintainer: Sebastian Lau <lauseb644 _at_ gmail.com>
# Contributor: twa022 <twa022 at gmail dot com>
# Contributor: American_Jesus <american.jesus.pt AT gmail DOT com>

pkgname=nemo-dropbox
pkgver=4.0.0
pkgrel=1
pkgdesc="Dropbox for Linux - Nemo extension"
arch=('x86_64')
url="https://github.com/linuxmint/nemo-extensions"
license=('custom:CC-BY-ND-3' 'GPL')
depends=('nemo>=4.0' 'dropbox' 'polkit')
makedepends=('glib2' 'python-docutils' 'python-gobject')
groups=('nemo-extensions')
source=("nemo-extensions-$pkgver.tar.gz::https://github.com/linuxmint/nemo-extensions/archive/$pkgver.tar.gz"
	"01__Remove-python-dependencies.patch"
        "02__Makefile.patch")
md5sums=('349e8a471944d1bc1fddd7acf49447d9'
         '4e607465244108d0eae5422ed04a7ac1'
         'fb0f04ed594b62bc9bf7256d18a4d6c2')

prepare() {
  cd "${srcdir}/nemo-extensions-${pkgver}/"

  patch -uNp1 < $srcdir/01__Remove-python-dependencies.patch
  patch -uNp1 < $srcdir/02__Makefile.patch

  cd "${pkgname}"
  autoreconf -fi
}

build() {
  cd "${srcdir}/nemo-extensions-${pkgver}/${pkgname}"

  ./configure --prefix=/usr --sysconfdir=/etc
  make
}

package() {
  cd "${srcdir}/nemo-extensions-${pkgver}/${pkgname}"
  make DESTDIR="${pkgdir}" install

  # install the common license
  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"

  cd "${srcdir}/nemo-extensions-${pkgver}/${pkgname}/data/emblems/"
  make DESTDIR="${pkgdir}" install

  cd "${srcdir}/nemo-extensions-${pkgver}/${pkgname}/data/icons/"
  make DESTDIR="${pkgdir}" install
}
