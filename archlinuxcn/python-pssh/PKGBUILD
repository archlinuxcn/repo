# Maintainer:  Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
# Contributor: Boris Momcilovic <boris.momcilovic@gmail.com>
# Contributor: Jaroslav Lichtblau <svetlemodry@archlinux.org>
# Contributor: Elis Hughes <elishughes@googlemail.com>
# Contributor: Mark Blakeney at bullet-systems dot net

pkgname=python-pssh
pkgver=2.3.5
pkgrel=13
pkgdesc="Parallel versions of the openssh tools ssh, scp, rsync, nuke, slurp"
arch=('any')
url="https://github.com/lilydjwg/pssh"
license=('BSD')
depends=('openssh' 'python')
makedepends=('python-setuptools' 'python-build' 'python-installer' 'python-wheel')
changelog=$pkgname.changelog
source=(https://github.com/lilydjwg/pssh/archive/refs/tags/v${pkgver}.tar.gz)
sha256sums=('97277f9d08b512c6a1b6dc5eac9677f34038096bae24484452d326137ba0d080')

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
