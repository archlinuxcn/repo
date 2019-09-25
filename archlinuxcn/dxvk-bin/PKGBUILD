# Maintainer: Adrià Cereto i Massagué <ssorgatem at gmail.com>

pkgbase=dxvk-bin
pkgname=('dxvk-bin')
pkgver=1.4.0
realver=1.4
pkgrel=1
pkgdesc="A Vulkan-based compatibility layer for Direct3D 10/11 which allows running 3D applications on Linux using Wine (Windows DLL binary files)"
arch=('x86_64' 'i686')
url="https://github.com/doitsujin/dxvk"
license=('zlib/libpng')
options=(!strip)
source=("https://github.com/doitsujin/dxvk/releases/download/v$realver/dxvk-$realver.tar.gz"
)
sha256sums=("bf22785de1ce728bbdcfb4615035924112b4718049ca2cade5861b03735181de")

package_dxvk-bin () {
        arch=('x86_64')
        provides=("dxvk")
        depends=('vulkan-icd-loader' 'wine>=3.10' 'lib32-vulkan-icd-loader')
        conflicts=("dxvk-git")
        mkdir -p "$pkgdir/usr/share/dxvk"
	mv dxvk-"$realver".tar.gz dxvk-"$pkgver".tar.gz
        tar -xf dxvk-"$pkgver".tar.gz -C "$pkgdir/usr/share/dxvk" --strip-components=1 dxvk-"$realver"/
        mkdir -p "$pkgdir/usr/bin"
        ln -s /usr/share/dxvk/setup_dxvk.sh "$pkgdir/usr/bin/setup_dxvk"
        chmod +x "$pkgdir/usr/share/dxvk/setup_dxvk.sh"
        chown -R root:root "$pkgdir/usr/"
}
