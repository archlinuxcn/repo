# Maintainer: Sean Enck <enckse@gmail.com>
# Maintainer: Sherlock Holo <sherlockya(at)gmail.com>
pkgname=python-telegram-bot
pkgver=10.0.1
pkgrel=1
pkgdesc="A Python wrapper around the Telegram Bot API"
url="https://github.com/python-telegram-bot/python-telegram-bot"
depends=('python-future' 'python-urllib3')
makedepends=('python-setuptools')
optdepends=('python-ujson: Ultra fast JSON parsing'
            'python-pysocks: SOCKS or HTTP proxy')

license=('LGPL3')
arch=('any')
#source=("https://pypi.python.org/packages/f9/89/b946d746abb68588efd57297a9490ccc2e9faaae6c5f20712495d132588e/python-telegram-bot-10.0.0.tar.gz")
source=("https://github.com/python-telegram-bot/python-telegram-bot/releases/download/v$pkgver/python-telegram-bot-$pkgver.tar.gz")
sha256sums=('580390d75a63706647962556bab69c7313bee1438411288c37f545e421498e6c')

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
