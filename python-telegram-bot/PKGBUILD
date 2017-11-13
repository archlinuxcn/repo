# Maintainer: Sean Enck <enckse@gmail.com>
# Maintainer: Sherlock Holo <sherlockya(at)gmail.com>
pkgname=python-telegram-bot
pkgver=8.1.1
pkgrel=3
pkgdesc="A Python wrapper around the Telegram Bot API"
url="https://github.com/python-telegram-bot/python-telegram-bot"
depends=('python-future' 'python-urllib3')
makedepends=('python-setuptools')
optdepends=('python-ujson: Ultra fast JSON parsing'
            'python-pysocks: SOCKS or HTTP proxy')

license=('LGPL3')
arch=('any')
source=("https://pypi.python.org/packages/b4/d4/66e153eb470179dd6346ae1f5a50c75b871c2263ab7b976427b2d9722689/python-telegram-bot-8.1.1.tar.gz")
sha256sums=('238c4a88b09d93c52d413bcf7e7fe14dfeb02f5f9222ffe4cafd4bd3d55489a3')

prepare(){
    cd $srcdir
    bsdtar -xf $pkgname-$pkgver.tar.gz
    #cp $srcdir/request.patch $srcdir/$pkgname-$pkgver/telegram/utils/
}

build(){
    cd $srcdir/$pkgname-$pkgver
    rm -rf telegram/vendor
    sed '/certifi/d' requirements.txt -i
    #patch -p0 -i setup.patch
    cd telegram/utils
    #patch -p0 -i request.patch
    sed -i 's/import telegram.vendor.ptb_urllib3.urllib3 as urllib3/import urllib3 as urllib3/g' request.py
    sed -i 's/import telegram.vendor.ptb_urllib3.urllib3.contrib.appengine as appengine/import urllib3.contrib.appengine as appengine/g' request.py
    sed -i 's/from telegram.vendor.ptb_urllib3.urllib3.connection import HTTPConnection/from urllib3.connection import HTTPConnection/g' request.py
    sed -i 's/from telegram.vendor.ptb_urllib3.urllib3.util.timeout import Timeout/from urllib3.util.timeout import Timeout/g' request.py
    sed -i "s/certifi.where()/\"\/etc\/ssl\/certs\/ca-certificates.crt\"/g" request.py
    sed -i 's/import certifi//g' request.py
    cd $srcdir/$pkgname-$pkgver
    python setup.py build
}

package(){
    cd $srcdir/$pkgname-$pkgver
    python setup.py install --skip-build --root="$pkgdir" --optimize=1 
}
