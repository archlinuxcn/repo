# Maintainer: Mildred Ki'Lya <mildred-nospam.at.mildred.fr>
pkgname=rnc2rng
pkgver=2.6.6
pkgrel=1
pkgdesc="Convert compact form Relac-NG schemas (rnc) to XML (rng)"
url="https://github.com/djc/rnc2rng"
arch=('any')
license=('custom:public domain')
depends=('python' 'python-rply')
optdepends=()
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
conflicts=()
replaces=()
backup=()
install=
source=("https://github.com/djc/${pkgname}/archive/${pkgver}.tar.gz")
md5sums=('92cb92e41803db3d2489ccda7baadbfd')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}/" dist/*.whl
  install -Dm644 setup.py "$pkgdir/usr/share/licenses/$pkgname/COPYING"
  install -Dm644 README.rst "$pkgdir/usr/share/doc/$pkgname/README.rst"
}

# vim:set ts=2 sw=2 et:

