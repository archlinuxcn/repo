# Maintainer: Mikuro Kagamine <mikurok@forgecrushing.com>

pkgname=browsh
pkgver=1.6.4
pkgrel=2
pkgdesc='A fully-modern text-based browser, rendering to TTY and browsers'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url='https://www.brow.sh'
license=('LGPL2.1')
makedepends=('go' 'go-bindata' 'dep' 'git')
optdepends=('upx: compress binary')
conflicts=('browsh-bin' 'browsh-git')
options=('!strip')
noextract=("${pkgname}-${pkgver}-an.fx.xpi")
source=("https://github.com/${pkgname}-org/${pkgname}/archive/v${pkgver}.tar.gz"
		"https://github.com/${pkgname}-org/${pkgname}/releases/download/v${pkgver}/${pkgname}-${pkgver}-an.fx.xpi")
sha256sums=('965ce2d94d1d9e4b92411d344421c0bea40994527cafd694c5a6e8e206681ede'
			'b410527a69dba88a30d8a6d341a20eb5cb1f84b684e9bc8bb6bc88a2930e0eea')


prepare() {
	## Go is fussy.
	export GOPATH="${srcdir}/.gopath"
	export _interfacer="${GOPATH}/src/${pkgname}/interfacer"
	mkdir -p "${GOPATH}/src"
	mv "${srcdir}/${pkgname}-${pkgver}" "${GOPATH}/src/${pkgname}"
	cd "${_interfacer}"

	echo Turn webext into an embeddable binary...
	xpipath="$(mktemp -d)"
	cp "${srcdir}/${pkgname}-${pkgver}-an.fx.xpi" "${xpipath}/${pkgname}.xpi"
	if [ $(which upx 2>/dev/null) ]; then
		_compress="-nocompress"
	else
		_compress=""; fi
	go-bindata	$_compress\
				-prefix "${xpipath}"\
				-pkg $pkgname\
				-o "${_interfacer}/src/${pkgname}/webextension.go"\
				"${xpipath}/${pkgname}.xpi"
	rm -r "${xpipath}"

	echo Install $pkgname dependencies...
	dep ensure
}

build() {
	export GOPATH="${srcdir}/.gopath"
	export _interfacer="${GOPATH}/src/${pkgname}/interfacer"
	cd "$_interfacer"
	echo Build ${pkgname}...
	go build	-x\
				-gcflags "all=-trimpath=${GOPATH}"\
				-asmflags "all=-trimpath=${GOPATH}"\
				-o "${srcdir}/${pkgname}" ./src/main.go
	strip --strip-all "${srcdir}/${pkgname}"
	if [ $(which upx 2>/dev/null) ]; then
		echo Compressing ${pkgname} with UPX...
		upx "${srcdir}/${pkgname}"; fi
}

package() {
	depends=('firefox>=63')
	install -Dm755 $pkgname "${pkgdir}/usr/bin/${pkgname}"
}
