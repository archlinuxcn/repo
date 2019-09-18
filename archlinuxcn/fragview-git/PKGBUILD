# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: sergej

pkgname=fragview-git
_gitname=fragview
pkgver=0.1.16.gaf55f55
pkgrel=1
pkgdesc="Analyze disk content and files fragmentation by displaying its map"
arch=('i686' 'x86_64')
url="https://github.com/i-rinat/fragview"
license=('MIT')
depends=('gtkmm3')
makedepends=('git' 'boost' 'sqlite' 'cmake')
optdepends=('sqlite: to open fragmentator.db databases created by fragdb')
source=('git://github.com/i-rinat/fragview.git')
md5sums=('SKIP')

pkgver() {
  cd "${_gitname}"
  git describe --always | sed 's|-|.|g' | sed 's|^v||'
}

build() {
  cd "${_gitname}"
  cmake -DCMAKE_INSTALL_PREFIX="/usr" .
  make
}

package() {
  cd "${srcdir}/${_gitname}"
  make DESTDIR="${pkgdir}" install

  # Add documentation file
  install -d "${pkgdir}/usr/share/doc/${pkgname}"
  install -m 0644 -t "${pkgdir}/usr/share/doc/${pkgname}" "README.md"

  # Add license file
  install -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m 0644 -t "${pkgdir}/usr/share/licenses/${pkgname}" "LICENSE.MIT"
}
