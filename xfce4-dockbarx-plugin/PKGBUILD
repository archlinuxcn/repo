# Contributor: twa022 <twa022 at gmail dot com>

pkgname=xfce4-dockbarx-plugin
pkgver=0.3.1
pkgrel=1
pkgdesc="Embed DockbarX in the xfce4-panel"
arch=('i686' 'x86_64')
url="http://xfce-look.org/content/show.php?content=157865"
license=('X11')
depends=('vala' 'dockbarx>=0.91' 'xfce4-panel')
makedepends=('python2')
source=( ${pkgname}-${pkgver}.tar.gz::https://codeload.github.com/TiZ-EX1/${pkgname}/tar.gz/${pkgver} )
sha256sums=('7255fe5c1585d2492b67618d6e3cc1b114b4a19fae2e0e5e639c0d1f414beb9e')

build() {
  cd ${srcdir}/${pkgname}-${pkgver}
  sed -i 's:env python$:&2:' waf wscript
  PREFIX=/usr ./waf configure
  ./waf build
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}
  DESTDIR="${pkgdir}" ./waf install
}

