# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: Dimitris Kiziridis <ragouel at outlook dot com>
pkgname=linux-wifi-hotspot
pkgver=4.6.0
pkgrel=2
pkgdesc="Feature-rich wifi hotspot creator"
arch=('x86_64' 'aarch64')
url="https://github.com/lakinduakash/linux-wifi-hotspot"
license=('BSD')
depends=('gtk3' 'hostapd' 'iproute2' 'iw' 'procps-ng' 'qrencode')
optdepends=("dnsmasq: For 'NATed' or 'None' Internet sharing method"
            "iptables: For 'NATed' or 'None' Internet sharing method"
            'haveged: For random MAC generation'
            'wireless_tools: if iw cannot recognize your adapter')
provides=('wihotspot' 'create_ap')
conflicts=('wihotspot' 'create_ap')
backup=('etc/create_ap.conf')
install="$pkgname.install"
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
        'https://github.com/lakinduakash/linux-wifi-hotspot/pull/367.patch')
sha256sums=('bc0ad1d38e3e1b00bb7e0416a2b7a1a79dc908036342c85b0a8c3962ffd5bded'
            '346cd6b7367edf9b01ca3612fa6c7f6acc28730b7718c21fc16e6175d77f4b45')

prepare() {
  cd "$pkgname-$pkgver"

  # Update frequency parsing for iw 6.7 compatibility
  patch -Np1 -i ../367.patch
}

build() {
  cd "$pkgname-$pkgver"
  make
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
