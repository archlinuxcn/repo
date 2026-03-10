# Maintainer: zjuyk <ownbyzjuyk@gmail.com>

pkgname=zju-connect-bin
_pkgname=zju-connect
pkgver=1.0.0
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
sha256sums=('7daefe33fb3af6d4b4f7e424abe79d74988bc9cab28012994f68f866df73aa61'
            '96f9145b783e770d6c448d9db7e43796b79c19f984f2b1387333a64c1874a74a'
            'ea2e8b80e006bc4a7d06ede40eaf5a2f2f9d62acebe0555a152dfd813a8cbc52')

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
