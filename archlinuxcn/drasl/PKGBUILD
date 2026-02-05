# Maintainer: Kimiblock Moe
# Contributor: evan <mail@evangoo.de>
_pkgname=drasl
pkgname="${_pkgname}"
pkgver=3.4.1
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
sha256sums=('5c1d26edad7d4e2476f3dc5b90a31e5fe512e417adff6b567ffc79f6d3b5a28e')

#function pkgver() {
#	cd "${srcdir}/${_pkgname}"
#	git describe --long --tags --abbrev=8 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
#}

function prepare() {
	cd "${srcdir}/${_pkgname}"
	git reset --hard
	git clean -fdx
	git remote add oidcfix https://github.com/evan-goode/drasl.git
	git fetch --all
	git cherry-pick 1a41da8f07c2c04d9d789bec5225c899c8f15946 --no-commit
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

