_pkgname='pathvalidate'
pkgname=python-$_pkgname
pkgver=3.2.3
pkgrel=1
pkgdesc='Sanitize/validate strings in filenames/file-paths/etc'
arch=('any')
url='https://github.com/thombashi/pathvalidate'
license=('MIT')
depends=('python' 'python-click')
makedepends=('python-setuptools-scm' 'python-wheel' 'python-installer' 'python-build')
source=("$pkgname-$pkgver.tar.gz::https://github.com/thombashi/pathvalidate/releases/download/v${pkgver}/pathvalidate-${pkgver}.tar.gz")
sha256sums=('59b5b9278e30382d6d213497623043ebe63f10e29055be4419a9c04c721739cb')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dvm644 'README.rst' -t "${pkgdir}/usr/share/doc/${pkgname}"
  install -Dvm644 'LICENSE' -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
