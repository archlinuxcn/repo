# Maintainer: Marcin Mielniczuk <marmistrz dot dev at zoho dot eu>

pkgname=ibus-libzhuyin
pkgver=1.10.0
pkgrel=1
pkgdesc="New Zhuyin engine based on libzhuyin for IBus"
arch=('x86_64')
license=('GPL2')
url="https://github.com/libzhuyin/ibus-libzhuyin"
# libpinyin provides both libpinyin.so and libzhuyin.so
depends=('ibus' 'opencc' 'python-xdg' 'libpinyin')
makedepends=('git' 'intltool' 'gnome-common' 'wget')
source=("$pkgname-$pkgver.tar.gz::https://github.com/libzhuyin/ibus-libzhuyin/archive/$pkgver.tar.gz")
sha512sums=('9b37b02ebaeb1f3e67eabc6b04d7f68ed5dad4c44097c585eebc48d4245ef3f39ab65cc57e374a07eddd74d83fa87a42ca7a2c138994ba0d9fa27748c29fb380')

build() {
  cd $pkgname-$pkgver
  ./autogen.sh --prefix=/usr --libexecdir=/usr/lib/$pkgname --enable-opencc
  make
}

package() {
  cd $pkgname-$pkgver
  make NO_INDEX=true DESTDIR="$pkgdir" install
}
