# vim: noexpandtab tabstop=4 shiftwidth=4 softtabstop=4
# Maintainer: Peter Cai <peter@typeblog.net>
# Contributor: <surefire@cryptomile.net>

pkgname=keeweb
pkgver=1.18.7
_electron=electron12
pkgrel=1
pkgdesc="Desktop password manager compatible with KeePass databases"
arch=('any')
url="https://keeweb.info"
license=('MIT')
depends=(
	"$_electron"
	'org.freedesktop.secrets'
)
makedepends=(
	'asar'
	'git'
	'libsass'
	'npm'
	'nodejs'
	'cmake'
)
conflicts=('keeweb-desktop')
source=(
	"${pkgname}::git+https://github.com/keeweb/keeweb.git#tag=v${pkgver}"
	"git+https://github.com/keeweb/keeweb-native-modules.git#tag=0.11.7"
	"git+https://github.com/keeweb/keeweb-connect.git#tag=0.3.7"
	'package.json.patch.js'
	'67e917af3dcd9d78273774e7061f74d893b5523b.patch'
)

sha1sums=('SKIP'
          'SKIP'
          'SKIP'
          '679f19fcdff4a8df49bb0bd8ee09eab1784cf264'
          '3b6341f657421899d4e4078b799bece7d93587e5')

case "$CARCH" in
	i686)    _arch=ia32;;
	x86_64)  _arch=x64;;
	aarch64) _arch=arm64;;
	*)       _arch=DUMMY;;
esac

prepare() {
	cd "${srcdir}/${pkgname}"

	# remove extra dependencies
	node ../package.json.patch.js

	sed -i \
		-e "/const electronVersion/  s/pkg.dependencies.electron/'$(</usr/lib/${_electron}/version)'/" \
	Gruntfile.js

	sed -i \
		-e "/'eslint',/  d" \
	grunt.tasks.js

	sed -i \
		-e "/const BundleAnalyzerPlugin/              d" \
		-e "/new BundleAnalyzerPlugin({$/, /^\s*})$/  d" \
	build/webpack.config.js

	# Patch `getNativeMessagingHostPath` to not rely on the executable path
	# (in our case, the executable path is the system electron binary)
	sed -i \
		-e 's@function getNativeMessagingHostPath() {@function getNativeMessagingHostPath() {\nreturn "/usr/lib/keeweb/keeweb-native-messaging-host";@' \
	desktop/scripts/util/browser-extension-installer.js
}

build() {
	export npm_config_build_from_source=true
	export npm_config_optional=false

	cd "${srcdir}/${pkgname}"

	SKIP_SASS_BINARY_DOWNLOAD_FOR_CI=1 \
	SASS_FORCE_BUILD=1 \
	LIBSASS_EXT=auto \
	npm install --nodedir=/usr

	npx grunt build-web-app build-desktop-app-content

	asar p tmp/desktop/app tmp/desktop/app.asar

	cat <<-EOF > tmp/desktop/keeweb
		#!/usr/bin/sh
		exec ${_electron} /usr/lib/keeweb/app.asar --disable-updater "\$@"
	EOF

	cd "${srcdir}/keeweb-native-modules"

	npm install --ignore-scripts

	# https://github.com/antelle/keyboard-auto-type/commit/67e917af3dcd9d78273774e7061f74d893b5523b
	patch -Np1 <"${srcdir}/67e917af3dcd9d78273774e7061f74d893b5523b.patch"

	HOME="${srcdir}/.electron-gyp" \
	npx electron-rebuild --arch="${_arch}" --version="$(</usr/lib/${_electron}/version)" --only=argon2,keytar,usb-detection,yubikey-chalresp,keyboard-auto-type

	cd "${srcdir}/keeweb-connect/native-messaging-host"
	make
}

package() {
	cd "${srcdir}/${pkgname}"

	install -Dm0755 -t "${pkgdir}/usr/bin" tmp/desktop/keeweb
	install -Dm0755 -t "${pkgdir}/usr/lib/keeweb" ../keeweb-connect/native-messaging-host/build/keeweb-native-messaging-host
	install -Dm0644 -t "${pkgdir}/usr/lib/keeweb" tmp/desktop/app.asar
	install -Dm0644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE DEPS-LICENSE
	install -Dm0644 -t "${pkgdir}/usr/share/mime/packages" package/deb/usr/share/mime/packages/keeweb.xml
	install -Dm0644 -t "${pkgdir}/usr/share/applications"  package/deb/usr/share/applications/keeweb.desktop

	install -Dm0644 graphics/128x128.png "${pkgdir}/usr/share/pixmaps/keeweb.png"

	local _src_mdir="${srcdir}/keeweb-native-modules/node_modules"
	local _pkg_mdir="${pkgdir}/usr/lib/keeweb/node_modules/@keeweb/keeweb-native-modules"

	install -Dm0644 "${_src_mdir}/usb-detection/build/Release/detection.node" \
		"${_pkg_mdir}/usb-detection-linux-${_arch}.node"

	for _mod in argon2 keyboard-auto-type keytar yubikey-chalresp; do
		install -Dm0644 "${_src_mdir}/${_mod}/build/Release/${_mod}.node" \
			"${_pkg_mdir}/${_mod}-linux-${_arch}.node"
	done
}
