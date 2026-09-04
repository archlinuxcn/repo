# Maintainer: Kimiblock Moe
# Contributor: evan <mail@evangoo.de>
_pkgname=drasl
pkgname="${_pkgname}"
pkgver=4.0.1
pkgrel=1
pkgdesc="Yggdrasil-compatible API server for Minecraft"
arch=('x86_64' 'aarch64')
url="https://github.com/unmojang/drasl"
license=('GPL-3.0-only')
makedepends=('git' 'go' 'gcc' 'nodejs' 'npm' 'swag')
depends+=(glibc)
conflicts=("${_pkgname}")
backup=("etc/drasl/config.toml")
source=(
	"${_pkgname}::git+https://github.com/unmojang/drasl.git#tag=v${pkgver}"
)
sha256sums=('846f9a2d78eb38788d5d7fa4064f25d13078cc3bf230d1f8770855ad678c3a9a')

#function pkgver() {
#	cd "${srcdir}/${_pkgname}"
#	git describe --long --tags --abbrev=8 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
#}

function prepare() {
	cd "${srcdir}/${_pkgname}"
	git reset --hard
	git clean -fdx
}

function build() {
	cd "${srcdir}/${_pkgname}"
	make
}

function package() {
	cd "$srcdir/${_pkgname}"
	make install prefix="${pkgdir}/usr"
	install -vDm644 ./example/config-example.toml "${pkgdir}/etc/drasl/config-example.toml"
	install -vDm644 ./example/config-example.toml "${pkgdir}/etc/drasl/config.toml"
	install -vDm644 ./example/drasl.service "${pkgdir}/usr/lib/systemd/system/${_pkgname}.service"
}

