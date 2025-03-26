# Maintainer: Dmytro Meleshko <qzlgeb.zryrfuxb@tznvy.pbz(rot13)>
# Contributor: acxz <akashpatel2008@yahoo.com>

pkgname=python-flake8-quotes
_pkgname=flake8-quotes
pkgver=3.4.0
pkgrel=1
pkgdesc="Flake8 lint for quotes"
arch=('any')
url="https://github.com/zheller/${_pkgname}"
license=('MIT')
depends=('flake8')
checkdepends=('python-pytest')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/zheller/${_pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('3d372716b21b3885a387e7f4fd0669833e0863cf69dd1262db06a58da1ae1417')

build() {
    cd "${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

check() {
    cd "${_pkgname}-${pkgver}"
    python -m pytest -k 'not test_stdin'
}

package() {
    cd "${_pkgname}-${pkgver}"
    python -m installer --destdir="${pkgdir}" dist/*.whl

    install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
