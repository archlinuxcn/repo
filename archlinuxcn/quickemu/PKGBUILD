# Maintainer: Steffen Hansen <steffengrundsoe@gmail.com>
pkgname=quickemu
pkgver=4.9.9
pkgrel=2
pkgdesc="Quickly create and run optimised Windows, macOS and Linux desktop virtual machines."
arch=(any)
url="https://github.com/quickemu-project/quickemu"
license=('MIT')
depends=('qemu' 'coreutils' 'grep' 'jq' 'procps' 'python3' 'cdrtools' 'usbutils' 'util-linux' 'sed' 'spice-gtk' 'swtpm' 'wget' 'xorg-xrandr' 'zsync' 'edk2-ovmf' 'xdg-user-dirs' 'socat')
optdepends=('quickgui: graphical user interface' 'aria2: faster downloads')
provides=("$pkgname")
conflicts=("$pkgname")
source=("$pkgname-$pkgver.tar.gz"::"https://github.com/quickemu-project/quickemu/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('ef5c5015e91c4fef6797c4961c400d18e1ae8191a8d1eae6e3512823dd2ff2a8')

package() {
  cd "$pkgname-$pkgver"

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm755 -t "$pkgdir/usr/bin" chunkcheck quickemu quickget quickreport
  install -Dm644 -t "$pkgdir/usr/share/man/man1" docs/quickemu.1 docs/quickget.1
  install -Dm644 -t "$pkgdir/usr/share/man/man5" docs/quickemu_conf.5
}
