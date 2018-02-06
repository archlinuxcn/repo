# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Submitter: Schala Zeal <schalaalexiazeal@gmail.com>

pkgname=spigot
_pkgver=1.12.2
_build=71
pkgver="${_pkgver}+b${_build}"
pkgrel=1
pkgdesc="High performance Minecraft server implementation"
arch=('any')
url="https://www.spigotmc.org/"
license=("LGPL")
depends=("java-runtime-headless>=8" 'screen' 'sudo' 'fontconfig' 'bash' 'awk' 'sed')
optdepends=("tar: needed in order to create world backups"
	"netcat: required in order to suspend an idle server")
makedepends=("java-environment>=8" 'git')
provides=("minecraft-server=${_pkgver%_*}" "bukkit=${_pkgver%_*}" "craftbukkit=${_pkgver%_*}")
conflicts=("bukkit" "craftbukkit" "spigot-patcher")
backup=("etc/conf.d/${pkgname}")
install="${pkgname}.install"
source=("BuildTools-${_pkgver}+b${_build}.jar::https://hub.spigotmc.org/jenkins/job/BuildTools/${_build}/artifact/target/BuildTools.jar"
	"${pkgname}-backup.service"
	"${pkgname}-backup.timer"
	"${pkgname}.service"
	"${pkgname}.conf"
	"${pkgname}.sh")
sha512sums=('d5a328a031aee8b449dbcf1b56c75ad3426d0a82a5e5e1210d56283c4a1504aa95e6194ed160b1f77fc3828a65ecf7ed49176a1a797f1a17f544783c0d45acb3'
            '914d079718bcf4adbe60ec1414ae95220be9e0ba6da8135d13fc9f1f82c7a5f1fb1844764a9d827bb9583bee2f6c10111880d0bcba135ec61d63b53a3f2aab27'
            '76c77e47c442b477216e968db2213612579b24add54cf0e0512f808498673500b4d24e59bce70b1e7479d724a9a897ceb154e937b88a476beb11c8776258b36c'
            'bfebbb163fe81dbf086f1511c60953c5ef4149e69c80e6a01af35ea67279e2c652072c9342a71e5d1c178a5504fc9d0275c19f51aacb65b722654c5c42a9b1cb'
            '33f456fd945bb2cfa6b390ce0ab02753cc6366e39abff80a4f2b7aa3aebe3cd31d148b785cbc2aa159dd8ad9fb03233a09f8693eb031b6b9db8dc03643d2397b'
            'f60f79121b9fd2b5bd117b539f5455b348ee9a5b5c16712ad71b362b8efff3e748c00df4d42135cdce9192cb35d0d9588d0fc5d0e28e6d493df076257586d164')

_game="spigot"
_server_root="/srv/craftbukkit"

build() {
	export MAVEN_OPTS="-Xmx2g"
	java -jar "BuildTools-${_pkgver}+b${_build}.jar" --rev "${_pkgver}"
}

package() {
	install -Dm644 "${_game}.conf" "${pkgdir}/etc/conf.d/${_game}"
	install -Dm755 "${_game}.sh" "${pkgdir}/usr/bin/${_game}"
	install -Dm644 "${_game}.service" "${pkgdir}/usr/lib/systemd/system/${_game}.service"
	install -Dm644 "${_game}-backup.service" "${pkgdir}/usr/lib/systemd/system/${_game}-backup.service"
	install -Dm644 "${_game}-backup.timer" "${pkgdir}/usr/lib/systemd/system/${_game}-backup.timer"
	install -Dm644 "${_game}-${_pkgver}.jar" "${pkgdir}${_server_root}/${_game}.${_pkgver}.jar"
	ln -s "${_game}.${_pkgver}.jar" "${pkgdir}${_server_root}/${_game}.jar"

	# Link the log files
	mkdir -p "${pkgdir}/var/log/"
	install -dm775 "${pkgdir}/${_server_root}/logs"
	ln -s "${_server_root}/logs" "${pkgdir}/var/log/${_game}"

	# Give the group write permissions and set user or group ID on execution
	chmod g+ws "${pkgdir}${_server_root}"

	# Make plugins folder ready for drag and drop
	install -dm777 "${pkgdir}/${_server_root}/plugins"
}
