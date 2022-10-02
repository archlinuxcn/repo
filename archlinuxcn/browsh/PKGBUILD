# Maintainer: gilcu3 <gilcu3 at gmail dot com>
# Contributor: Mikuro Kagamine <mikurok@forgecrushing.com>

pkgname=browsh
pkgver=1.8.0
pkgrel=3
pkgdesc='A fully-modern text-based browser, rendering to TTY and browsers'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url='https://www.brow.sh'
license=('LGPL2.1')
makedepends=('git' 'go')
makeoptdepends=('upx: compress binary')
depends=('firefox>=63')
conflicts=('browsh-bin' 'browsh-git')
options=('!strip')
source=("https://github.com/${pkgname}-org/${pkgname}/archive/v${pkgver}.tar.gz"
		"https://github.com/${pkgname}-org/${pkgname}/releases/download/v${pkgver}/${pkgname}-${pkgver}.xpi"
		)
sha256sums=('81b1f9d725527f851457046845f8ed0d1fdd00fdc97d3c19e69c0bc5a7e70cd3'
            'd76c566dfe278181d62ca57dcb2c728b4372ff31d28f6a3b21c6adb3e11ffa90'
			)


prepare() {
	cw=$(pwd)
	export GOPATH=$cw/go
	mkdir -p $GOPATH
	interfacer="${GOPATH}/src/github.com/browsh-org/${pkgname}/interfacer"
	mkdir -p "${GOPATH}/src/github.com/browsh-org/${pkgname}"
	rm -rf ${interfacer}
  	ln -sf  "../../../../../${pkgname}-${pkgver}/interfacer" "${interfacer}"
	cp "${srcdir}/${pkgname}-${pkgver}.xpi" "${interfacer}/src/${pkgname}/${pkgname}.xpi"
}

build() {
	cw=$(pwd)
	export GOPATH=$cw/go
	interfacer="${GOPATH}/src/github.com/browsh-org/${pkgname}/interfacer"
	cd "$interfacer"
	echo Build ${pkgname}...
	local webextension="src/browsh/browsh.xpi"
	go build	-x -modcacherw \
				-gcflags "all=-trimpath=${GOPATH}"\
				-asmflags "all=-trimpath=${GOPATH}"\
				 -o "${srcdir}/${pkgname}" ./cmd/browsh 
	strip --strip-all "${srcdir}/${pkgname}"
	if [ $(which upx 2>/dev/null) ]; then
		echo Compressing ${pkgname} with UPX...
		upx "${srcdir}/${pkgname}"; fi
}

package() {
	install -Dm755 $pkgname "${pkgdir}/usr/bin/${pkgname}"
}
