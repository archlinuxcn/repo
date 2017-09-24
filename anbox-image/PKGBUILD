# Maintainer: Iwan Timmer <irtimmer@gmail.com>

pkgname=anbox-image
pkgver=3
_pkgdate=2017/07/13
pkgrel=1
epoch=1
pkgdesc="Android image for running in Anbox"
arch=('x86_64')
url="http://anbox.io/"
license=('custom')
source=("http://build.anbox.io/android-images/${_pkgdate}/android_${pkgver}_amd64.img")
sha256sums=('20caeb254d716610bab2c94cd360a92353e48860fdc7cb21c16e0eab74bc42d0')

package() {
  install -Dm 644 $srcdir/android_${pkgver}_amd64.img $pkgdir/var/lib/anbox/android.img
}
