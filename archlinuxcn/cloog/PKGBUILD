# Maintainer: Aaron Fischer <mail@aaron-fischer.net>
# Contributor: Allan McRae <allan@archlinux.org>

pkgname=cloog
pkgver=0.20.0
pkgrel=1
pkgdesc="Library that generates loops for scanning polyhedra"
arch=('i686' 'x86_64' 'armv7h')
url="http://www.bastoul.net/cloog/"
license=('GPL')
depends=('osl' 'isl')
makedepends=('texlive-core' 'texlive-bin')
source=(https://github.com/periscop/cloog/releases/download/$pkgname-$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('d00cbefd348b45d9d482320a088f7ae736440046b99469cbdfbb177a38dcef182c3305f0a567a1f5699c23b7108db6fd5ad6dfbc071d63ccca1d6bfc1b198565')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --prefix=/usr --with-isl=system --with-osl=system
  make
}

check() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  # There are certain race conditions on running the tests, so we restrict
  # it to one job (one CPU core).

  make -j1 check
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR=$pkgdir/ install
}
