# Maintainer: Xeonacid <h.dwwwwww@gmail.com>
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Aaron Griffin <aaron@archlinux.org>
# Original TU: Jeff Mickey <j@codemac.net>
# Contributor: ciccio.a

pkgname=sasquatch
pkgver=4.5.1_4
pkgrel=1
pkgdesc='Patches to the standard unsquashfs utility that attempts to add support for many hacked-up vendor-specific SquashFS implementations.'
arch=(x86_64)
url='https://github.com/onekey-sec/sasquatch'
license=(GPL-2.0-or-later)
depends=(
  glibc
  gcc-libs
  lz4
  lzo
  xz
  zlib
  zstd
)
makedepends=(git)
source=(git+$url.git#tag=$pkgname-v${pkgver//_/-})
sha512sums=('2ef501423f06a69938e9cfa21308640008737d6501483c0b5c24efc97554faae6b39b3005f0ae4eceb92ccabeda05040b84dd8f810c8b7b1834143f536a8ba5f')

build() {
  local make_options=(
    GZIP_SUPPORT=1
    LZ4_SUPPORT=1
    LZO_SUPPORT=1
    XATTR_SUPPORT=1
    XZ_SUPPORT=1
    ZSTD_SUPPORT=1
    -C $pkgname/squashfs-tools
  )

  make "${make_options[@]}"
}

package() {
  local make_options=(
    INSTALL_PREFIX="$pkgdir/usr"
    install
    -C $pkgname/squashfs-tools
  )

  make "${make_options[@]}"
  install -vDm 644 $pkgname/{ACTIONS-README,CHANGES,README*,USAGE} -t "$pkgdir/usr/share/doc/$pkgname/"
}
