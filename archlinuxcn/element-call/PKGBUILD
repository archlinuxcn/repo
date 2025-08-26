# Maintainer: Kimiblock Moe

pkgname=element-call
pkgdesc="Group calls powered by Matrix"
url="https://github.com/element-hq/element-call"
license=("Apache-2.0")
arch=("any")
pkgver=0.15.0
pkgrel=2
makedepends=("yarn-berry" "liburing" "git" "nodejs")
depends=()
source=("git+${url}#tag=v${pkgver}")
md5sums=('2c2f46c7f3e852ccfad90061bb056f43')
provides=("element-call")
options=()
backup=()

function prepare() {
	cd element-call
	yarn
}

function build() {
	cd element-call
	yarn build
}

function package() {
	cd element-call
	install -d "${pkgdir}/usr/share/element-call"
	cp -r dist/* "${pkgdir}/usr/share/element-call"
	ln -srf \
		"${pkgdir}/usr/share/webapps/element-call" \
		"${pkgdir}/usr/share/element-call"
}
