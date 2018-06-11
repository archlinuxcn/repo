# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Submitter: Schala Zeal <schalaalexiazeal@gmail.com>

pkgname=spigot
_pkgver=1.12.2
_build=73
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
sha512sums=('b9dfe324f7eed186278285595e6785cdeb197cec2cac59442b79731ac70ebee224798906cf14f331cd43527122bca9647d69561354a40d7bc39a2690a61e9d83'
            '914d079718bcf4adbe60ec1414ae95220be9e0ba6da8135d13fc9f1f82c7a5f1fb1844764a9d827bb9583bee2f6c10111880d0bcba135ec61d63b53a3f2aab27'
            '76c77e47c442b477216e968db2213612579b24add54cf0e0512f808498673500b4d24e59bce70b1e7479d724a9a897ceb154e937b88a476beb11c8776258b36c'
            '3af8a79686d6086a651b8ff34ff6195417a6d2285b2b959d87d95856b9500ea57e8e6f8475199e96f5db45bbe3308b98d7c8e27b468790331a1a8695887138db'
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
