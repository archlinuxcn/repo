# Maintainer: Steffen Hansen <steffengrundsoe@gmail.com>
pkgname=quickemu
pkgver=4.9.6
pkgrel=1
pkgdesc="Quickly create and run optimised Windows, macOS and Linux desktop virtual machines."
arch=(any)
url="https://github.com/quickemu-project/quickemu"
license=('MIT')
depends=('qemu' 'coreutils' 'grep' 'jq' 'procps' 'python3' 'cdrtools' 'usbutils' 'util-linux' 'sed' 'spice-gtk' 'swtpm' 'wget' 'xorg-xrandr' 'zsync' 'edk2-ovmf' 'xdg-user-dirs' 'socat')
optdepends=('quickgui: graphical user interface' 'aria2: faster downloads')
provides=("$pkgname")
conflicts=("$pkgname")
source=("$pkgname-$pkgver.tar.gz"::"https://github.com/quickemu-project/quickemu/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('796a047b0bfabb91eb143e5422ff74f5d2812f47120ed6b34eaf82bbdfe3e2a3')

package() {
  cd "$pkgname-$pkgver"

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm755 chunkcheck "$pkgdir/usr/bin/chunkcheck"
  install -Dm755 quickemu "$pkgdir/usr/bin/quickemu"
  install -Dm755 quickget "$pkgdir/usr/bin/quickget"
  install -Dm755 quickreport "$pkgdir/usr/bin/quickreport"
  install -Dm755 windowskey "$pkgdir/usr/bin/windowskey"

  install -Dm644 docs/quickget.1 $pkgdir/usr/share/man/man1/quickget.1
  install -Dm644 docs/quickemu.1 $pkgdir/usr/share/man/man1/quickemu.1
  install -Dm644 docs/quickemu_conf.1 $pkgdir/usr/share/man/man1/quickemu_conf.1
}
