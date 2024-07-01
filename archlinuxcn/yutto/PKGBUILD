# Maintainer: Yufan You <ouuansteve at gmail>

pkgname=yutto
pkgver=2.0.0b40
pkgrel=2
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
makedepends=(python-build python-installer python-wheel python-poetry-core)
source=("https://pypi.io/packages/source/${pkgname:0:1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('737de02779de3cd59a5084d263fd8a9e07c7cde23acb5fba6c234b555e16686e')

build() {
    cd "$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
