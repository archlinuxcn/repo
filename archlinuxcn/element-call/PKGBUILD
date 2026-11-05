# Maintainer: Kimiblock Moe

pkgname=element-call
pkgdesc="Group calls powered by Matrix"
url="https://github.com/element-hq/element-call"
license=("Apache-2.0")
arch=("any")
pkgver=0.28.2
pkgrel=1
makedepends=("git" "pnpm" "nodejs-vite")
depends=()
source=("git+${url}#tag=v${pkgver}")
md5sums=('6dec5c115ae152256c6de5a66f32097b')
provides=("element-call")
options=()
backup=()

function prepare() {
	cd element-call
	pnpm install --frozen-lockfile --ignore-pnpmfile
}

function build() {
	cd element-call
	export NODE_OPTIONS="--max-old-space-size=4096"

	pnpm run build:full:production
}

function package() {
	cd element-call
	install -d "${pkgdir}/usr/share/element-call"
	cp -r dist/* "${pkgdir}/usr/share/element-call"
	ln -srf \
		"${pkgdir}/usr/share/webapps/element-call" \
		"${pkgdir}/usr/share/element-call"
}
