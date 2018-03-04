# Maintainer: Sean Enck <enckse@gmail.com>
# Maintainer: Sherlock Holo <sherlockya(at)gmail.com>
pkgname=python-telegram-bot
pkgver=10.0.0
pkgrel=2
pkgdesc="A Python wrapper around the Telegram Bot API"
url="https://github.com/python-telegram-bot/python-telegram-bot"
depends=('python-future' 'python-urllib3')
makedepends=('python-setuptools')
optdepends=('python-ujson: Ultra fast JSON parsing'
            'python-pysocks: SOCKS or HTTP proxy')

license=('LGPL3')
arch=('any')
#source=("https://pypi.python.org/packages/f9/89/b946d746abb68588efd57297a9490ccc2e9faaae6c5f20712495d132588e/python-telegram-bot-10.0.0.tar.gz")
source=("https://github.com/python-telegram-bot/python-telegram-bot/releases/download/v10.0.0/python-telegram-bot-$pkgver.tar.gz")
sha256sums=('2e93d129d4b013b5b383c67c8dbfd8d791be23e58c1c3dfe5ad2aeaeba5bf037')

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
