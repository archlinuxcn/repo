# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Submitter: Schala Zeal <schalaalexiazeal@gmail.com>

pkgname=spigot
_pkgver=1.20.1
_build=157
pkgver="${_pkgver}+b${_build}"
pkgrel=1
_mng_ver=1.0.2
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
sha512sums=('043b30830ae3a4329cc4efe2fc364fff643188e8037e6783b65b8d5bb52669734e7f88b1bfaa666917c5d78d971ba717d4d034fd1e885ef19cef9f4bdb309689'
            '11d708d511b63e5541bcc1dbcaf29abbf7cb9583b1d313028770a39b26b41d48dcba023f7e1d6fe30f3c093d20e10a43363011edd432e5785a4580e5c5f852a6')

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
	chmod g+ws "${pkgdir}${_server_root}"

	# Make plugins folder ready for drag and drop
	install -dm2775 "${pkgdir}/${_server_root}/plugins"
}
