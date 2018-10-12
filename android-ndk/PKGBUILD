# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Contributor: Alexander F Rødseth <xyproto@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: frownlee <florez.brownlee@gmail.com>

pkgname=android-ndk
pkgver=r18.b
pkgrel=1
pkgdesc='Android C/C++ developer kit'
arch=('x86_64')
url='https://developer.android.com/ndk/'
license=('GPL' 'LGPL' 'custom')
options=('!strip' 'staticlibs')
backup=('etc/profile.d/android-ndk.sh')
install="$pkgname.install"
replaces=('android-ndk64')
depends=('glibc')
source=('android-ndk.sh')
source_x86_64=("https://dl.google.com/android/repository/$pkgname-${pkgver/./}-linux-x86_64.zip")
sha1sums=('2479a8d74428eb651ad2b9772ad655d7a90af410')
sha1sums_x86_64=('500679655da3a86aecf67007e8ab230ea9b4dd7b')

package() {
  install -Ddm755 "$pkgdir/opt"
  mv "$pkgname-${pkgver/./}" "$pkgdir/opt/$pkgname"

  install -Dm755 android-ndk.sh "$pkgdir/etc/profile.d/android-ndk.sh"
}

# vim: ts=2 sw=2 et:
