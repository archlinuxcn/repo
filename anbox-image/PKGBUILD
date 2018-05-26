# Maintainer: Iwan Timmer <irtimmer@gmail.com>

pkgname=anbox-image
pkgver=2018.05.23
pkgrel=1
epoch=1
pkgdesc="Android image for running in Anbox"
arch=('x86_64')
url="http://anbox.io/"
license=('custom')
source=("http://build.anbox.io/android-images/${pkgver//./\/}/android_amd64.img")
sha256sums=('cbcb8c4740ed38dbc243122df2d8d87511a9c8dcc162781f2eabb5dc1ea079fe')

package() {
  install -Dm 644 $srcdir/android_amd64.img $pkgdir/var/lib/anbox/android.img
}
