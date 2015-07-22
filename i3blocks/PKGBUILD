# Maintainer: Vlad M. <vlad@archlinux.net>
# Contributor: Patrice Peterson <runiq at archlinux dot us>
# Contributor: Vivien Didelot <vivien+aur@didelot.org>

pkgname=i3blocks
pkgver=1.4
pkgrel=2
pkgdesc='Define blocks for your i3bar status line'
arch=('i686' 'x86_64')
group=('i3')
url="https://github.com/vivien/i3blocks"
license=('GPL3')
optdepends=('openvpn: For openvpn script'
            'playerctl: For mediaplayer script'
            'lm_sensors: For temperature script'
            'acpi: For battery script'
            'sysstat: For cpu_usage script')
source=("https://github.com/vivien/$pkgname/releases/download/$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('c64720057e22cc7cac5e8fcd58fd37e75be3a7d5a3cb8995841a7f18d30c0536')

build () {
  cd "$pkgname-$pkgver"
  make VERSION="$pkgver"
}

package () {
  cd "$pkgname-$pkgver"
  make VERSION="$pkgver" PREFIX=/usr LIBEXECDIR=/usr/lib DESTDIR="$pkgdir" install
}
