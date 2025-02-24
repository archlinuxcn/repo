# Maintainer: zjuyk <ownbyzjuyk@gmail.com>

pkgname=zju-connect-bin
_pkgname=zju-connect
pkgver=0.8.0
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
sha256sums=('23edd12d1dd0dac93ddd86a6e2a18d06393bc0f67c60d782338754924213e3fa'
            '96f9145b783e770d6c448d9db7e43796b79c19f984f2b1387333a64c1874a74a'
            '2a1176953c8de26079b930645eaf41596300aa3f7a9cf8bc494c95dd090843c1')

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
