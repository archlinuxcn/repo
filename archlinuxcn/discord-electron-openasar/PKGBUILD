# Maintainer: Manuel Hüsers <aur@huesers.de>

pkgname=discord-electron-openasar
_pkgname=discord
pkgver=0.0.106+837
_pkgver=${pkgver%%+*}
pkgrel=1
_electronver=37
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
	"git+https://github.com/goosemod/openasar.git#commit=92abbb0e3efc39e553fd24e9125c42cdba1318ec")
sha512sums=('972d6ff124260c2d4f7b07845095c9738847b92a9d6e9f8914b8f3ddd21a232d454ea7f27e3e16f380a415bf28d46e437ccea3bf4edc8e9c1858de83ce69dbe1'
            'd996494c6c606de01814c68954613afc009957ac8a539b4331c87fe40c79927f09470c7e6d8bbc07411413bb91592818c98bcea49972703ec13a2f94efbc488e'
            '42cef68c1f7d574b4fbe859a4dc616e8994c7d16f62bcae3ff1f88e1edc58ac37b39c238d7defa9c97ceda417fcd6224cf0a0fd2608b8d18d0877e3c1befa59c'
            '855c53c067eca6b27791de7b4d859d5566daf1a85361d8fff1e6ecc3a3dd07560f248b4a2f1da5a788af5c22409b6bb4701fba935da3dc2f98b984a842fc8b92')

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
