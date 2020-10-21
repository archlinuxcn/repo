# Maintainer: Julian Thonhauser <julthon@gmail.com>
pkgname=plymouth-theme-gdm-arch
pkgver=v1
pkgrel=1
pkgdesc="Simple plymouth gdm-like theme with Arch Linux logo"
url="https://github.com/julthon/plymouth-theme-gdm-arch"
license=("GPL3")
arch=(any)
depends=(plymouth)
source=("$pkgname-$pkgver.tar.gz::https://github.com/julthon/plymouth-theme-gdm-arch/releases/download/$pkgver/plymouth-theme-gdm-arch_$pkgver.tar.gz")
md5sums=('c132534052e07ae2163af7293fa77f1c')

package() {
  _instdir="$pkgdir/usr/share/plymouth/themes"
  mkdir -p $_instdir
  cp -dpr --no-preserve=ownership "$srcdir/gdm-arch" $_instdir
}
