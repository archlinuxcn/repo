# Maintainer: nl6720 <nl6720@archlinux.org>

pkgname='shim-signed'
pkgver='15.r2.debian+15+1533136590.3beb971+7+deb10u1'
pkgrel='1'
pkgdesc='Initial UEFI bootloader that handles chaining to a trusted full bootloader under secure boot environments (prebuilt X64 EFI binaries from Debian)'
url='https://packages.debian.org/buster/shim-signed'
arch=('any')
license=('BSD')
options=('!strip')
noextract=('shim-helpers-amd64-signed_1+15+1533136590.3beb971+7+deb10u1_amd64.deb')
source=('https://deb.debian.org/debian/pool/main/s/shim-signed/shim-signed_1.33+15+1533136590.3beb971-7_amd64.deb'
        'https://deb.debian.org/debian/pool/main/s/shim-helpers-amd64-signed/shim-helpers-amd64-signed_1+15+1533136590.3beb971+7+deb10u1_amd64.deb')
sha256sums=('da466858eee1786433646dfcc9918395d2da06a7fb1815a3f66de749f5d8e506'
            '5d9198a417a4e0692e68d04594df1717ea10e9f80eb8292f19d30c56ab34a100')
prepare() {
	cd "$srcdir"
	# Exctract shimx64.efi
	bsdtar -xf 'data.tar.xz' 'usr/lib/shim/'
	# Extract mmx64.efi and fbx64.efi
	bsdtar -xf 'shim-helpers-amd64-signed_1+15+1533136590.3beb971+7+deb10u1_amd64.deb' 'data.tar.xz'
	bsdtar -xf 'data.tar.xz' 'usr/lib/shim/'
}

package() {
	install -Dm0644 "${srcdir}/usr/lib/shim/shimx64.efi.signed" "${pkgdir}/usr/share/${pkgname}/shimx64.efi"
	install -Dm0644 "${srcdir}/usr/lib/shim/mmx64.efi.signed" "${pkgdir}/usr/share/${pkgname}/mmx64.efi"
	install -Dm0644 "${srcdir}/usr/lib/shim/fbx64.efi.signed" "${pkgdir}/usr/share/${pkgname}/fbx64.efi"
}
