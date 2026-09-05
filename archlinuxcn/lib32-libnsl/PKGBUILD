# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Maintainer: David Runge <dvzrv@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>

_name=libnsl
pkgname=lib32-libnsl
pkgver=2.0.1
pkgrel=2
pkgdesc='Public client interface library for NIS(YP)'
arch=(x86_64)
url=https://github.com/thkukuk/libnsl
license=(LGPL-2.1-only)
depends=(
  lib32-glibc
  lib32-libtirpc
  "libnsl=${pkgver}"
)
provides=(libnsl.so)
source=($url/archive/v$pkgver/$_name-v$pkgver.tar.gz)
sha512sums=('1d9290c3123c0933f156808c388654698f7d6994c625cbbc492cc07d656b996c62847048b14b93b8eda632945096ace418a3418ee1f40ff2cc748a3278f987a4')
b2sums=('6988399a5c0f0dab89a47a026e8717f4a3276b0af7c7c507e7bcf1093951a258b54e84e09a679ff4e426ecffbcbb682c31ca393bde6cd92708e07d4709c203aa')

prepare() {
  cd $_name-$pkgver
  autoreconf -fiv
}

build() {
  local configure_options=(
    --prefix=/usr
    --libdir=/usr/lib32
    --disable-static
  )

  cd $_name-$pkgver

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkg-config'

  ./configure "${configure_options[@]}"
  make
}

package() {
  make DESTDIR="$pkgdir" install -C $_name-$pkgver
  rm -rf "$pkgdir"/usr/include
}

# vim: ts=2 sw=2 et:
