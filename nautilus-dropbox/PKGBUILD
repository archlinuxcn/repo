# Maintainer: Christophe Gueret <christophe.gueret@gmail.com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>
# Contributor: cmorlok <christianmorlok@web.de>
# Contributor: fazibear <fazibear@gmail.com>
# Contributor: neuromante <lorenzo.nizzi.grifi@gmail.com>
# Contributor: Gordin <9ordin @t gmail.com>

pkgname=nautilus-dropbox
pkgver=2015.02.12
pkgrel=1
pkgdesc="Dropbox for Linux - Nautilus extension"
arch=('i686' 'x86_64')
url="https://www.dropbox.com/"
license=('custom:CC-BY-ND-3' 'GPL')
depends=('libnotify' 'nautilus' 'dropbox' 'hicolor-icon-theme')
makedepends=('python2-docutils' 'python2' 'pygtk' 'pkg-config')
install=${pkgname}.install
options=('!libtool' '!emptydirs')
source=("https://linux.dropbox.com/packages/${pkgname}-${pkgver}.tar.bz2")
md5sums=('bac2adbfc3bbcf1bb1cb28dcc975a090')

build() {
  cd "${pkgname}-${pkgver}/"
  sed -i "s/python/python2/" configure dropbox.in Makefile.in rst2man.py
  ./configure --prefix=/usr --sysconfdir=/etc
  make
}

package() {
  cd "${pkgname}-${pkgver}/"
  make DESTDIR="${pkgdir}" install
  # install the common license
  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
  # remove executables and depend on 'dropbox' package
  rm "${pkgdir}/usr/bin/dropbox"
  rm "${pkgdir}/usr/share/applications/dropbox.desktop"
  rm "${pkgdir}/usr/share/man/man1/dropbox.1"
}
