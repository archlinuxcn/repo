# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributer: Philip Abernethy <chais.z3r0@gmail.com>
# Contributer: sowieso <sowieso@dukun.de>

pkgname=minecraft-server
pkgver=1.16.4
_nonce=35139deedbd5182953cf1caa23835da59ca3d7cd
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
sha512sums=('2807168800da30e6e58a22fc9f1981b58be6ba986d12dc138c19013269fcf51976db21a0488c3a95468e4f8016646db3a9966ac2065f6950ba9b733056df47bd'
            'a10e38c0e9a09c25e23e46147a8b8ce4d88a62ee780c1c0b525b9e41a563c4a4ed8e94d851abc3936bc31f3faa916ef005543129a039f66878b8f2c34853b91d'
            '19ee3646bfbace353b65c0373594edb654de11c9671f29cebad3b31109f29f94ade1d529d9f409b0989c376bef9b451585b22a1e0ac4295fcc92d9565f808418'
            '5203f6331f740ecfcea2a2cc653603ae97419baa89e08512f9d8feb63e4a52978442a69b313eccd9037b676a62ab528e2b533c0fb95a9c7177318279fe0cde79'
            'a62c8c04e08dbac0db0aa2eeb505d70f8fd925bd2e427899512ba3ac828d4644e1c43c8d92325c6bc49c8d9ecb40cb5c44bf5957a63980b1e2cf86fdb38a05a7'
            '34a2ef48f6f2c7c384db7138d2255ae8cfacd755d2d135bd528cdfeb22ed45df707de7d812acf1ce073a54cc0b058beef81c97fc7099f01ef50cb4c757106d3f'
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
