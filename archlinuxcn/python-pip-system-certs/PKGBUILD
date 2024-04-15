# Maintainer: Fabian Maurer<dark.shadow4@web.de>

pkgname=python-pip-system-certs
pkgver=4.0
pkgrel=3
pkgdesc="Patches pip and requests at runtime to use certificates from the default system store"
arch=('any')
license=('BSD')
url="https://gitlab.com/alelec/pip-system-certs"
depends=('python3' 'python-wrapt')
makedepends=(python-build python-installer python-wheel python-git-versioner)
source=("https://gitlab.com/alelec/pip-system-certs/-/archive/v4.0/pip-system-certs-v$pkgver.tar.gz")
sha512sums=('6c583e0f8b61a774a78e0f561aa95717ed3e5735268bdd6a2767f0803697a3f7a64d132c9d1d5947a2bf06c220b9da4a10d4c31e8e523605422c4cbb7935a294')

build() {
    export SETUPTOOLS_SCM_PRETEND_VERSION=$pgkver
    cd pip-system-certs-v$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd pip-system-certs-v$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
