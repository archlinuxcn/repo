# Maintainer: gmes78 <gmes.078 at gmail dot com>

pkgname=python-qasync
pkgver=0.9.4
pkgrel=1
pkgdesc="Python library for using asyncio in Qt-based applications"
arch=(any)
url="https://github.com/CabbageDevelopment/qasync"
license=("BSD")

depends=("python")
makedepends=("python-setuptools")
optdepends=("python-pyqt5: PyQt5 support"
            "pyside2: PySide2 support")

source=("https://github.com/CabbageDevelopment/qasync/archive/v${pkgver}.tar.gz")
sha512sums=("90150364c838c3de760238ef8e7052c428cfd3167e39ec4f3e4d1ecff69b66c0c12130e73ed478148bbe388507fd405e2f83f7f54c05411361bf4ed8231cc2b1")

package() {
    cd qasync-${pkgver}
    python setup.py install --root="$pkgdir/" --optimize=1
    install -m644 -D LICENSE "$pkgdir/usr/share/licenses/$pkgname"
}
