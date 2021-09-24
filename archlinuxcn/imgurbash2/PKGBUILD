# Maintainer: Alec Mev <alec@mev.earth>
# Contributor: NightSong <ramif.47@gmail.com>

pkgname=imgurbash2
pkgver=3.2
pkgrel=1
pkgdesc='A shell script that uploads/deletes images to/from IMGUR'
arch=('any')
url='https://github.com/ram-on/imgurbash2'
license=('MIT')
depends=('bash' 'curl')
optdepends=(
	'wl-clipboard: To be able to copy image URL to clipboard in Wayland'
	'xclip: To be able to copy image URL to clipboard in X'
	'xsel: To be able to copy image URL to clipboard in X'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/ram-on/imgurbash2/archive/${pkgver}.tar.gz")
sha256sums=('a17ef6c96399550293ee806bae4665e4353c3280df4d3ebe041cf589fe6bc259')

package() {
	cd "${pkgname}-${pkgver}"
	install -Dm755 -t "${pkgdir}/usr/bin/" "${pkgname}"
	install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}" README.md
	install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}" examples.md
	install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}
