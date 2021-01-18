# Maintainer: Dimitris Kiziridis <ragouel at outlook dot com>
# Co-Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=linux-wifi-hotspot
pkgver=3.6.0
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
optdepends=('haveged: For random MAC generation'
            'wireless_tools: if iw cannot recognize your adapter'
            'bash-completion: for bash completions')
provides=('wihotspot' 'create_ap')
conflicts=('wihotspot' 'create_ap')
backup=('etc/create_ap.conf')
install="$pkgname.install"
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
        'makefile.patch')
sha256sums=('a3020ded511c57d24ad97a257878bf024bb6483860721d97bb8fb62c132d8de0'
            '0b7a043231d07cc5e14efb3b3c2541caac037cece882b3ca9891b0fe169ff942')

prepare() {
  cd "${pkgname}-${pkgver}"
  patch --forward --strip=1 --input="${srcdir}/makefile.patch"
}

build() {
  cd "${pkgname}-${pkgver}"
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install

  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

# vim:set ts=2 sw=2 et:
