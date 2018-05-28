# Maintainer: Hideaki Takahashi <mymelo+aur@gmail.com>
python=python

_libname=pushbullet.py
pkgname=python-$_libname
pkgver=0.11.0
pkgrel=1
pkgdesc="A simple python client for pushbullet.com."
depends=('python-requests' 'python-magic' 'python-websocket-client')
makedepends=('python-setuptools')
arch=('any')
source=(https://github.com/randomchars/${_libname}/archive/${pkgver}.tar.gz)
md5sums=('3ce16295be29fbc4272a47ba5c2243c9')

url="https://github.com/randomchars/pushbullet.py"
license=("MIT")

build() {
    cd $srcdir/$_libname-$pkgver

    $python setup.py build || return 1
}

package() {
    cd $srcdir/$_libname-$pkgver

    $python setup.py install --root=$pkgdir

    install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE
}
