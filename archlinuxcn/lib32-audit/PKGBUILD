# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Maintainer: David Runge <dvzrv@archlinux.org>
# Contributor: Christian Rebischke <Chris.Rebischke@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: <kang@insecure.ws>
# Contributor: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>
# Contributor: Connor Behan <connor.behan@gmail.com>
# Contributor: henning mueller <henning@orgizm.net>

pkgname=lib32-audit
_name=audit-userspace
pkgver=4.2.1
pkgrel=2
pkgdesc='Userspace components of the audit framework'
url="https://github.com/linux-audit/audit-userspace"
arch=(x86_64)
license=(
  GPL-2.0-or-later
  LGPL-2.0-or-later
)
depends=(
  audit=$pkgver
  lib32-glibc
)
provides=(
  libaudit.so
)
source=(
  $url/archive/v$pkgver/$_name-v$pkgver.tar.gz
)
sha512sums=('71c4ac50b471138da866a82a0fa45970cf26181962f005ae570bdbb76e7cd15b66f8ebeba75a075bf04e52b20d039f012e2bbf8b1055f44641c36897f132894d')
b2sums=('7642a3be30b65ee9fbc10f0929592a0dccd8ef4aca67a237983b5ee644c52d5def62a84161184eae1f9d5741355314d799f39a39b149ae451026f0274c0b9c51')

prepare() {
  cd $_name-$pkgver
  autoreconf -fiv
}

build() {
  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  local configure_options=(
    --disable-zos-remote
    --libdir=/usr/lib32
    --libexecdir=/usr/lib32/audit
    --prefix=/usr
    --runstatedir=/run
    --sbindir=/usr/bin
    --sysconfdir=/etc
    --with-python3=no
  )

  cd $_name-$pkgver
  ./configure "${configure_options[@]}"
  # prevent excessive overlinking due to libtool
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make -C common
  make -C lib
}

package() {
  make DESTDIR="$pkgdir" install -C $_name-$pkgver/lib
  install -vDm 644 $_name-$pkgver/{{README,SECURITY}.md,ChangeLog} -t "$pkgdir/usr/share/doc/$pkgname/"

  rm -r "$pkgdir"/usr/{include,share}
}
