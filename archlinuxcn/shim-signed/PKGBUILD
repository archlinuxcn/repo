# Maintainer: nl6720 <nl6720@archlinux.org>

pkgname='shim-signed'
pkgver='15.6+fedora+2'
pkgrel='1'
pkgdesc='Initial UEFI bootloader that handles chaining to a trusted full bootloader under secure boot environments (prebuilt X64 and IA32 EFI binaries from Fedora)'
url='https://koji.fedoraproject.org/koji/packageinfo?packageID=14502'
arch=('any')
license=('BSD')
options=('!strip')
install="${pkgname}.install"
source=("https://kojipkgs.fedoraproject.org/packages/shim/${pkgver//+fedora+/\/}/x86_64/shim-"{x64,ia32}"-${pkgver//+fedora+/-}.x86_64.rpm")
sha512sums=('971978bddee95a6a134ef05c4d88cf5df41926e631de863b74ef772307f3e106c82c8f6889c18280d47187986abd774d8671c5be4b85b1b0bb3d1858b65d02cf'
            '045325802474f53c6e86eff1166f1a966268c9ad706fac4c08966f211dbc32fba21ed3a07c46445ec579ac1e2819a1313ff54d6169737806954962945c61bdc2')
package() {
	install -D -m0644 -t "${pkgdir}/usr/share/${pkgname}/" "${srcdir}/boot/efi/EFI/fedora/shimx64.efi"
	install -D -m0644 -t "${pkgdir}/usr/share/${pkgname}/" "${srcdir}/boot/efi/EFI/fedora/mmx64.efi"
	install -D -m0644 -t "${pkgdir}/usr/share/${pkgname}/" "${srcdir}/boot/efi/EFI/BOOT/fbx64.efi"
	install -D -m0644 -t "${pkgdir}/usr/share/${pkgname}/" "${srcdir}/boot/efi/EFI/fedora/shimia32.efi"
	install -D -m0644 -t "${pkgdir}/usr/share/${pkgname}/" "${srcdir}/boot/efi/EFI/fedora/mmia32.efi"
	install -D -m0644 -t "${pkgdir}/usr/share/${pkgname}/" "${srcdir}/boot/efi/EFI/BOOT/fbia32.efi"
}
