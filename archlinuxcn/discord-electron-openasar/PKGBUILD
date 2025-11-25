# Maintainer: Manuel Hüsers <aur@huesers.de>

pkgname=discord-electron-openasar
_pkgname=discord
pkgver=0.0.116+847
_pkgver=${pkgver%%+*}
pkgrel=1
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
	'xdg-utils: Open files'
	'python-pyelftools: Required for Krisp patcher'
	'python-capstone: Required for Krisp patcher'
)
source=("https://dl.discordapp.net/apps/linux/${_pkgver}/${_pkgname}-${_pkgver}.tar.gz"
	'discord-launcher.sh'
	'krisp-patcher.py' # original: https://github.com/sersorrel/sys/blob/main/hm/discord/krisp-patcher.py
	"git+https://github.com/goosemod/openasar.git#commit=5b259e4efaf9eee69aeca7b2ef153e5bfedc35d0")
sha512sums=('801a228ff7c84aba76ce4565535d1da1d0ee3e7c30e2c381a118db32b2c7dcbdfe0f52ea8caa369732ca29c5a23a3ef7bb5439adc57e70243beb6ab7fc539a7f'
            '618c89fdd90d6826dd44c3d5973428fb68b1836f1198a356e936da0b78c18b748d522ff7ecee15752d590dcd137ef16c4370ac6325c5b5f0aced4b5cce36b825'
            '42cef68c1f7d574b4fbe859a4dc616e8994c7d16f62bcae3ff1f88e1edc58ac37b39c238d7defa9c97ceda417fcd6224cf0a0fd2608b8d18d0877e3c1befa59c'
            '86e296524f831b450620e4c0abb576f5b370982f70951beafdc821bcbce7db4b7b000bb2a7ce29516c209c2590fb428e8fed9450387ec37918dd79fc0a0a85e4')

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
