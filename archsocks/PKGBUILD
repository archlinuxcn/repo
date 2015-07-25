# Maintainer: lilydjwg <lilydjwg@gmail.com>
pkgname=archsocks
pkgdesc="archsocks 网络加速代理"
pkgver=0.1
pkgrel=1
arch=('any')
url="http://www.archsocks.com/"
license=()
depends=('python-aiohttp' 'python-chardet')
install=${pkgname}.install
source=("http://www.archsocks.com/files/archsocks.tar.gz"
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

sha256sums=('bc12cbadfcd657b935cf7377980f1f4c842aac50ec47155ad272fbf58ce6d409'
            'dac4cba524d950d068ea13ea467f5d42da308106e15bb45293fa28f225692c53'
            'cd3cf869b53612fd15084088fa82e6a7e8689f8fc47803e36b7df45f71479c5e')
