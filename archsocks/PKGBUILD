# Maintainer: lilydjwg <lilydjwg@gmail.com>
pkgname=archsocks
pkgdesc="archsocks 网络加速代理"
pkgver=0.5
pkgrel=1
arch=('any')
url="https://github.com/archsocks/archsocks"
license=()
depends=('python-aiohttp' 'python-chardet' 'iptables')
install=${pkgname}.install
source=("archsocks-${pkgver}.tar.gz::http://104.129.177.141/files/archsocks.tar.gz"
        archsocks
        archsocks.service
)

build() {
  true
}

package() {
  _pyver=$(python -c 'import sys; print("%d.%d" % sys.version_info[:2])')
  cd "$srcdir/archsocks-files/lib"

  mkdir -p "$pkgdir/usr/lib/python$_pyver/site-packages"
  cp -r archsocks_client_updater "$pkgdir/usr/lib/python$_pyver/site-packages"
  cp -r archsocks_common "$pkgdir/usr/lib/python$_pyver/site-packages"
  python3 -m compileall "$pkgdir/usr/lib/python$_pyver/site-packages"

  cd "$srcdir"
  install -Dm755 archsocks "$pkgdir/usr/bin/archsocks"
  install -Dm644 archsocks.service "$pkgdir/usr/lib/systemd/system/archsocks.service"
  install -dm750 "$pkgdir/var/lib/archsocks"
}

sha256sums=('cc28982e9a4b17b3a8f012186522b3b47108b5da4c42e5f78aa937bb1cd6e8ea'
            'dac4cba524d950d068ea13ea467f5d42da308106e15bb45293fa28f225692c53'
            'c21c0fe29393e6ef45d018b6402f6c493888e93dfde26852f1a6638632061c4b')
