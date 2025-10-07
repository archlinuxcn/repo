# Maintainer: saitewasreset <saiteTimedOut at outlook dot com>
# Maintainer: DeepChirp <DeepChirp@outlook.com>

pkgname=sping
pkgver=0.3.0
pkgrel=2
pkgdesc='Modern terminal HTTP/TCP latency monitoring tool with real-time visualization.'
arch=(any)
url="https://gitlab.com/dseltzer/sping"
license=('MIT')
depends=('python>=3.9' 'python-typer>=0.9.0' 'python-httpx>=0.27.0' 'python-rich>=13.0.0')
makedepends=('python-build' 'python-installer' 'python-hatchling>=1.18.0')
checkdepends=('python-pytest>=7.0.0' 'python-pytest-asyncio>=0.21.0' 'python-httpx>=0.27.0')
source=(
    "${pkgname}-${pkgver}.tar.gz::${url}/-/archive/${pkgver}/sping-${pkgver}.tar.gz"
    "MIT.txt"
)
sha256sums=('e94e2cf147a75070a4a0109c832cf13b863fb96ae8dacd9617a538ee2c04b81c'
            'bdc505697cc896eb784e38217b8d63d6dc19488c91060a391e1c1cc213cf033d')

build() {
  cd "${pkgname}-${pkgver}"

  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}-${pkgver}"

  python -m installer --destdir="${pkgdir}" dist/*.whl

  install -Dm644 "${srcdir}/MIT.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

check(){
    cd "${pkgname}-${pkgver}"

    PYTHONPATH="." pytest
}
