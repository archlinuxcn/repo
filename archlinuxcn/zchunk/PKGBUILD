# Maintainer: Yurii Kolesnykov <root@yurikoles.com>
# Ex-Maintainer: Nikita Puzyryov <PuzyryovN@gmail.com>
#
# PRs are welcome here: https://github.com/yurikoles-aur/zchunk
#

pkgname=zchunk
pkgver=1.3.0
pkgrel=1
pkgdesc='A file format designed for highly efficient deltas while maintaining good compression'
arch=(x86_64)
url=https://github.com/zchunk/zchunk
license=(BSD)
depends=(libcurl.so zstd)
provides=(libzck.so)
makedepends=(meson)
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('5563baa254b256e30e1fea87f94f53a5cf63a074898644f3f7ae5b58f446db03')

build() {
  arch-meson "${pkgname}-${pkgver}" build
  meson compile -C build
}

check() {
  meson test -C build
}

package() {
  DESTDIR="${pkgdir}" meson install -C build
  install -Dm644 "${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
