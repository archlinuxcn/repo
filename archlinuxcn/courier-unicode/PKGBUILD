# Maintainer: Neil Romig <neilromig@gmail.com>
# Contributor: Robert Knauer <robert@capsaicin-dev.de>

pkgname=courier-unicode
pkgver=2.2.5
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
  '5f42cbaec318ad69366745c9409025c7e0eb8692e887a8382e46b9767b8b98b8'
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
