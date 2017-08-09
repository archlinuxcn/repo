# Maintainer: Sean Enck <enckse@gmail.com>
# Maintainer: Sherlock Holo <sherlockya(at)gmail.com>
pkgname=python-telegram-bot
pkgver=7.0.1
pkgrel=1
pkgdesc="A Python wrapper around the Telegram Bot API"
url="https://github.com/python-telegram-bot/python-telegram-bot"
depends=('python' 'python-future' 'python-urllib3')
makedepends=('python-setuptools')
optdepends=('python-ujson: Ultra fast JSON parsing'
            'python-pysocks: SOCKS or HTTP proxy')
license=('LGPLv3')
arch=('any')
source=("https://pypi.python.org/packages/c4/76/df538d842f16793244842eb71e19697d240affb65a32a65fa1067760b211/python-telegram-bot-7.0.1.tar.gz"
        "request.patch")
sha256sums=('494ffdd76ffcca62ce6276906b0afe6e8e8c4245b78501404f723aec79949bff'
            '2919bd5588988d10ba3ebd416bbcb7fe77a4a151aec43f21d753163512d87dc5')

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
