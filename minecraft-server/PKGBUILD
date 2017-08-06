# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributer: Philip Abernethy <chais.z3r0@gmail.com>
# Contributer: sowieso <sowieso@dukun.de>

pkgname=minecraft-server
pkgver=1.12.1
pkgrel=1
pkgdesc="Minecraft server unit files, script, and jar"
arch=('any')
url="https://minecraft.net/"
license=('custom')
depends=('java-runtime-headless=8' 'screen' 'sudo' 'bash' 'awk' 'sed')
optdepends=("tar: needed in order to create world backups"
	"netcat: required in order to suspend an idle server")
conflicts=('minecraft-server-systemd' 'minecraft-canary')
backup=('etc/conf.d/minecraft')
install="${pkgname}.install"
source=("https://s3.amazonaws.com/Minecraft.Download/versions/${pkgver}/minecraft_server.${pkgver}.jar"
	"minecraftd-backup.service"
	"minecraftd-backup.timer"
	"minecraftd.service"
	"minecraftd.conf"
	"minecraftd.sh")
noextract=("minecraft_server.${pkgver}.jar")
sha512sums=('ae715dcf729b28682ea77109d0fd01473812147de55b749508b8bddaa6d7c6153cb85f30c5d32955145fa3dea99c35a1158c137dab8793bd785a19fe5f948b9b'
            'c8f96bafb0ba3fd8946ac791b09e75cae54dc1a8e02822f91ca70a77a8ba45b253a83c4db30f9cfbf0658a2608b38e6de3d00f1d832ef676f329a78e69eab3e7'
            '19ee3646bfbace353b65c0373594edb654de11c9671f29cebad3b31109f29f94ade1d529d9f409b0989c376bef9b451585b22a1e0ac4295fcc92d9565f808418'
            'b0124c8cd90a4f9901a9105c0ee51eb3e7db944d106cf30fd91b29794178e650d3a21c3be3c8e0cb454b2cef6f27541c44e7a5e77a1d50f89b9152363de51d28'
            '73132ec613e05c8ed7ebe4eda2395f1ea0733ffe94ba7e203e06246d5852139bbfb7a9073b2b01891282339a2f85676699cd889cde79d6317066e27fd65b1d67'
            'b83b93a25d312825363eb85dec4b04379e9a3b2caf9faaf6f4958966900ecd2d2d5d8c5ecc25fca711da1dbf162129720bed419492ef8bf9dbb1649a5bdb1656')

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
