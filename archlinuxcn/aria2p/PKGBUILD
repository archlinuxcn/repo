# Maintainer: Filipe Nascimento <flipee at tuta dot io>

pkgname=aria2p
pkgver=0.12.0
pkgrel=1
pkgdesc="Command-line tool and library to interact with an aria2c daemon process with JSON-RPC"
arch=('any')
url="https://pawamoy.github.io/showcase/aria2p"
license=('ISC')
depends=('python-appdirs' 'python-loguru' 'python-requests' 'python-websocket-client' )
makedepends=('python-build' 'python-installer' 'python-pdm-backend')
optdepends=('aria2: aria2c daemon'
            'python-asciimatics: interactive interface support'
            'python-pyperclip: interactive interface support')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('ac42d2b67b819994df75c79be461ee6adf71be8616105275bce7e8794372c0b7')

build() {
    cd $pkgname-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $pkgname-$pkgver
    python -m installer --destdir="${pkgdir}" dist/*.whl
    chmod +x "${pkgdir}"/usr/bin/*
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
