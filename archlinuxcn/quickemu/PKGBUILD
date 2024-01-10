# Maintainer: Steffen Hansen <steffengrundsoe@gmail.com>
pkgname=quickemu
pkgver=4.9.2
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
sha256sums=('fa5e2e5112deb836c0ab6035ab0aaabd1465b13e945d4a49dc975b94f1b01233')

package() {
  cd "$pkgname-$pkgver"

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm755 quickemu "$pkgdir/usr/bin/quickemu"
  install -Dm755 macrecovery "$pkgdir/usr/bin/macrecovery"
  install -Dm755 quickget "$pkgdir/usr/bin/quickget"

  install -Dm644 docs/quickget.1 $pkgdir/usr/share/man/man1/quickget.1
  install -Dm644 docs/quickemu.1 $pkgdir/usr/share/man/man1/quickemu.1
  install -Dm644 docs/quickemu_conf.1 $pkgdir/usr/share/man/man1/quickemu_conf.1
}
