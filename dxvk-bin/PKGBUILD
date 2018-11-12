# Maintainer: Adrià Cereto i Massagué <ssorgatem at gmail.com>

pkgbase=dxvk-bin
pkgname=('dxvk-win64-bin' 'dxvk-win32-bin' 'dxvk-bin')
pkgver=0.92
pkgrel=1
pkgdesc="A Vulkan-based compatibility layer for Direct3D 10/11 which allows running 3D applications on Linux using Wine (binary files)"
arch=('x86_64' 'i686')
url="https://github.com/doitsujin/dxvk"
license=('zlib/libpng')
provides=("dxvk")
conflicts=("dxvk-git")
options=(!strip)
source=("https://github.com/doitsujin/dxvk/releases/download/v$pkgver/dxvk-$pkgver.tar.gz"
    "setup_dxvk_aur.verb"
)
sha256sums=("e22c0ae4693aac88562c7a9a97b3316e086b9048c9f8f9e128923ac1611a5c49"
    "1a88e01e02ef9bfd9bf43d8dec4e70b425fb25812f597463ee4145705c82a504")

_extract_bin() {
	mkdir -p $pkgdir/usr/share/dxvk
	tar -xf dxvk-"$pkgver".tar.gz -C "$pkgdir/usr/share/dxvk" --strip-components=1 dxvk-"$pkgver"/x$1
	mkdir -p $pkgdir/usr/bin
	cat setup_dxvk_aur.verb | sed s/"DXVK_ARCH=64"/"DXVK_ARCH=$1"/g > "$pkgdir/usr/share/dxvk/x$1/setup_dxvk_aur.verb"
	echo "#!/bin/sh" > "$pkgdir/usr/bin/setup_dxvk$1"
	echo "winetricks --force /usr/share/dxvk/x$1/setup_dxvk_aur.verb" >> "$pkgdir/usr/bin/setup_dxvk$1"
	chmod +x "$pkgdir/usr/bin/setup_dxvk$1"
}

package_dxvk-win64-bin () {
        arch=('x86_64')
        provides=("dxvk" "dxvk64")
        depends=('vulkan-icd-loader' 'wine>=3.10' 'winetricks')
        conflicts=("dxvk-git" "dxvk-bin<0.63-5" "dxvk-win64-git")
        replaces=("dxvk-bin<0.63-5")
        _extract_bin 64
}
package_dxvk-win32-bin () {
        arch=('x86_64' 'i686')
        provides=("dxvk" "dxvk32")
        depends=('lib32-vulkan-icd-loader' 'wine>=3.10' 'winetricks')
        conflicts=("dxvk-git<0.63-5" "dxvk-bin<0.63-5" "dxvk-win32-git")
        replaces=("dxvk-bin")
        _extract_bin 32
}
package_dxvk-bin () {
	pkgdesc="Dummy package to smooth the transition to the split packages"
	depends=("dxvk-win32-bin" "dxvk-win64-bin")
}
