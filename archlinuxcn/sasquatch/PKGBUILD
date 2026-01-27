# Maintainer: Xeonacid <h.dwwwwww@gmail.com>
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Aaron Griffin <aaron@archlinux.org>
# Original TU: Jeff Mickey <j@codemac.net>
# Contributor: ciccio.a

pkgname=sasquatch
pkgver=4.5.1_6
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
sha512sums=('a0d7837941b01746146fa5ecb1a854c6462cfaee7f3c78322655185a727f985fc322e022b14fb6930c44520f1b1bd154e901aeaed5c6996181b26bcf37e3b673')

prepare() {
  cd "$srcdir/$pkgname"
  # Fix: signal handlers must be void (*)(int)
  sed -i -E \
    's/^void[[:space:]]+sigwinch_handler\(\)/void sigwinch_handler(int __attribute__((unused)) signum)/' \
    squashfs-tools/unsquashfs.c
  sed -i -E \
    's/^void[[:space:]]+sigalrm_handler\(\)/void sigalrm_handler(int __attribute__((unused)) signum)/' \
    squashfs-tools/unsquashfs.c
}

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
