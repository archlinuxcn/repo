# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Thomas Weißschuh <thomas t-8ch de>

pkgname=logcat-color3
pkgver=0.10.0
# curl https://api.github.com/repos/yan12125/logcat-color3/git/ref/tags/v$pkgver | jq -r .object.sha
_tag=ee5c73183b4ab58e0103bddbe1119632ce43e500
pkgrel=1
pkgdesc='A colorful and highly configurable alternative to the standard "adb logcat" command from the Android SDK'
arch=(any)
url='https://github.com/yan12125/logcat-color3'
license=(Apache)
depends=(python python-colorama)
makedepends=(git python-build python-installer python-setuptools python-setuptools-scm python-wheel)
conflicts=(logcat-color)
source=("git+https://github.com/yan12125/logcat-color3?signed#tag=$_tag")
sha256sums=('SKIP')
validpgpkeys=(
  'E62545315B012B69C8C94A1D56EC201BFC794362'  # Chih-Hsuan Yen <yan12125@archlinux.org>
)

pkgver() {
  cd logcat-color3
  git describe --tags | sed 's/^v//'
}

build() {
  cd logcat-color3
  python -m build --wheel --no-isolation
}

check() {
  cd logcat-color3
  python -m unittest discover ./test
}

package() {
  cd logcat-color3
  python -m installer --destdir="$pkgdir" dist/*.whl
}
