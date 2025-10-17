# Maintainer: Manuel Hüsers <aur@huesers.de>

pkgname=discord-electron-openasar
_pkgname=discord
pkgver=0.0.112+846
_pkgver=${pkgver%%+*}
pkgrel=3
_electronver=38
_electronname="electron${_electronver}"
pkgdesc="Discord packaged with OpenAsar using system provided electron (v${_electronver}) for increased security and performance"
arch=('x86_64')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
url='https://discord.com'
license=('custom')
options=('!strip')
install="$pkgname.install"
depends=("${_electronname}" 'libxss' 'unzip')
makedepends=('git' 'asar' 'nodejs' 'curl')
optdepends=(
	'libpulse: Pulseaudio support'
	'libappindicator-gtk3: Systray indicator support'
	'xdg-utils: Open files'
	'python-pyelftools: Required for Krisp patcher'
	'python-capstone: Required for Krisp patcher'
)
source=("https://dl.discordapp.net/apps/linux/${_pkgver}/${_pkgname}-${_pkgver}.tar.gz"
	'discord-launcher.sh'
	'krisp-patcher.py' # original: https://github.com/sersorrel/sys/blob/main/hm/discord/krisp-patcher.py
	"git+https://github.com/goosemod/openasar.git#commit=bf8a71e2fcf1c77761092b7b899839164e3a596c")
sha512sums=('5b37b63c3fbc2ea55a1cfc9c4bfc26f73e896c1978f9dcecf0735d385e76f4ae7f7107947f8939efc0eaac7dca7a951eba13ad953329244a4935cd2b92b8065c'
            'c3152d7d36d5acf77facd5b280ba696ef9f1c7489646174269b90c4f00fed04d734d5e831d11c15936ba3b530ae4162ff255accd5e39f81ac0c07a07da9fefbb'
            '42cef68c1f7d574b4fbe859a4dc616e8994c7d16f62bcae3ff1f88e1edc58ac37b39c238d7defa9c97ceda417fcd6224cf0a0fd2608b8d18d0877e3c1befa59c'
            'b25328161b958683c60a33c3295577286057e724449e932eea828169c65b6e1103a2dcfc83deb088119e8b8b49871b7cd355d489c4d713aeac837b91f7a40a1e')

# just in case I get the version wrong
pkgver() {
	cd "${srcdir}/openasar"
	printf "%s+%s" "$_pkgver" "$(git rev-list --count HEAD)"
}

prepare() {
	# prepare launcher script
	sed -i -e "s|@PKGNAME@|${_pkgname}|g" \
		-e "s|@PKGVER@|${_pkgver}|g" \
		-e "s|@ELECTRON@|${_electronname}|g" \
		discord-launcher.sh

	# fix the .desktop file
	sed -i -e "s|Exec=.*|Exec=/usr/bin/${_pkgname}|" ${_pkgname^}/$_pkgname.desktop

	# create the license files
	curl -o LICENSE.html https://discord.com/terms
	curl -o OSS-LICENSES.html https://discord.com/licenses
}

build() {
	cd "${srcdir}"/openasar

	# pack openasar
	sed -i -e "s|nightly|nightly-$(git rev-parse HEAD | cut -c 1-7)|" src/index.js
	sed -i -e "/config.setup = true/a\  config.autoupdate = false;" src/config/index.js
	sed -i -e "s|process.resourcesPath|'/usr/lib/${_pkgname}/resources'|" src/utils/buildInfo.js
	sed -i -e "s|^Exec=\${exec}$|Exec=/usr/bin/${_pkgname}|" \
		-e "s|^Name=\${basename(exec)}$|Name=${_pkgname^}|" src/autoStart.js
	node scripts/strip.js
	asar p src app.asar
}

package() {
	# create necessary directories
	install -d "${pkgdir}"/usr/lib/$_pkgname

	# copy relevant data
	cp -r ${_pkgname^}/resources "${pkgdir}"/usr/lib/$_pkgname/

	# intall icon and desktop file
	install -Dm 644 ${_pkgname^}/$_pkgname.png "${pkgdir}"/usr/share/pixmaps/$_pkgname.png
	install -Dm 644 ${_pkgname^}/$_pkgname.desktop "${pkgdir}"/usr/share/applications/$_pkgname.desktop

	# overwrite Discord asar
	install -Dm 644 openasar/app.asar "${pkgdir}"/usr/lib/$_pkgname/resources/

	# install the launch script
	install -Dm 755 discord-launcher.sh "${pkgdir}"/usr/bin/$_pkgname

	# install krisp patcher
	install -Dm 644 krisp-patcher.py "${pkgdir}"/usr/lib/$_pkgname/

	# install licenses
	install -Dm 644 LICENSE.html "${pkgdir}"/usr/share/licenses/$_pkgname/LICENSE.html
	install -Dm 644 OSS-LICENSES.html "${pkgdir}"/usr/share/licenses/$_pkgname/OSS-LICENSES.html
}
