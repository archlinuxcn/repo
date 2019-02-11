# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

_pkgname=apfsprogs
pkgname=$_pkgname-git
pkgver=r23.0dac1d6
pkgrel=1
pkgdesc='Experimental APFS tools for linux'
arch=(x86_64)
license=(GPL2)
url='https://github.com/eafer/apfsprogs'
depends=('glibc')
makedepends=('git')
conflicts=("$_pkgname")
provides=("$_pkgname=$pkgver")
source=('git+https://github.com/eafer/apfsprogs'
        'add-ldflags.patch')
sha256sums=('SKIP'
            'a47c0056a94cf8bc7bba443e467a1a434356cad71ce0a88be460c727e6aee6c9')

pkgver() {
  cd $_pkgname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd $_pkgname
  patch -Np1 -i ../add-ldflags.patch
}

build() {
  cd $_pkgname/apfsck

  make
}

package() {
  cd $_pkgname/apfsck

  install -Dm755 apfsck -t "$pkgdir"/usr/bin
}
