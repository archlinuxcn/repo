# Maintainer:
# Contributor: Filipe Nascimento <flipee at tuta dot io>

pkgname=aria2p
pkgver=0.12.1
pkgrel=1
pkgdesc="Command-line tool and library to interact with an aria2c daemon process with JSON-RPC"
arch=('any')
url="https://pawamoy.github.io/showcase/aria2p"
license=('ISC')
depends=('python' 'python-loguru' 'python-platformdirs' 'python-requests' 'python-tomli' 'python-websocket-client')
makedepends=('python-build' 'python-installer' 'python-pdm-backend')
optdepends=('aria2: aria2c daemon'
            'python-asciimatics: interactive interface support'
            'python-pyperclip: interactive interface support')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('1521ccba4a4bb164a023f4c4213513dc3e6f47b91927f5e49dd50678da8c1294')

build() {
    cd "${pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${pkgname}-${pkgver}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
