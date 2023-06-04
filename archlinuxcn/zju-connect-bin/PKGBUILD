# Maintainer: zjuyk <ownbyzjuyk@gmail.com>

pkgname=zju-connect-bin
_pkgname=zju-connect
pkgver=0.3.0
pkgrel=8
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
sha256sums=('5a04f66178b9ac0f035a4354bb4425c5953006038204b185ea0ee4fca0c8b817'
            'f82ae013579f8d9e43242274ba660ef122e43747a4fc88e6e0dbd8b9c96d6cf4'
            '02d294350d41ab9cc9e979a9447cb4429f4577fc6d85ee3e6685464e65511c2c')

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
