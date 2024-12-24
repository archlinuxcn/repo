# Maintainer: Roald Clark <roaldclark@gmail.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

_name=nose-of-yeti
pkgname=python-noseofyeti
pkgver=2.4.9
pkgrel=1
pkgdesc="A custom pyton codec that provides an RSpec style dsl for python"
arch=('any')
url="https://github.com/delfick/${_name}"
license=('MIT')
depends=('python')
makedepends=(
    'python-build'
    'python-hatchling'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
#checkdepends=(
#    'python-alt-pytest-asyncio'
#    'python-pytest'
#    'python-pytest-helpers-namespace'
#)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/release-${pkgver}.tar.gz")
sha256sums=('687f9bd446bf4c027fac7e7ec0f02c26312b7d976802f30cefebb23840243d08')

prepare() {
    cd "${srcdir}/${_name}-release-${pkgver}"
    # https://github.com/delfick/nose-of-yeti/issues/22
    sed -i '/asynctest/d' pyproject.toml
}

build() {
    cd "${srcdir}/${_name}-release-${pkgver}"
    python -m build --wheel --no-isolation
}

#check() {
#    cd "${srcdir}/${_name}-release-${pkgver}"
#    python -m venv --system-site-packages test-env
#    test-env/bin/python -m installer dist/*.whl
#    test-env/bin/python -m pytest -v
#}

package() {
    cd "${srcdir}/${_name}-release-${pkgver}"
    install -Dm0644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
