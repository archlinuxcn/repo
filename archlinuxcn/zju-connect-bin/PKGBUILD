# Maintainer: zjuyk <ownbyzjuyk@gmail.com>

pkgname=zju-connect-bin
_pkgname=zju-connect
pkgver=0.4.1
pkgrel=1
pkgdesc="Go client for ZJU RVPN"
arch=("x86_64")
url="https://github.com/Mythologyli/zju-connect"
license=('AGPL-3.0')
depends=()
backup=("etc/zju-connect/config.toml")
install=zju-connect.install
provides=("zju-connect")
source=("$pkgname-$pkgver-amd64.zip::https://github.com/Mythologyli/${_pkgname}/releases/download/v${pkgver}/${_pkgname}-linux-amd64.zip"
        "${_pkgname}.service"
	"config.toml::https://raw.githubusercontent.com/Mythologyli/zju-connect/main/config.toml.example")
sha256sums=('e55c5daf00f48662f54bbe9e484a82567cdf097d8510fe84df4b97a976244867'
            '96f9145b783e770d6c448d9db7e43796b79c19f984f2b1387333a64c1874a74a'
            '4cf5695e326ce753769f207c439d419d0eba74f1510a1f8c9ace532002f76ff3')

package() {
	cd ${srcdir}
	
	mkdir -p ${pkgdir}/opt/${pkgname}
	mv ${srcdir}/zju-connect ${pkgdir}/opt/${pkgname}/

	mkdir -p ${pkgdir}/usr/bin
	ln -s /opt/${pkgname}/zju-connect "${pkgdir}"/usr/bin/zju-connect

	mkdir -p ${pkgdir}/etc/${_pkgname}
	install -Dm644 ${srcdir}/config.toml -t ${pkgdir}/etc/${_pkgname}/ 

	install -Dm644 ${_pkgname}.service -t ${pkgdir}/usr/lib/systemd/system/
}
