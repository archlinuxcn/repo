# Maintainer: Adrià Cereto i Massagué <ssorgatem at gmail.com>

pkgbase=dxvk-bin
pkgname=('dxvk-win64-bin' 'dxvk-win32-bin' 'dxvk-bin')
pkgver=1.0.1
pkgrel=1
pkgdesc="A Vulkan-based compatibility layer for Direct3D 10/11 which allows running 3D applications on Linux using Wine (Windows DLL binary files)"
arch=('x86_64' 'i686')
url="https://github.com/doitsujin/dxvk"
license=('zlib/libpng')
provides=("dxvk")
conflicts=("dxvk-git")
options=(!strip)
source=("https://github.com/doitsujin/dxvk/releases/download/v$pkgver/dxvk-$pkgver.tar.gz"
)
sha256sums=("739847cdd14b302dac600c66bc6617d7814945df6d4d7b6c91fecfa910e3b1b1")

package_dxvk-win64-bin () {
        arch=('x86_64')
        depends=('dxvk-bin')
	pkgdesc="Dummy package"
}
package_dxvk-win32-bin () {
        arch=('x86_64' 'i686')
        depends=('dxvk-bin')
	pkgdesc="Dummy package"
}
package_dxvk-bin () {
        arch=('x86_64')
        provides=("dxvk" "dxvk64" "dxvk32")
        depends=('vulkan-icd-loader' 'wine>=3.10' 'lib32-vulkan-icd-loader')
        conflicts=("dxvk-git" "dxvk-bin<1.0-1" "dxvk-win64-bin<1.0-1" "dxvk-win32-bin<1.0-1"  "dxvk-win64-git")
        mkdir -p $pkgdir/usr/share/dxvk
        tar -xf dxvk-"$pkgver".tar.gz -C "$pkgdir/usr/share/dxvk" --strip-components=1 dxvk-"$pkgver"/
        mkdir -p $pkgdir/usr/bin
	echo "#!/bin/sh" > "$pkgdir/usr/bin/setup_dxvk"
	echo '/usr/share/dxvk/setup_dxvk.sh $1 --symlink --without-dxgi' >> "$pkgdir/usr/bin/setup_dxvk"
        chmod +x "$pkgdir/usr/share/dxvk/setup_dxvk.sh"
	chmod +x "$pkgdir/usr/bin/setup_dxvk"
        chown -R root:root "$pkgdir/usr/"
}
