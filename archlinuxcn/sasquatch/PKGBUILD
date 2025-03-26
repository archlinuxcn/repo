# Maintainer: Xeonacid <h.dwwwwww@gmail.com>
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Aaron Griffin <aaron@archlinux.org>
# Original TU: Jeff Mickey <j@codemac.net>
# Contributor: ciccio.a

pkgname=sasquatch
pkgver=4.5.1_5
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
sha512sums=('cf54ad00877e706e3646e7b502a7c0570e932dd3f82fa98257b48f98ee27df55f8e73e9582a3b3a449d954e8990acdcdbc80cfcc65cb394dba0c773c86db4996')

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
