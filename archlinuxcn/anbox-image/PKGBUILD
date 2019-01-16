# Maintainer: Iwan Timmer <irtimmer@gmail.com>

pkgname=anbox-image
pkgver=2018.07.19
pkgrel=1
epoch=1
pkgdesc="Android image for running in Anbox"
arch=('x86_64')
url="http://anbox.io/"
license=('custom')
source=("http://build.anbox.io/android-images/${pkgver//./\/}/android_amd64.img")
sha256sums=('6b04cd33d157814deaf92dccf8a23da4dc00b05ca6ce982a03830381896a8cca')

package() {
  install -Dm 644 $srcdir/android_amd64.img $pkgdir/var/lib/anbox/android.img
}
