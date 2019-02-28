# Maintainer: Rhinoceros <https://aur.archlinux.org/account/rhinoceros>
# Contributor: Rhinoceros <https://aur.archlinux.org/account/rhinoceros>

pkgname=sc-im
pkgver=0.7.0
pkgrel=2
pkgdesc='A spreadsheet program based on SC'
arch=('i686' 'x86_64' 'armv7h')
url='https://github.com/andmarti1424/sc-im'
depends=(libxml2 libzip)
optdepends=('libxlsxwriter: export to xlsx. Requires rebuild of sc-im')
license=('BSD')
conflicts=('scim-spreadsheet' 'sc-im-git')
source=("https://github.com/andmarti1424/$pkgname/archive/v${pkgver}.tar.gz"
        'arch.patch'
        'https://patch-diff.githubusercontent.com/raw/andmarti1424/sc-im/pull/258.patch')
sha256sums=('87225918cb6f52bbc068ee6b12eaf176c7c55ba9739b29ca08cb9b6699141cad'
            '1fcd263a13224fe2c18991852d31c2cc264c7d627578cbae348a9291dd38dede'
            '4a56da6b1fd7276e65ca1e6faf3adcafecee40172622a9ebc2ea0a162cf89f7b')
MAKEFLAGS='-j1'

prepare() {
  cd "$pkgname-$pkgver/src"
  # install things in the correct place for package managers
  patch <"$srcdir/arch.patch"
  cd ..
  patch -p1 <"$srcdir/258.patch"
}

build() {
  cd "$pkgname-$pkgver/src"
  make
}

package() {
  cd "$pkgname-$pkgver/src"
  make DESTDIR="$pkgdir" install

  install -D -m644 ../LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
