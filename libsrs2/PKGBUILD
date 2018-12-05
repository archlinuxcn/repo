# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=libsrs2
pkgver=1.0.18
pkgrel=1
pkgdesc='The next generation SRS library'
arch=('i686' 'x86_64')
url='https://www.libsrs2.org/'
license=(GPL2 BSD)
depends=(glibc)
source=("https://www.libsrs2.org/srs/libsrs2-$pkgver.tar.gz")
sha512sums=('b9c189caa227487e90566f65430345f09a3d545fc286a3eb0c445aee3a74905c1a9248ce78b36a7cfb6a2936f6cd1efbe99ba7b8df49a613a81c6435396f5422')

build() {
  cd $pkgname-$pkgver
  ./configure --prefix=/usr
  make
}

package() {
  cd $pkgname-$pkgver
  make DESTDIR="$pkgdir" install
  install -Dm644 LICENSE.GPL-2 LICENSE.BSD -t "$pkgdir"/usr/share/licenses/$pkgname
}
