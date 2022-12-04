# Maintainer: Neil Romig <neilromig@gmail.com>
# Contributor: Robert Knauer <robert@capsaicin-dev.de>

pkgname=courier-unicode
pkgver=2.2.6
pkgrel=1
pkgdesc="Courier Unicode Library"
arch=("i686" "x86_64" "aarch64")
url="http://www.courier-mta.org/unicode/"
license=('GPL3')
depends=('gcc-libs')
source=(
  "https://sourceforge.net/projects/courier/files/${pkgname}/${pkgver}/${pkgname}-${pkgver}.tar.bz2"
)
sha256sums=(
  '513f68066ed192ace630f601984c565b5c1d1c81d98c6478ebe4edb3a15be03a'
)

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --prefix=/usr
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}/" install
}
