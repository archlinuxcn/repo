# Maintainer: Adrià Cereto i Massagué <ssorgatem at gmail.com>

pkgbase=dxvk-bin
pkgname=('dxvk-bin')
pkgver=1.3.2
pkgrel=0
pkgdesc="A Vulkan-based compatibility layer for Direct3D 10/11 which allows running 3D applications on Linux using Wine (Windows DLL binary files)"
arch=('x86_64' 'i686')
url="https://github.com/doitsujin/dxvk"
license=('zlib/libpng')
options=(!strip)
source=("https://github.com/doitsujin/dxvk/releases/download/v$pkgver/dxvk-$pkgver.tar.gz"
)
sha256sums=("aa70890a17b48be27648d15cb837b5167c99f75ee32ae0c94a85ec1f1fdc4675")

package_dxvk-bin () {
        arch=('x86_64')
        provides=("dxvk")
        depends=('vulkan-icd-loader' 'wine>=3.10' 'lib32-vulkan-icd-loader')
        conflicts=("dxvk-git")
        mkdir -p "$pkgdir/usr/share/dxvk"
        tar -xf dxvk-"$pkgver".tar.gz -C "$pkgdir/usr/share/dxvk" --strip-components=1 dxvk-"$pkgver"/
        mkdir -p "$pkgdir/usr/bin"
        ln -s /usr/share/dxvk/setup_dxvk.sh "$pkgdir/usr/bin/setup_dxvk"
        chmod +x "$pkgdir/usr/share/dxvk/setup_dxvk.sh"
        chown -R root:root "$pkgdir/usr/"
}
