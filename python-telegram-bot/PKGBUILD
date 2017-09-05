# Maintainer: Sean Enck <enckse@gmail.com>
# Maintainer: Sherlock Holo <sherlockya(at)gmail.com>
pkgname=python-telegram-bot
pkgver=8.0
pkgrel=1
pkgdesc="A Python wrapper around the Telegram Bot API"
url="https://github.com/python-telegram-bot/python-telegram-bot"
depends=('python' 'python-future' 'python-urllib3')
makedepends=('python-setuptools')
optdepends=('python-ujson: Ultra fast JSON parsing'
            'python-pysocks: SOCKS or HTTP proxy')
license=('LGPLv3')
arch=('any')
source=("https://pypi.python.org/packages/74/12/bbc0158dd7aa20ff7e55dc936954e4d06f0844c11ad0cb52b29bf547b532/python-telegram-bot-8.0.tar.gz"
        "request.patch")
sha256sums=('b648845f9d5c3ed569066be25e5efdfa36148a24d87e7b5219b4eb8e64853b4d'
            'cb93235b5e479603d6195e158df7b6028fc3bf87e7bd9bc7a602a029f9bdc644')

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
