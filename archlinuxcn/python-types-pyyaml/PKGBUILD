# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Achmad Fathoni<fathoni.id(at)gmail.com>

pkgname=python-types-pyyaml
pkgver=6.0.12.20260815
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
sha512sums=('564f7a763d4d060c8b0de924456e0ba4f853249acba5e249a689eaff447fbb69443a681df92d3eee8def795842aec3d834a50ee5fded7910c531974ff0910e38')

build() {
    cd ${__name}-${pkgver}
    python -m build --wheel --no-isolation
}

package() {
    cd ${__name}-${pkgver}
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
