# Maintainer: taotieren <admin@taotieren.com>

pkgname=python-cmsis-svd-git
pkgver=0.5.r14.g4a23b3b
pkgrel=1
pkgdesc='Aggegration of ARM Cortex-M (and other) CMSIS SVDs and related tools'
url='https://github.com/cmsis-svd/cmsis-svd'
license=('Apache-2.0')
arch=(any)
depends=(python
    python-lxml
    python-six)
# checkdepends=(python-pytest
#     python-nose2
#     python-pytest-subtests)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
    git)
provides=("${pkgname%-git}" "cmsis-svd")
conflicts=("${pkgname%-git}" "cmsis-svd")
source=("$pkgname::git+$url.git")
sha256sums=('SKIP')

pkgver() {
    cd "${srcdir}/$pkgname/python"
    git describe --long --tags | sed 's/^python-//g;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
    git -C "${srcdir}/${pkgname}" clean -dfx
}

build() {
    cd "${srcdir}/$pkgname/python"
    python -m build --wheel --no-isolation
}

# check() {
#     cd "${srcdir}/$pkgname/python"
#     PYTHONPATH=build pytest build/lib
# }

package() {
    cd "${srcdir}/$pkgname/python"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
