# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributer: Philip Abernethy <chais.z3r0@gmail.com>
# Contributer: sowieso <sowieso@dukun.de>

pkgname=minecraft-server
pkgver=1.17.1
_nonce=a16d67e5807f57fc4e550299cf20226194497dc2
pkgrel=2
pkgdesc="Minecraft server unit files, script, and jar"
arch=('any')
url="https://minecraft.net/"
license=('custom')
depends=('java-runtime-headless>=16' 'tmux' 'sudo' 'bash' 'awk' 'sed')
optdepends=("tar: needed in order to create world backups"
	"netcat: required in order to suspend an idle server")
conflicts=('minecraft-server-systemd' 'minecraft-canary')
backup=('etc/conf.d/minecraft')
# See https://launchermeta.mojang.com/mc/game/version_manifest.json for a list of all releases
source=("minecraft_server.${pkgver}.jar"::"https://launcher.mojang.com/v1/objects/${_nonce}/server.jar"
	"minecraftd-backup.service"
	"minecraftd-backup.timer"
	"minecraftd.service"
	"minecraftd.sysusers"
	"minecraftd.tmpfiles"
	"minecraftd.conf"
	"minecraftd.sh")
noextract=("minecraft_server.${pkgver}.jar")
sha512sums=('fe6e48e2cee38224d2c88f04c19afca9c21fddbe6077b5538e0a0581c2f6c4478ec99bc369bec5131d709b89273dbd769659f149163f0c284b518a38e58a5bcc'
            'a10e38c0e9a09c25e23e46147a8b8ce4d88a62ee780c1c0b525b9e41a563c4a4ed8e94d851abc3936bc31f3faa916ef005543129a039f66878b8f2c34853b91d'
            '19ee3646bfbace353b65c0373594edb654de11c9671f29cebad3b31109f29f94ade1d529d9f409b0989c376bef9b451585b22a1e0ac4295fcc92d9565f808418'
            '5203f6331f740ecfcea2a2cc653603ae97419baa89e08512f9d8feb63e4a52978442a69b313eccd9037b676a62ab528e2b533c0fb95a9c7177318279fe0cde79'
            'a62c8c04e08dbac0db0aa2eeb505d70f8fd925bd2e427899512ba3ac828d4644e1c43c8d92325c6bc49c8d9ecb40cb5c44bf5957a63980b1e2cf86fdb38a05a7'
            'a74f4e31065b6c6f5c830182de05a8c75a6de6eaac7b3dc26479827646ef20ab872509aac88be613048c97d378711c38612ec7ac92d22134acefd40f6e0a99da'
            '30e434ba183527da8047b1ffe403a083f1af34dbd229b5871222e9da0004cdf5d4152eaa4b73215befcb1233d08cc757af32ad6b572f4b6d2a623b6f120aa0d9'
            'c18b6c28095a6195edfbf782c2e0f2caed59692d837d9cb4599ee0458f9ac658006c181ccda31cf078a7864676897163d6458e217c453bd637dadfe9ddd25d0b')

_game="minecraft"
_server_root="/srv/minecraft"

package() {
	install -Dm644 ${_game}d.conf              "${pkgdir}/etc/conf.d/${_game}"
	install -Dm755 ${_game}d.sh                "${pkgdir}/usr/bin/${_game}d"
	install -Dm644 ${_game}d.service           "${pkgdir}/usr/lib/systemd/system/${_game}d.service"
	install -Dm644 ${_game}d-backup.service    "${pkgdir}/usr/lib/systemd/system/${_game}d-backup.service"
	install -Dm644 ${_game}d-backup.timer      "${pkgdir}/usr/lib/systemd/system/${_game}d-backup.timer"
	install -Dm644 ${_game}d.sysusers          "${pkgdir}/usr/lib/sysusers.d/${_game}d.conf"
	install -Dm644 ${_game}d.tmpfiles          "${pkgdir}/usr/lib/tmpfiles.d/${_game}d.conf"
	install -Dm644 ${_game}_server.${pkgver}.jar "${pkgdir}${_server_root}/${_game}_server.${pkgver}.jar"
	ln -s "${_game}_server.${pkgver}.jar" "${pkgdir}${_server_root}/${_game}_server.jar"

	# Link the log files
	mkdir -p "${pkgdir}/var/log/"
	install -dm2755 "${pkgdir}/${_server_root}/logs"
	ln -s "${_server_root}/logs" "${pkgdir}/var/log/${_game}"

	# Give the group write permissions and set user or group ID on execution
	chmod g+ws "${pkgdir}${_server_root}"
}
