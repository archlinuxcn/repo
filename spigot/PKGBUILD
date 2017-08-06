# Maintainer: Gordian Edenhofer <gordian.edenhofer[at]yahoo[dot]de>
pkgname=spigot
pkgver=1.12.1
pkgrel=1
pkgdesc="High performance Minecraft server implementation"
arch=(any)
url="https://www.spigotmc.org/"
license=("LGPL")
depends=("java-runtime-headless>=8" screen sudo fontconfig bash awk sed)
optdepends=("tar: needed in order to create world backups"
"netcat: required in order to suspend an idle server")
makedepends=("java-environment>=8" git)
provides=("minecraft-server=${pkgver%_*}" "bukkit=${pkgver%_*}" "craftbukkit=${pkgver%_*}")
conflicts=(bukkit craftbukkit spigot-patcher)
backup=("etc/conf.d/${pkgname}")
install="${pkgname}.install"
source=("https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"
"${pkgname}-backup.service"
"${pkgname}-backup.timer"
"${pkgname}.service"
"${pkgname}.conf"
"${pkgname}.sh")
noextract=("BuildTools.jar")
md5sums=('SKIP'
         '7bb2dc610c5f55e133bd41ab608ec7a1'
         '872d2e03799f1f8f0c75acdebce91894'
         '1eb2d5f485cf9eff7a99c826ad56fcf4'
         'b377759fa023d1119893dacff3b01cec'
         'bb5389bb949e6913ab62141f3cce24cb')

_game="spigot"
_server_root="/srv/craftbukkit"

build() {
	export MAVEN_OPTS="-Xmx2g"
	java -jar BuildTools.jar --rev ${pkgver}
}

package() {
	install -Dm644 ${_game}.conf              "${pkgdir}/etc/conf.d/${_game}"
	install -Dm755 ${_game}.sh                "${pkgdir}/usr/bin/${_game}"
	install -Dm644 ${_game}.service           "${pkgdir}/usr/lib/systemd/system/${_game}.service"
	install -Dm644 ${_game}-backup.service    "${pkgdir}/usr/lib/systemd/system/${_game}-backup.service"
	install -Dm644 ${_game}-backup.timer      "${pkgdir}/usr/lib/systemd/system/${_game}-backup.timer"
	install -Dm644 ${_game}-${pkgver}.jar     "${pkgdir}${_server_root}/${_game}.${pkgver}.jar"
	ln -s "${_game}.${pkgver}.jar" "${pkgdir}${_server_root}/${_game}.jar"

	# Link the log files
	mkdir -p "${pkgdir}/var/log/"
	ln -s "${_server_root}/logs" "${pkgdir}/var/log/${_game}"

	# Give the group write permissions and set user or group ID on execution
	chmod g+ws "${pkgdir}${_server_root}"
	
	# Make plugins folder ready for drag and drop
	install -dm777 "${pkgdir}/${_server_root}/plugins"
}
