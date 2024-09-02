# Maintainer: Carl George < arch at cgtx dot us >
# Contributor: Erik Johnson <palehose at gmail dot com>
# Contributor: <kwrazi at gmail dot com>

pkgbase="ptpython"
pkgname="ptpython"
pkgver="3.0.29"
pkgrel="1"
pkgdesc="Python REPL build on top of prompt_toolkit"
arch=("any")
url="https://github.com/prompt-toolkit/ptpython"
license=("BSD")
makedepends=("python-setuptools")
depends=(
    "python-jedi>=0.9.0"
    "python-prompt_toolkit>=3.0.3"
    "python-pygments"
    "python-black"
    "python-appdirs"
)
optdepends=(
    "ipython: ptipython (ptpython + ipython)"
)
provides=("ptpython3")
source=("${pkgbase}-${pkgver}.tar.gz::https://github.com/prompt-toolkit/ptpython/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('168bdc7fb74cdc2e9f6410cbde8c7ca7c23702796d9a931f6cc9a05badc82c7b')

prepare() {
    cp -a "${srcdir}/${pkgbase}-${pkgver}" "${srcdir}/${pkgbase}2-${pkgver}"
}

build() {
    cd "${srcdir}/${pkgbase}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${pkgbase}-${pkgver}"
    python setup.py install --skip-build --root="${pkgdir}" --optimize=1
    install -D --mode 644 --target-directory "$pkgdir/usr/share/licenses/$pkgname" LICENSE
}
