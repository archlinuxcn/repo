# Maintainer: nl6720 <nl6720@archlinux.org>

pkgname='shim-signed'
pkgver='15.f8'
pkgrel='2'
pkgdesc='Initial UEFI bootloader that handles chaining to a trusted full bootloader under secure boot environments (prebuilt X64 EFI binaries from Fedora)'
url='https://koji.fedoraproject.org/koji/packageinfo?packageID=14502'
arch=('any')
license=('BSD')
options=('!strip')
noextract=('shim-x64-13-4.x86_64.rpm')
source=("https://kojipkgs.fedoraproject.org/packages/shim/${pkgver//.f/\/}/x86_64/shim-x64-${pkgver//.f/-}.x86_64.rpm"
        'https://kojipkgs.fedoraproject.org/packages/shim-signed/13/4/x86_64/shim-x64-13-4.x86_64.rpm')
sha512sums=('bea58059801c9af1f9beab675cf7b6bb7262278b1fe874cb56c3dec051a71236a352d3444f82ee0204518fdf1e18cbde4ce2d240dc1223dda2409ea23c3daa48'
            'b6091fd4154b7cd4353e9bea2bcd0b796864c3c268a5a9ebce90e738afc7ab30924099b2127eec108d62da96983147c4d40292ed391ed1b2cfe5257b8d6fd474')

prepare() {
	cd "${srcdir}"
	# Use old MokManager from Fedora's shim-signed 13-4, https://github.com/rhboot/shim/issues/143 
	bsdtar -f shim-x64-13-4.x86_64.rpm -x boot/efi/EFI/fedora/mmx64.efi
}

package() {
	install -D -m0644 -t "${pkgdir}/usr/share/${pkgname}/" "${srcdir}/boot/efi/EFI/fedora/shimx64.efi"
	install -D -m0644 -t "${pkgdir}/usr/share/${pkgname}/" "${srcdir}/boot/efi/EFI/fedora/mmx64.efi"
	install -D -m0644 -t "${pkgdir}/usr/share/${pkgname}/" "${srcdir}/boot/efi/EFI/BOOT/fbx64.efi"
}
