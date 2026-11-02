# Maintainer: Kimiblock Moe

pkgname=element-call
pkgdesc="Group calls powered by Matrix"
url="https://github.com/element-hq/element-call"
license=("Apache-2.0")
arch=("any")
pkgver=0.28.1
pkgrel=1
makedepends=("git" "pnpm" "nodejs-vite")
depends=()
source=("git+${url}#tag=v${pkgver}")
md5sums=('456687d2d50ba1fd914f0cfbc1f1b184')
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
