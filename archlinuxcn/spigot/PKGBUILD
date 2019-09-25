# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Submitter: Schala Zeal <schalaalexiazeal@gmail.com>

pkgname=spigot
_pkgver=1.14.4
_build=103
pkgver="${_pkgver}+b${_build}"
pkgrel=2
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
sha512sums=('4a8a65f243f730f2ac7400e237710e6f511fc3e53937174b3e66a0b8e136f8076f742d50e6b702e4dbb172d910d51278a6ab04ebce4f5e41d22a2528d137b74f'
            '914d079718bcf4adbe60ec1414ae95220be9e0ba6da8135d13fc9f1f82c7a5f1fb1844764a9d827bb9583bee2f6c10111880d0bcba135ec61d63b53a3f2aab27'
            '76c77e47c442b477216e968db2213612579b24add54cf0e0512f808498673500b4d24e59bce70b1e7479d724a9a897ceb154e937b88a476beb11c8776258b36c'
            '5a32439ff4b8fa9db89e9242206cf99109e0b00f29f87711c25342dda522171d999f7e18fb2013437ddf62cfec05b6677601933233aaf42bcb5d67eb7a1469ee'
            '33f456fd945bb2cfa6b390ce0ab02753cc6366e39abff80a4f2b7aa3aebe3cd31d148b785cbc2aa159dd8ad9fb03233a09f8693eb031b6b9db8dc03643d2397b'
            '28d8292d442b8f77ce2b568f2ac0a10474d12361f02ae4e6e67e810d653f5a7e1e100d1f937dec2dfea35fd736047f55a7fb0d8754628b23d1a81948c0d62009')

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
