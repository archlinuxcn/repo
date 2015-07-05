# Maintainer: Patrice Peterson <runiq at archlinux dot us>
# Contributor: Vivien Didelot <vivien+aur@didelot.org>

_ghuser=vivien
pkgname=i3blocks
pkgver=1.3
pkgrel=2
pkgdesc='Define blocks for your i3bar status line'
arch=('any')
group=('i3')
url="https://github.com/$_ghuser/$pkgname"
license=('GPL3')
optdepends=('openvpn: For openvpn script'
            'playerctl: For mediaplayer script'
            'lm_sensors: For temperature script'
            'acpi: For battery script'
            'sysstat: For cpu_usage script')
source=("https://github.com/$_ghuser/$pkgname/releases/download/$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('e9d8a4a2c822645cef2373aa7d3762215d7b8d3e7d44c2dd24002c37b532ee53')

build () {
  cd "$pkgname-$pkgver"
  make VERSION="$pkgver"
}

package () {
  cd "$pkgname-$pkgver"
  make VERSION="$pkgver" PREFIX=/usr DESTDIR="$pkgdir" install
}

# vim: et ts=2 sw=2
