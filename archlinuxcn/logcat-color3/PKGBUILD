# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Thomas Weißschuh <thomas t-8ch de>

pkgname=logcat-color3
pkgver=0.9.0
pkgrel=3
pkgdesc='A colorful and highly configurable alternative to the standard "adb logcat" command from the Android SDK'
arch=(any)
url='https://github.com/yan12125/logcat-color3'
license=(Apache)
depends=(python-colorama)
makedepends=(python-setuptools-scm)
conflicts=(logcat-color)
source=("https://files.pythonhosted.org/packages/source/l/logcat-color3/logcat-color3-$pkgver.tar.gz"{,.asc})
sha256sums=('57471841b59d0a456f6d3a971bb3701ca2fc9a8319735e9515c9de3cd2062c92'
            'SKIP')
validpgpkeys=(
  '481C4474AF1572165AE4C6AF3FDDD575826C5C30'  # Chih-Hsuan Yen <yan12125@gmail.com>
)

build() {
  cd logcat-color3-$pkgver
  python setup.py build
}

check() {
  cd logcat-color3-$pkgver
  python test/test.py
}

package() {
  cd logcat-color3-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
