# Maintainer: Yufan You <ouuansteve at gmail>

pkgname=yutto
pkgver=2.0.0b42
pkgrel=1
pkgdesc='一个可爱且任性的 B 站视频下载器'
arch=('any')
url='https://github.com/yutto-dev/yutto'
license=('GPL-3.0-only')
depends=(
    'python-aiofiles'
    'python-biliass'
    'python-typing_extensions'
    'python-dict2xml'
    'python-httpx'
    'python-h2'
    'python-socksio'
    'ffmpeg'
)
makedepends=(python-build python-installer python-wheel python-hatchling)
source=("https://pypi.io/packages/source/${pkgname:0:1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('7d27977e93ab984a70ddca2fde9e0085be27a8ad0ec5b42d3b8a483468be2b00')

build() {
    cd "$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
