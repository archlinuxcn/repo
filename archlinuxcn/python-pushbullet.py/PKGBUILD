# Maintainer: Hideaki Takahashi <mymelo+aur@gmail.com>
python=python

_libname=pushbullet.py
pkgname=python-$_libname
pkgver=0.11.1
pkgrel=1
pkgdesc="A simple python client for pushbullet.com."
depends=('python-requests' 'python-magic' 'python-websocket-client')
makedepends=('python-setuptools')
arch=('any')
source=(https://github.com/randomchars/${_libname}/archive/${pkgver}.tar.gz)
sha256sums=('7b25734638d36f6788e2cededd5c0684ca16510e9acf9c536e929a162b1dc608')

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
