# Maintainer: Iwan Timmer <irtimmer@gmail.com>

pkgname=anbox-image
pkgver=2018.06.12
pkgrel=1
epoch=1
pkgdesc="Android image for running in Anbox"
arch=('x86_64')
url="http://anbox.io/"
license=('custom')
source=("http://build.anbox.io/android-images/${pkgver//./\/}/android_amd64.img")
sha256sums=('5c4b8f7caeaf604770e37a29b65c7711b26d009a548b4fac8dfb77585e56dc73')

package() {
  install -Dm 644 $srcdir/android_amd64.img $pkgdir/var/lib/anbox/android.img
}
