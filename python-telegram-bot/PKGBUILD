# Maintainer: Sean Enck <enckse@gmail.com>
# Maintainer: Sherlock Holo <sherlockya(at)gmail.com>
pkgname=python-telegram-bot
pkgver=9.0.0
pkgrel=1
pkgdesc="A Python wrapper around the Telegram Bot API"
url="https://github.com/python-telegram-bot/python-telegram-bot"
depends=('python-future' 'python-urllib3')
makedepends=('python-setuptools')
optdepends=('python-ujson: Ultra fast JSON parsing'
            'python-pysocks: SOCKS or HTTP proxy')

license=('LGPL3')
arch=('any')
source=("https://pypi.python.org/packages/f6/bc/a63239325cc5a28c5bee06fdf0a259fc4100194c11e6d029036aa6fe7ea8/python-telegram-bot-9.0.0.tar.gz")
sha256sums=('f5c3233bea7c7adf165e31225bbe9f28717e9f1f5070ebe99a4757c31c27ab28')

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
