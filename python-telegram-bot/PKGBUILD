# Maintainer: Sean Enck <enckse@gmail.com>
# Maintainer: Sherlock Holo <sherlockya(at)gmail.com>
pkgname=python-telegram-bot
pkgver=6.1.0
pkgrel=1
pkgdesc="A Python wrapper around the Telegram Bot API"
url="https://github.com/python-telegram-bot/python-telegram-bot"
depends=('python' 'python-future' 'python-urllib3')
makedepends=('python-setuptools')
optdepends=('python-ujson: SOCKS or HTTP proxy'
            'python-pysocks: Ultra fast JSON parsing')
license=('LGPLv3')
arch=('any')
source=("https://pypi.python.org/packages/3f/f7/4f0f1f935f356fdd3ceca0282f3d57745c4f26d2bb6152707e3505392894/python-telegram-bot-6.1.0.tar.gz"
        "request.patch")
sha256sums=('90ac2ff18f6217ad06330af98ba148957c55b92ae473c65b6726e6b17d3674f6'
            '61fe8778ba75d8e6a3ee247c7c45a892a2362ab73bd17cf91a2c241b86231993')

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
