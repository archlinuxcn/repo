# Maintainer: surefire@cryptomile.net

pkgname=keeweb
pkgver=1.16.4
_electron=electron
pkgrel=1
pkgdesc="Desktop password manager compatible with KeePass databases"
arch=('any')
url="https://keeweb.info"
license=('MIT')
depends=(
	$_electron
	'org.freedesktop.secrets'
)
makedepends=(
	'asar'
	'git'
	'libsass>=3.5.5'
	'npm'
	'python2'
)
optdepends=('xdotool: for auto-type')
conflicts=('keeweb-desktop')
source=(
	"${pkgname}::git+https://github.com/keeweb/keeweb.git#tag=v${pkgver}"
	"git+https://github.com/keeweb/keeweb-native-modules.git#tag=0.5.3"
	'package.json.patch.js'
)

sha1sums=('SKIP'
          'SKIP'
          '5e2a12694cf56ec9ed558554819dba0187e7fbdc')

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
}

build() {
	export npm_config_build_from_source=true
	export npm_config_optional=false

	cd "${srcdir}/${pkgname}"

	export SKIP_SASS_BINARY_DOWNLOAD_FOR_CI=1
	export SASS_FORCE_BUILD=1
	export LIBSASS_EXT=auto

	npm install --nodedir=/usr
	npm install css-loader

	npx grunt build-web-app build-desktop-app-content

	asar p tmp/desktop/app tmp/desktop/app.asar

	cat <<-EOF > tmp/desktop/keeweb
		#!/usr/bin/sh
		exec ${_electron} /usr/lib/keeweb/app.asar --disable-updater "\$@"
	EOF

	cd "${srcdir}/keeweb-native-modules"

	local electron_build_opts=(
		production
		arch=$_arch
		runtime=electron
		disturl=https://electronjs.org/headers
		target=$(</usr/lib/${_electron}/version)
		target_arch=$_arch
		use_system_libusb=true
	)

	HOME="${srcdir}/.electron-gyp" npm install "${electron_build_opts[@]/#/--}"
}

package() {
	cd "${srcdir}/${pkgname}"

	install -Dm0755 -t "${pkgdir}/usr/bin" tmp/desktop/keeweb
	install -Dm0644 -t "${pkgdir}/usr/lib/keeweb" tmp/desktop/app.asar
	install -Dm0644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE DEPS-LICENSE
	install -Dm0644 -t "${pkgdir}/usr/share/mime/packages" package/deb/usr/share/mime/packages/keeweb.xml
	install -Dm0644 -t "${pkgdir}/usr/share/applications"  package/deb/usr/share/applications/keeweb.desktop

	install -Dm0644 graphics/128x128.png "${pkgdir}/usr/share/pixmaps/keeweb.png"

	local _src_mdir="${srcdir}/keeweb-native-modules/node_modules"
	local _pkg_mdir="${pkgdir}/usr/lib/keeweb/node_modules/@keeweb/keeweb-native-modules"

	install -Dm0644 "${_src_mdir}/argon2/build-tmp-napi-v3/Release/argon2.node" \
		"${_pkg_mdir}/argon2-linux-${_arch}.node"
	install -Dm0644 "${_src_mdir}/keytar/build/Release/keytar.node" \
		"${_pkg_mdir}/keytar-linux-${_arch}.node"
	install -Dm0644 "${_src_mdir}/usb/build/Release/usb_bindings.node" \
		"${_pkg_mdir}/usb-linux-${_arch}.node"
	install -Dm0644 "${_src_mdir}/yubikey-chalresp/build/Release/yubikey-chalresp.node" \
		"${_pkg_mdir}/yubikey-chalresp-linux-${_arch}.node"
}
