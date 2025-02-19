# Maintainer: Yufan You <ouuansteve at gmail>

pkgname=yutto
pkgver=2.0.1
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
    'python-pydantic'
    'ffmpeg'
)
makedepends=(python-build python-installer python-wheel python-hatchling)
source=("https://pypi.io/packages/source/${pkgname:0:1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('c420ddf217aafe0a0f073bdf2a4cd5eccc7e982d52b23038c9ae50268373d579')

build() {
    cd "$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
