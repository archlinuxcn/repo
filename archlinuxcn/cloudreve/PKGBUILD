# Maintainer: Kimiblock Moe

pkgname=cloudreve
arch=('x86_64')
backup=("etc/cloudreve/config.ini")
pkgver=4.7.0
pkgrel=1
pkgdesc="Self-hosted file management and sharing system, supports multiple storage providers"
url=https://github.com/cloudreve/Cloudreve
license=("GPL-3.0-only")
#depends=("")
source=("git+https://github.com/cloudreve/Cloudreve.git#tag=${pkgver}" "cloudreve.service" "config.ini")
makedepends=("go" "git" "goreleaser" "yarn" "zip")
sha256sums=('76d916c62014af9938693643ec5fdc5c86defd1e11ab658581fe3c495871d107'
            '5e78a6bc0624c39ca1fb5e7733ffa8472d41540dab2e009871504c82469d0384'
            '3145bf311d7ae94a1f00a8c78df08240fa95668d1a8eb3981ffd7fca3b70535a')
provides=("cloudreve")

function prepare(){
	cd "${srcdir}/Cloudreve"
	git submodule init
	git submodule update --depth=1
}

function build(){
	echo "Starting build"
	cd "${srcdir}/Cloudreve"
	goreleaser build --clean --single-target
}

function package(){
	install -Dm644 "${srcdir}/config.ini" "${pkgdir}/etc/cloudreve/config.ini"
	cd "${srcdir}/Cloudreve"
	install -Dm755 "${srcdir}/Cloudreve/dist/Cloudreve_linux_amd64_v1/cloudreve" "${pkgdir}/usr/lib/cloudreve/cloudreve"
	install -Dm644 "${srcdir}/cloudreve.service" "${pkgdir}/usr/lib/systemd/system/cloudreve.service"
	mkdir -p "${pkgdir}/usr/lib/sysusers.d"
	echo 'u	cloudreve	-	"Cloudreve User"	/var/lib/cloudreve' >"${pkgdir}/usr/lib/sysusers.d/cloudreve.conf"
	mkdir -p "${pkgdir}/usr/lib/tmpfiles.d"
	mkdir -p "${pkgdir}/usr/lib/cloudreve"
	echo 'd	/var/lib/cloudreve	0700	cloudreve	cloudreve	-' >"${pkgdir}/usr/lib/tmpfiles.d/cloudreve.conf"
}
