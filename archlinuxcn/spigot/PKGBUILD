# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Submitter: Schala Zeal <schalaalexiazeal@gmail.com>

pkgname=spigot
_pkgver=1.21.5
_build=191
pkgver="${_pkgver}+b${_build}"
pkgrel=1
_mng_ver=1.0.4
pkgdesc="High performance Minecraft server implementation"
arch=('any')
url="https://www.spigotmc.org/"
license=("LGPL")
depends=("java-runtime-headless>=17" 'tmux' 'sudo' 'fontconfig' 'bash' 'awk' 'sed')
optdepends=("tar: needed in order to create world backups"
	"netcat: required in order to suspend an idle server")
makedepends=("java-environment>=17" 'git')
provides=("minecraft-server=${_pkgver%_*}" "bukkit=${_pkgver%_*}" "craftbukkit=${_pkgver%_*}")
conflicts=("bukkit" "craftbukkit" "spigot-patcher")
backup=("etc/conf.d/${pkgname}")
install="${pkgname}.install"
source=("BuildTools-${_pkgver}+b${_build}.jar::https://hub.spigotmc.org/jenkins/job/BuildTools/${_build}/artifact/target/BuildTools.jar"
	"minecraft-server-${_mng_ver}.tar.gz"::"https://github.com/Edenhofer/minecraft-server/archive/refs/tags/v${_mng_ver}.tar.gz")
sha512sums=('1579cd2754bc9895d4bdfc2aae3e1b91a1373d8352d3b7a22f493b5fc6c7f24c19b8b4b20f7bd0f022f85a17ade9d47e275c7809cca77ca2870229ce2ecd5cfa'
            'dd4d68ca061c97a1e3cb5c0bb68439f7d8d45b15092344f3c4dbd4f7f39fef433d566670ad440970061007d93055183b570c7bf98f09c111ecdf8ab0f208f556')

_game="spigot"
_server_root="/srv/craftbukkit"

build() {
	export MAVEN_OPTS="-Xmx2g"
	java -jar "BuildTools-${_pkgver}+b${_build}.jar" --rev "${_pkgver}"

	make -C "${srcdir}/minecraft-server-${_mng_ver}" clean

	make -C "${srcdir}/minecraft-server-${_mng_ver}" \
		GAME=${_game} \
		INAME=${_game} \
		SERVER_ROOT=${_server_root} \
		BACKUP_PATHS="world world_nether world_the_end" \
		GAME_USER=craftbukkit \
		MAIN_EXECUTABLE=spigot.jar \
		SERVER_START_CMD="java -Xms512M -Xmx1024M -jar ./spigot.jar nogui" \
		all
}

package() {
	make -C "${srcdir}/minecraft-server-${_mng_ver}" \
		DESTDIR="${pkgdir}" \
		GAME=${_game} \
		INAME=${_game} \
		install

	install -Dm644 "${_game}-${_pkgver}.jar" "${pkgdir}${_server_root}/${_game}.${_pkgver}.jar"
	ln -s "${_game}.${_pkgver}.jar" "${pkgdir}${_server_root}/${_game}.jar"

	# Link the log files
	mkdir -p "${pkgdir}/var/log/"
	install -dm2775 "${pkgdir}/${_server_root}/logs"
	ln -s "${_server_root}/logs" "${pkgdir}/var/log/${_game}"

	# Give the group write permissions and set user or group ID on execution
	chmod g+s "${pkgdir}${_server_root}"

	# Make plugins folder ready for drag and drop
	install -dm2775 "${pkgdir}/${_server_root}/plugins"
}
