# $Id: PKGBUILD 226630 2017-05-03 13:48:02Z spupykin $
# Maintainer: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Alessio 'mOLOk' Bolognino <themolok@gmail.com>

pkgname=bwidget
pkgver=1.9.13
pkgrel=1
pkgdesc="A suite of megawidgets for Tk"
arch=('any')
url="https://wiki.tcl.tk/2251"
license=('GPL')
depends=('bash' 'tcl')
source=("http://downloads.sourceforge.net/project/tcllib/BWidget/$pkgver/bwidget-$pkgver.tar.gz")
sha256sums=('76d8f42280e7160242186d12437949830eabd5009a6c14f4e7dba0f661403a81')

package() {
  cd "${srcdir}"
  install -d "${pkgdir}"/usr/lib/tcl8.6
  cp -r bwidget-$pkgver "${pkgdir}"/usr/lib/tcl8.6/
}
