# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Thomas Weißschuh <thomas t-8ch de>

pkgname=logcat-color3
pkgver=0.9.2
pkgrel=1
pkgdesc='A colorful and highly configurable alternative to the standard "adb logcat" command from the Android SDK'
arch=(any)
url='https://github.com/yan12125/logcat-color3'
license=(Apache)
depends=(python python-colorama)
makedepends=(python-setuptools-scm python-wheel)
conflicts=(logcat-color)
source=("https://files.pythonhosted.org/packages/source/l/logcat-color3/logcat-color3-$pkgver.tar.gz"{,.asc})
sha256sums=('a1da09de689470c323576014e7644f4987e7866846d1a785b53eab2a324dcb40'
            'SKIP')
validpgpkeys=(
  'E62545315B012B69C8C94A1D56EC201BFC794362'  # Chih-Hsuan Yen <yan12125@archlinux.org>
)

build() {
  cd logcat-color3-$pkgver
  python setup.py build
}

check() {
  cd logcat-color3-$pkgver
  python -m unittest discover ./test
}

package() {
  cd logcat-color3-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
