# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Sven-Hendrik Haase <svenstaro@archlinux.org>
# Contributor: Christian Hesse <mail@eworm.de>
# Contributor: Bill Fraser <wfraser@codewise.org>
# Contributor: Thomas Bächler <thomas@archlinux.org>

pkgname=lib32-libpcap
_name=${pkgname/*-/}
pkgver=1.10.7
pkgrel=1
pkgdesc="A system-independent interface for user-level packet capture (32-bit)"
arch=(x86_64)
url="http://www.tcpdump.org/"
_url=https://github.com/the-tcpdump-group/libpcap
license=(BSD-3-Clause)
depends=(
  lib32-glibc
  lib32-libnl
  $_name=$pkgver
)
makedepends=(
  bluez-libs
  git
  lib32-dbus
)
provides=(libpcap.so)
options=(!staticlibs)
source=(git+$_url?signed#tag=$_name-$pkgver)
sha512sums=('c89694cc2b5eb2ff3402f153ebaa917118789c4c251e8705ce2bb093fce9728edd7d31de0593209285fe9559c3f532609019e6a2e7c1f4bf5a80478903570b50')
b2sums=('7eae899ef89317bc43df4dc31e1d56e95feb064aa7ce3f26224aa1f79d1bf49bf54e7b3560be880046e610e291a349c5a9d84536ff4b3a5a9f774d69c9e3660e')
validpgpkeys=('1F166A5742ABB9E0249A8D30E089DEF1D9C15D0D') # The Tcpdump Group (Package signing key) <release@tcpdump.org>

prepare() {
  cd $_name
  autoreconf -fiv
}

build() {
  local configure_options=(
    --prefix=/usr
    --libdir=/usr/lib32
    --enable-ipv6
    --enable-bluetooth
    --enable-usb
    --with-libnl
  )
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  cd $_name
  ./configure "${configure_options[@]}"
  make
}

package() {
  depends+=(
    lib32-dbus libdbus-1.so
  )

  cd $_name

  make DESTDIR="$pkgdir" install

  # remove files provided by libpcap
  rm -rf "$pkgdir/usr/"{include,share,bin}

  install -vDm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
  install -vDm 644 {CHANGES,{CONTRIBUTING,README}.md} -t "$pkgdir/usr/share/doc/$pkgname/"
}
