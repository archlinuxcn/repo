# Maintainer: Felix Yan <felixonmars@archlinux.org>

_pkgname=jieba
pkgname=python2-$_pkgname
pkgver=0.36.2
pkgrel=1
pkgdesc="JieBa Chinese Words Segment Library based on HMM model for Python"
arch=('any')
url='https://github.com/fxsjy/jieba'
license=('MIT')
depends=('python2')
source=("http://pypi.python.org/packages/source/j/$_pkgname/$_pkgname-$pkgver.zip")

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python2 setup.py install -O1 --root="$pkgdir"
}

sha512sums=('3714d91222c610a18b004eedb1a3b706509e31540bb7a4092d529fd99acb9ba1a83abce9c5aa24c1d726a385b3f92fbc19fb4d344f24c7be928ae68afed09642')
