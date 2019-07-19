# Maintainer: suthernfriend <public@janpeterkoenig.com>
# Contributor: RPDiep
# Contributor: Hugo Barrera <hugo@barrera.io>
# Contributor: liberodark

pkgname=tusk
pkgver=0.23.0
pkgrel=0
pkgdesc="Refined Evernote desktop app"
arch=('x86_64')
url="https://github.com/klaussinani/tusk"

license=('MIT')
makedepends=('npm')
depends=('xdg-utils' 'electron')

source=(
	"${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
	"${pkgname}.desktop"
	"${pkgname}.png"
	"${pkgname}"
)

sha256sums=('1b367df6b24fe6c7b2a284bad07abf889de9aba5dcfe8a1d9c02e0becd9d97f9'
            'b72cfcd35a727cb982f82d9f97f9e4330e81fbc70af47d1bc7f5baa7837a29f3'
            '2e8e1f13a86bd4a8fdbd2a4a69cde6b09e035b31352ad60f5a81d61a7abfe5bf'
            'b4e388ee237f137e94ac3fac317007e0ba79bddc2b4406b9760ebbcc62b9224d')

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	npm install --cache "${srcdir}/npm-cache"
	node ./node_modules/electron-builder/out/cli/cli.js build -l dir --x64
}

package() {
	# licenses
	install -Dm644 "${srcdir}/${pkgname}-${pkgver}/license.md" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
	install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" "${srcdir}/${pkgname}-${pkgver}/dist/linux-unpacked/LICENSE"*
	
	# binary
	install -Dm644 "${srcdir}/${pkgname}-${pkgver}/dist/linux-unpacked/resources/app.asar" "${pkgdir}/usr/lib/${pkgname}/${pkgname}.asar"
	
	# shell wrapper
	install -Dm755 "${srcdir}/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
	
	# desktop and image
	install -Dm644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
	install -Dm644 "${srcdir}/${pkgname}.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
}
