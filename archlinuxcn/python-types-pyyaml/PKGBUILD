# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Achmad Fathoni<fathoni.id(at)gmail.com>

pkgname=python-types-pyyaml
pkgver=6.0.12.20260906
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
sha512sums=('c8eced042846ed679e21a95811a9738a0763246c3e8b88d9859a263bc2d8f5796f71cb0a6a8b0d6b210721d2e6ac7f561c7da556a204a5c87f4066a981db7f0a')

build() {
    cd ${__name}-${pkgver}
    python -m build --wheel --no-isolation
}

package() {
    cd ${__name}-${pkgver}
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
