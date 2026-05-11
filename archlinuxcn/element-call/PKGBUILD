# Maintainer: Kimiblock Moe

pkgname=element-call
pkgdesc="Group calls powered by Matrix"
url="https://github.com/element-hq/element-call"
license=("Apache-2.0")
arch=("any")
pkgver=0.19.3
pkgrel=1
makedepends=("git" "pnpm" "nodejs-vite")
depends=()
source=("git+${url}#tag=v${pkgver}")
md5sums=('fc4434d46a0919bd682b5fa6de5d0023')
provides=("element-call")
options=()
backup=()

function prepare() {
	cd element-call
	pnpm i
}

function build() {
	cd element-call
	pnpm build
}

function package() {
	cd element-call
	install -d "${pkgdir}/usr/share/element-call"
	cp -r dist/* "${pkgdir}/usr/share/element-call"
	ln -srf \
		"${pkgdir}/usr/share/webapps/element-call" \
		"${pkgdir}/usr/share/element-call"
}
