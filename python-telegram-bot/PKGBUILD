# Maintainer: Sean Enck <enckse@gmail.com>
# Maintainer: Sherlock Holo <sherlockya(at)gmail.com>
pkgname=python-telegram-bot
pkgver=6.0.3
pkgrel=2
pkgdesc="A Python wrapper around the Telegram Bot API"
url="https://github.com/python-telegram-bot/python-telegram-bot"
depends=('python' 'python-future' 'python-urllib3')
makedepends=('python-setuptools')
optdepends=('python-ujson: SOCKS or HTTP proxy'
            'python-pysocks: Ultra fast JSON parsing')
license=('LGPLv3')
arch=('any')
source=("https://pypi.python.org/packages/3b/6e/fedd1a0b79938c851b92061f4547d2ca6217d9d49f9800f033fe5738f5df/python-telegram-bot-6.0.3.tar.gz"
        "request.patch")
sha256sums=('5263dfc1d2039aa4c855cb6ee7ef0b55674fe62fe0bf0d8af2b56fcabb97a970'
            '1eb33a8ce7fa54839e975f91ec5390594238e9531a8ff7d671220021b8b5f4c7')

prepare(){
    cd $srcdir
    bsdtar -xf $pkgname-$pkgver.tar.gz
    cp $srcdir/request.patch $srcdir/$pkgname-$pkgver/telegram/utils/
}

build(){
    cd $srcdir/$pkgname-$pkgver
    rm -rf telegram/vendor
    sed '/certifi/d' requirements.txt -i
    #patch -p0 -i setup.patch
    cd telegram/utils
    patch -p0 -i request.patch
    cd $srcdir/$pkgname-$pkgver
    python setup.py build
}

package(){
    cd $srcdir/$pkgname-$pkgver
    python setup.py install --root="$pkgdir" --optimize=1 
}
