# Maintainer: Pierre Carru <pierre@carru.fr>
# based on dstat package

pkgname=dool-git
_pkgname=dool
pkgver=1.0.0.r1.g34a3244
pkgrel=1
pkgdesc="A versatile resource statistics tool"
arch=('any')
url="https://github.com/scottchiefbaker/dool"
license=('GPL')
depends=('python' 'python-six')
provides=('dool')
conflicts=('dool')
#source=(https://github.com/scottchiefbaker/dool/archive/master.tar.gz)
#sha512sums=(SKIP)
source=("${pkgname%-*}::git+https://github.com/scottchiefbaker/dool.git")
sha512sums=(SKIP)

pkgver() {
  cd "$_pkgname"
  git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

package() {
  cd "$_pkgname"

  make DESTDIR="$pkgdir" install
}
