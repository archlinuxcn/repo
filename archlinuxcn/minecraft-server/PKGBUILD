# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributer: Philip Abernethy <chais.z3r0@gmail.com>
# Contributer: sowieso <sowieso@dukun.de>

pkgname=minecraft-server
pkgver=1.18.1
_nonce=125e5adf40c659fd3bce3e66e67a16bb49ecc1b9
pkgrel=2
_mng_ver=1.0.0
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
sha512sums=('cb306772c06e88b70475961ec1f057a9edfcef8db334479ec5c28e8b07287b3209bc54d83f7da7e8c63a8581e7ddbb93109acbf491ff74806b27486368640e71'
            'e315277da81cb28de338e870f477dc58dc9d8f8542594431ab5321150c92ff5634ace2be8c6778d1edb718fdeb6850d7021bffcbd3cae2a00f20e3a64caa3d92')

_game="minecraft"
_server_root="/srv/minecraft"

build() {
	make -C "${srcdir}/minecraft-server-${_mng_ver}" clean

	make -C "${srcdir}/minecraft-server-${_mng_ver}" \
		GAME=${_game} \
		MYNAME=${_game}d \
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
		MYNAME=${_game}d \
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
