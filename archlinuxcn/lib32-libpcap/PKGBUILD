# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Sven-Hendrik Haase <svenstaro@archlinux.org>
# Contributor: Christian Hesse <mail@eworm.de>
# Contributor: Bill Fraser <wfraser@codewise.org>
# Contributor: Thomas Bächler <thomas@archlinux.org>

pkgname=lib32-libpcap
_name=${pkgname/*-/}
pkgver=1.11.0
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
sha512sums=('a946f5663cd04152f6f2f98051bc8d077b3fb00a47d4fcc508c7bf25ac0fa6ffffeb5110e027cdebc28ed8e2091f2efe8a49383f4807d375e6dd80f540920d4a')
b2sums=('fbc2024e40bb19c82f92b03de3a3007b477a9504aa05f62ab0046500384eb5d273b13c1c486fabb12dd0d2cfa2b6d70bf616409515ff0bd66c52b3580b2e485b')
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
