_pkgname=aioconsole
pkgname=python-aioconsole
pkgver=0.1.8
pkgrel=1
pkgdesc="Asynchronous console and interfaces for asyncio"
arch=('any')
url="https://github.com/vxgmichel/aioconsole"
license=('GPLv3')
depends=('python' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/34/bb/0479e51f7df8c92df9409ec2464184aac64c2ad793780c312fc316e6c381/aioconsole-0.1.8.tar.gz')
md5sums=('5dbf64e6ced6c56c8a62de26692bd0f3')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
