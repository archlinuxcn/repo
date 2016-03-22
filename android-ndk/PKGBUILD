# Maintainer: Alexander F Rødseth <xyproto@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: frownlee <florez.brownlee@gmail.com>

pkgname=android-ndk
pkgver=r11
pkgrel=2
pkgdesc='Android C/C++ developer kit'
arch=('x86_64')
url='https://developer.android.com/ndk/'
license=('GPL' 'LGPL' 'custom')
options=('!strip' 'staticlibs')
backup=('etc/profile.d/android-ndk.sh')
install="$pkgname.install"
provides=('android-ndk')
replaces=('android-ndk64')
depends=('ncurses5-compat-libs' 'libtinfo')
source=('android-ndk.sh' "http://dl.google.com/android/repository/${pkgname}-$pkgver-linux-x86_64.zip")
sha256sums=('5bc58ccd7e7de03c9656ca8f13fb9bf9dff2eeee31a2670ce04a4b97be73dc95'
            '59ab44f7ee6201df4381844736fdc456134c7f7660151003944a3017a0dcce97')

package() {
  install -d "$pkgdir/opt"
  mv "$pkgname-$pkgver" "$pkgdir/opt/$pkgname"

  install -Dm755 android-ndk.sh "$pkgdir/etc/profile.d/android-ndk.sh"

  # Fix broken permissions
  chmod -R o=g "$pkgdir/opt/$pkgname"
  find "$pkgdir/opt/$pkgname" -perm 744 -exec chmod 755 {} +
}

# vim:set ts=2 sw=2 et:
