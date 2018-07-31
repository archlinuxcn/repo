# Maintainer: Adrià Cereto i Massagué <ssorgatem at gmail.com>

pkgbase=dxvk-bin
pkgname=('dxvk-win64-bin' 'dxvk-win32-bin' 'dxvk-bin')
pkgver=0.63
pkgrel=5
pkgdesc="A Vulkan-based compatibility layer for Direct3D 11 which allows running 3D applications on Linux using Wine (binary files)"
arch=('x86_64' 'i686')
url="https://github.com/doitsujin/dxvk"
license=('zlib/libpng')
depends=('vulkan-icd-loader' 'wine>=3.10')
provides=("dxvk")
conflicts=("dxvk-git")
options=(!strip)
source=("https://github.com/doitsujin/dxvk/releases/download/v$pkgver/dxvk-$pkgver.tar.gz")
sha256sums=("696df816bd9640770dee14f932bc641a16261fccf76be7c28d812a64ca6040fa")

_extract_bin() {
	mkdir -p $pkgdir/usr/share/dxvk
	tar -xf dxvk-"$pkgver".tar.gz -C "$pkgdir/usr/share/dxvk" --strip-components=1 dxvk-"$pkgver"/x$1
	mkdir -p $pkgdir/usr/bin
	ln -s "/usr/share/dxvk/x$1/setup_dxvk.sh" "$pkgdir/usr/bin/setup_dxvk$1"
}

package_dxvk-win64-bin () {
        arch=('x86_64')
        provides=("dxvk" "dxvk64")
        conflicts=("dxvk-git" "dxvk-bin<0.63-5" "dxvk-win64-git")
        replaces=("dxvk-bin<0.63-5")
        _extract_bin 64
}
package_dxvk-win32-bin () {
        arch=('x86_64' 'i686')
        provides=("dxvk" "dxvk32")
        conflicts=("dxvk-git<0.63-5" "dxvk-bin<0.63-5" "dxvk-win32-git")
        replaces=("dxvk-bin")
        _extract_bin 32
}
package_dxvk-bin () {
	pkgdesc="Dummy package to smooth the transition to the split packages"
	depends=("dxvk-win32-bin" "dxvk-win64-bin")
}
