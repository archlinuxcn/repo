_pkgname=aioconsole
pkgname=python-aioconsole
pkgver=0.1.9
pkgrel=1
pkgdesc="Asynchronous console and interfaces for asyncio"
arch=('any')
url="https://github.com/vxgmichel/aioconsole"
license=('GPLv3')
depends=('python' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/47/f8/49ebb5124dac1b2994452c1809ae7a1b6dfb4ecbf3bdb8bda1771fa05304/aioconsole-0.1.9.tar.gz')
md5sums=('d96aedaa6852c9da3b238e3c0752ea7b')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
