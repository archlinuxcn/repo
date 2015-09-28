# Contributor: twa022 <twa022 at gmail dot com>

pkgname=xfce4-dockbarx-plugin
pkgver=0.4.1
pkgrel=1
pkgdesc="Embed DockbarX in the xfce4-panel"
arch=('i686' 'x86_64')
url="https://github.com/TiZ-EX1/xfce4-dockbarx-plugin"
license=('X11')
depends=('vala' 'dockbarx>=0.91' 'xfce4-panel')
makedepends=('python2')
conflicts=("$pkgname"-git)

source=( ${pkgname}-${pkgver}.tar.gz::https://github.com/TiZ-EX1/${pkgname}/archive/v${pkgver}.tar.gz )
sha256sums=('c55e5231ae8b69ab10c22ab5150e47f5392b2398572e753cbcb1a147362e0ba5')

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

