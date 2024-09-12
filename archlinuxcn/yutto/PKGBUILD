# Maintainer: Yufan You <ouuansteve at gmail>

pkgname=yutto
pkgver=2.0.0b41
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
makedepends=(python-build python-installer python-wheel python-hatchling)
source=("https://pypi.io/packages/source/${pkgname:0:1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('55e204f723c3253b8aae409b4232cac41dced7635b1843ccf4f86ae0121fcfb9')

build() {
    cd "$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
