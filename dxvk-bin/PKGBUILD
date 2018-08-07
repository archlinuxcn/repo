# Maintainer: Adrià Cereto i Massagué <ssorgatem at gmail.com>

pkgbase=dxvk-bin
pkgname=('dxvk-win64-bin' 'dxvk-win32-bin' 'dxvk-bin')
pkgver=0.64
pkgrel=6
pkgdesc="A Vulkan-based compatibility layer for Direct3D 11 which allows running 3D applications on Linux using Wine (binary files)"
arch=('x86_64' 'i686')
url="https://github.com/doitsujin/dxvk"
license=('zlib/libpng')
provides=("dxvk")
conflicts=("dxvk-git")
options=(!strip)
source=("https://github.com/doitsujin/dxvk/releases/download/v$pkgver/dxvk-$pkgver.tar.gz")
sha256sums=("2e03e40ff0a9d36f96a06137f3fa9110ebaea230d0bf6c22cf6399e16e97fb9c")

_extract_bin() {
	mkdir -p $pkgdir/usr/share/dxvk
	tar -xf dxvk-"$pkgver".tar.gz -C "$pkgdir/usr/share/dxvk" --strip-components=1 dxvk-"$pkgver"/x$1
	mkdir -p $pkgdir/usr/bin
	ln -s "/usr/share/dxvk/x$1/setup_dxvk.sh" "$pkgdir/usr/bin/setup_dxvk$1"
}

package_dxvk-win64-bin () {
        arch=('x86_64')
        provides=("dxvk" "dxvk64")
        depends=('vulkan-icd-loader' 'wine>=3.10')
        conflicts=("dxvk-git" "dxvk-bin<0.63-5" "dxvk-win64-git")
        replaces=("dxvk-bin<0.63-5")
        _extract_bin 64
}
package_dxvk-win32-bin () {
        arch=('x86_64' 'i686')
        provides=("dxvk" "dxvk32")
        depends=('lib32-vulkan-icd-loader' 'wine>=3.10')
        conflicts=("dxvk-git<0.63-5" "dxvk-bin<0.63-5" "dxvk-win32-git")
        replaces=("dxvk-bin")
        _extract_bin 32
}
package_dxvk-bin () {
	pkgdesc="Dummy package to smooth the transition to the split packages"
	depends=("dxvk-win32-bin" "dxvk-win64-bin")
}
