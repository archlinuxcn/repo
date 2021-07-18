# Maintainer: nl6720 <nl6720@archlinux.org>

pkgname='shim-signed'
pkgver='15.4+fedora+5'
pkgrel='1'
pkgdesc='Initial UEFI bootloader that handles chaining to a trusted full bootloader under secure boot environments (prebuilt X64 EFI binaries from Fedora)'
url='https://koji.fedoraproject.org/koji/packageinfo?packageID=14502'
arch=('any')
license=('BSD')
options=('!strip')
install="${pkgname}.install"
source=("https://kojipkgs.fedoraproject.org/packages/shim/${pkgver//+fedora+/\/}/x86_64/shim-x64-${pkgver//+fedora+/-}.x86_64.rpm")
sha512sums=('966836d71ad4b6cca44e650893aeb09e69d1ca9d192d61a8b9efef8d7389b2a6e0ff0f488c3c00dd895427ac2ae1a4778e62d39340d7bd0ff9e809a45cebd014')

package() {
	install -D -m0644 -t "${pkgdir}/usr/share/${pkgname}/" "${srcdir}/boot/efi/EFI/fedora/shimx64.efi"
	install -D -m0644 -t "${pkgdir}/usr/share/${pkgname}/" "${srcdir}/boot/efi/EFI/fedora/mmx64.efi"
	install -D -m0644 -t "${pkgdir}/usr/share/${pkgname}/" "${srcdir}/boot/efi/EFI/BOOT/fbx64.efi"
}
