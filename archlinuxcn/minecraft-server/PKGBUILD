# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributer: Philip Abernethy <chais.z3r0@gmail.com>
# Contributer: sowieso <sowieso@dukun.de>

pkgname=minecraft-server
pkgver=1.15.1
_nonce=4d1826eebac84847c71a77f9349cc22afd0cf0a1
pkgrel=2
pkgdesc="Minecraft server unit files, script, and jar"
arch=('any')
url="https://minecraft.net/"
license=('custom')
depends=('java-runtime-headless>=8' 'screen' 'sudo' 'bash' 'awk' 'sed')
optdepends=("tar: needed in order to create world backups"
	"netcat: required in order to suspend an idle server")
conflicts=('minecraft-server-systemd' 'minecraft-canary')
backup=('etc/conf.d/minecraft')
install="${pkgname}.install"
# See https://launchermeta.mojang.com/mc/game/version_manifest.json for a list of all releases
source=("minecraft_server.${pkgver}.jar"::"https://launcher.mojang.com/v1/objects/${_nonce}/server.jar"
	"minecraftd-backup.service"
	"minecraftd-backup.timer"
	"minecraftd.service"
	"minecraftd.conf"
	"minecraftd.sh")
noextract=("minecraft_server.${pkgver}.jar")
sha512sums=('4458daa6cd87b04ddbf0819dfc0538d24b8d08c529a94f1abff9b894d24ffb4eb3d0b23b8bfb088b2b6f43fb6f71d17700d9f80dab2ed56dc51c5bef329ba6bb'
            '32d11156b63f780fe530ca408e8f2c36c7cb761427992526a70819e24ebc042813f9001b1d822847ffe22e6aec34420f215c8bf21ca73905747537ef4ab7e905'
            '19ee3646bfbace353b65c0373594edb654de11c9671f29cebad3b31109f29f94ade1d529d9f409b0989c376bef9b451585b22a1e0ac4295fcc92d9565f808418'
            '5203f6331f740ecfcea2a2cc653603ae97419baa89e08512f9d8feb63e4a52978442a69b313eccd9037b676a62ab528e2b533c0fb95a9c7177318279fe0cde79'
            'b7e84172bdb791e3a065b2593e63f3f4a017481d4321d28cdc528f88447f9c591a9ac58ccec828e76cb4ec3eacfa0acd8e3645f82e6065f80e4fec06cead67d9'
            'a1022e06a3d8567b31c9670b817a4751ad9f14242ce7ee69f184a459c667ec2334dcd259410de38fc75a0f9a65c0a033d737cf0b73abcf37f5de073db9560035')

_game="minecraft"
_server_root="/srv/minecraft"

package() {
	install -Dm644 ${_game}d.conf              "${pkgdir}/etc/conf.d/${_game}"
	install -Dm755 ${_game}d.sh                "${pkgdir}/usr/bin/${_game}d"
	install -Dm644 ${_game}d.service           "${pkgdir}/usr/lib/systemd/system/${_game}d.service"
	install -Dm644 ${_game}d-backup.service    "${pkgdir}/usr/lib/systemd/system/${_game}d-backup.service"
	install -Dm644 ${_game}d-backup.timer      "${pkgdir}/usr/lib/systemd/system/${_game}d-backup.timer"
	install -Dm644 ${_game}_server.${pkgver}.jar "${pkgdir}${_server_root}/${_game}_server.${pkgver}.jar"
	ln -s "${_game}_server.${pkgver}.jar" "${pkgdir}${_server_root}/${_game}_server.jar"

	# Link the log files
	mkdir -p "${pkgdir}/var/log/"
	install -dm2755 "${pkgdir}/${_server_root}/logs"
	ln -s "${_server_root}/logs" "${pkgdir}/var/log/${_game}"

	# Give the group write permissions and set user or group ID on execution
	chmod g+ws "${pkgdir}${_server_root}"
}
