# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgname=piep
pkgdesc='Bringing the power of python to stream editing'
pkgver=0.8.0
_tag=version-$pkgver
pkgrel=1
arch=("any")
url="https://github.com/gfxmonk/piep"
license=("GPL")
makedepends=('python2-setuptools')
depends=('python2' 'python2-pygments')
source=("https://github.com/gfxmonk/$pkgname/archive/$_tag.tar.gz")

package() {
  cd "$srcdir/$pkgname-$_tag"
  sed -i "s/python>=2.6<3/python/" setup.py
  python2 setup.py install --root="${pkgdir}" --optimize=1
}

# vim:set ts=2 sw=2 et:
md5sums=('32dc3f9c4fb40eaf9a7ad3f9e92b82ce')
