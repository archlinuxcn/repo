# Maintainer: Dimitris Kiziridis <ragouel at outlook dot com>
# Co-Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=linux-wifi-hotspot
pkgver=2.1.1
pkgrel=1
pkgdesc="Create virtual wifi hotspot using same wifi card which is connected to an AP + many features (a GUI tool)"
arch=('x86_64')
url="https://github.com/lakinduakash/linux-wifi-hotspot"
license=('BSD')
depends=('hostapd'
         'iw'
         'gtk3'
         'procps-ng'
         'dnsmasq'
         'iproute2')
makedepends=('cmake' 'git')
optdepends=('haveged: For random MAC generation'
            'wireless_tools: if iw cannot recognize your adapter')
provides=('wihotspot')
conflicts=('wihotspot' 'create_ap')
install="$pkgname.install"
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('6d4f122630f9ebf44dbdd24d6080ddbd0b79ed5850865b78a2c556fd9371a177')

build() {
  cd "${pkgname}-${pkgver}"
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install

  install -Dm644 LICENSE -t \
   "${pkgdir}/usr/share/licenses/${pkgname}"
  install -Dm644 src/desktop/hotspot.png \
    "$pkgdir/usr/share/pixmaps/wihotspot.png"
  install -Dm644 src/desktop/wifihotspot.desktop \
    "$pkgdir/usr/share/applications/wihotspot.desktop"

  install -d "$pkgdir/usr/share/doc/$pkgname"
  cp -r docs/* "$pkgdir/usr/share/doc/$pkgname"
}
# vim:set ts=2 sw=2 et:
