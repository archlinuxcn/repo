# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Achmad Fathoni<fathoni.id(at)gmail.com>

pkgname=python-types-pyyaml
pkgver=6.0.12.20250516
pkgrel=1
pkgdesc='Typing stubs for PyYAML'
arch=(any)
url='https://pypi.org/project/types-PyYAML'
license=('Apache-2.0')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
_name=${pkgname#python-}
__name=${_name//-/_}
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${__name}/${__name}-$pkgver.tar.gz")
sha512sums=('ecf1e43d80149972857867c1b53a7053f6a61774d7a6e9f285596bd2a55929c454aa4e4ea3f4e7c4769ba1aa32defeb8e0b58f4736f91688caad62d03c5da193')

build() {
    cd ${__name}-${pkgver}
    python -m build --wheel --no-isolation
}

package() {
    cd ${__name}-${pkgver}
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
