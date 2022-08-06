# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributer: Philip Abernethy <chais.z3r0@gmail.com>
# Contributer: sowieso <sowieso@dukun.de>

pkgname=minecraft-server
pkgver=1.19.2
_nonce=f69c284232d7c7580bd89a5a4931c3581eae1378
pkgrel=1
_mng_ver=1.0.2
pkgdesc="Minecraft server unit files, script, and jar"
arch=('any')
url="https://minecraft.net/"
license=('custom')
depends=('java-runtime-headless>=16' 'tmux' 'sudo' 'bash' 'awk' 'sed')
optdepends=("tar: needed in order to create world backups"
	"netcat: required in order to suspend an idle server")
conflicts=('minecraft-server-systemd' 'minecraft-canary')
backup=('etc/conf.d/minecraft')
install="${pkgname}.install"
# See https://launchermeta.mojang.com/mc/game/version_manifest.json for a list of all releases
source=("minecraft_server.${pkgver}.jar"::"https://launcher.mojang.com/v1/objects/${_nonce}/server.jar"
	"minecraft-server-${_mng_ver}.tar.gz"::"https://github.com/Edenhofer/minecraft-server/archive/refs/tags/v${_mng_ver}.tar.gz")
noextract=("minecraft_server.${pkgver}.jar")
sha512sums=('4af9474416abd22ccfe42a230b7ffff6a1fb82cdc7aa5994f6788223ab12149a26bcf76443752e7ce8c2fc3fef0535f704bdba786a95210fb4bac1b45b72a8c9'
            '11d708d511b63e5541bcc1dbcaf29abbf7cb9583b1d313028770a39b26b41d48dcba023f7e1d6fe30f3c093d20e10a43363011edd432e5785a4580e5c5f852a6')

_game="minecraft"
_server_root="/srv/minecraft"

build() {
	make -C "${srcdir}/minecraft-server-${_mng_ver}" clean

	make -C "${srcdir}/minecraft-server-${_mng_ver}" \
		GAME=${_game} \
		INAME=${_game}d \
		SERVER_ROOT=${_server_root} \
		BACKUP_PATHS="world" \
		GAME_USER=${_game} \
		MAIN_EXECUTABLE=minecraft_server.jar \
		SERVER_START_CMD="java -Xms512M -Xmx1024M -jar ./minecraft_server.jar nogui" \
		all
}

package() {
	make -C "${srcdir}/minecraft-server-${_mng_ver}" \
		DESTDIR="${pkgdir}" \
		GAME=${_game} \
		INAME=${_game}d \
		install

	install -Dm644 ${_game}_server.${pkgver}.jar "${pkgdir}${_server_root}/${_game}_server.${pkgver}.jar"
	ln -s "${_game}_server.${pkgver}.jar" "${pkgdir}${_server_root}/${_game}_server.jar"

	# Link the log files
	mkdir -p "${pkgdir}/var/log/"
	install -dm2755 "${pkgdir}/${_server_root}/logs"
	ln -s "${_server_root}/logs" "${pkgdir}/var/log/${_game}"

	# Give the group write permissions and set user or group ID on execution
	chmod g+ws "${pkgdir}${_server_root}"
}
