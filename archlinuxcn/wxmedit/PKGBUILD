# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: codestation <codestation404 at gmail dot com>

pkgname=wxmedit
pkgver=3.2
pkgrel=1
pkgdesc="Cross-platform Text/Hex Editor, a fork of MadEdit with bug fixes and improvements"
arch=("i686" "x86_64")
url="https://wxmedit.github.io/"
license=('GPL')
depends=('curl' 'gcc-libs' 'glib2' 'glibc' 'gtk3' 'hicolor-icon-theme' 'icu' 'wxwidgets-common' 'wxwidgets-gtk3')
makedepends=('boost')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/hltj/wxMEdit/archive/$pkgver.tar.gz")
sha256sums=('d2bdf266125c6df724ec78cb99ef5f043fca28e8e873eac4b49db7b5986c7579')

build() {
  cd "$srcdir/wxMEdit-$pkgver"
  ./configure --prefix=/usr --with-wx-config=/usr/bin/wx-config
  make
}

package() {
  cd "$srcdir/wxMEdit-$pkgver"
  make DESTDIR="${pkgdir}" install
}
