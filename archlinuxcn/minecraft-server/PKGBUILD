# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributer: Philip Abernethy <chais.z3r0@gmail.com>
# Contributer: sowieso <sowieso@dukun.de>

pkgname=minecraft-server
pkgver=1.14.4
_nonce=3dc3d84a581f14691199cf6831b71ed1296a9fdf
pkgrel=1
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
sha512sums=('b3d2852c6fa1b996bbf2fa9fc1fb860c6bca5136bcc5ddd3d236d85789c6bce81620f6b2d69eaa10c41d020fe0bb54de2fa601b3df3093af2691853a4445e1f8'
            'c8f96bafb0ba3fd8946ac791b09e75cae54dc1a8e02822f91ca70a77a8ba45b253a83c4db30f9cfbf0658a2608b38e6de3d00f1d832ef676f329a78e69eab3e7'
            '19ee3646bfbace353b65c0373594edb654de11c9671f29cebad3b31109f29f94ade1d529d9f409b0989c376bef9b451585b22a1e0ac4295fcc92d9565f808418'
            '5203f6331f740ecfcea2a2cc653603ae97419baa89e08512f9d8feb63e4a52978442a69b313eccd9037b676a62ab528e2b533c0fb95a9c7177318279fe0cde79'
            '73132ec613e05c8ed7ebe4eda2395f1ea0733ffe94ba7e203e06246d5852139bbfb7a9073b2b01891282339a2f85676699cd889cde79d6317066e27fd65b1d67'
            '9e806e35c207c96714f53a360e2d493f665867126398c2f12486b6f9d2b2db98c883e19aade703e18c31696e05808847762e494f743db7802127f415a00ba3bc')

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
