# $Id: PKGBUILD 226630 2017-05-03 13:48:02Z spupykin $
# Maintainer: Geballin - Guillaume Ballin <macniaque at free dot fr>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Alessio 'mOLOk' Bolognino <themolok@gmail.com>

pkgname=bwidget
pkgver=1.9.14
pkgrel=1
pkgdesc="A suite of megawidgets for Tk"
arch=('any')
url="https://wiki.tcl.tk/2251"
license=('GPL')
depends=('bash' 'tcl')
source=("http://downloads.sourceforge.net/project/tcllib/BWidget/$pkgver/bwidget-$pkgver.tar.gz")
sha256sums=('531a6ecfa33114471dd58b0bedd5f9ff6f311c792fc1a030d8e454c5ebb5d44e')

package() {
  cd "${srcdir}"
  install -d "${pkgdir}"/usr/lib/tcl8.6
  cp -r bwidget-$pkgver "${pkgdir}"/usr/lib/tcl8.6/
}
