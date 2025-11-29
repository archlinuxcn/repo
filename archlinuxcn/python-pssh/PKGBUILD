# Maintainer:  Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
# Contributor: Boris Momcilovic <boris.momcilovic@gmail.com>
# Contributor: Jaroslav Lichtblau <svetlemodry@archlinux.org>
# Contributor: Elis Hughes <elishughes@googlemail.com>
# Contributor: Mark Blakeney at bullet-systems dot net

pkgname=python-pssh
pkgver=2.3.6
pkgrel=13
pkgdesc="Parallel versions of the openssh tools ssh, scp, rsync, nuke, slurp"
arch=('any')
url="https://github.com/lilydjwg/pssh"
license=('BSD')
depends=('openssh' 'python')
makedepends=('python-setuptools' 'python-build' 'python-installer' 'python-wheel')
changelog=$pkgname.changelog
source=(https://github.com/lilydjwg/pssh/archive/refs/tags/v${pkgver}.tar.gz)
sha256sums=('dfe1b898e483377213b44b8316a81fd6e1bbe427e1607e76be18366071c04c85')

build() {
  cd "${srcdir}"/pssh-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}"/pssh-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl

# fix putty pscp file conflict
  mv "${pkgdir}"/usr/bin/pscp "${pkgdir}"/usr/bin/psshscp

# license
  install -Dm644 COPYING "${pkgdir}"/usr/share/licenses/$pkgname/COPYING
}
