# Maintainer: surefire@cryptomile.net

pkgname=keeweb
pkgver=1.15.5
pkgrel=1
pkgdesc="Desktop password manager compatible with KeePass databases"
arch=('any')
url="https://keeweb.info"
license=('MIT')
depends=('electron')
makedepends=(
	'asar'
	'git'
	'libsass>=3.5.5'
	'nodejs>=8.15.0'
	'npm'
	'python2'
)
optdepends=('xdotool: for auto-type')
conflicts=('keeweb-desktop')
source=(
	"${pkgname}::git+https://github.com/keeweb/keeweb.git#tag=v${pkgver}"
	'keeweb.sh'
	'package.json.patch.js'
)

sha1sums=('SKIP'
          'c925527f25e732d58438ee16b1c93b33be7bf9c4'
          'd64a29202b71f30b1c4eaef5c01cee574b55894a')

case "$CARCH" in
	i686)    _keeweb_arch=ia32;;
	x86_64)  _keeweb_arch=x64;;
	aarch64) _keeweb_arch=arm64;;
	*)       _keeweb_arch=DUMMY;;
esac

prepare() {
	cd "${pkgname}"

	# remove extra dependencies
	node ../package.json.patch.js

	sed -i \
		-e "/const electronVersion/  s/pkg.dependencies.electron/'$(</usr/lib/electron/version)'/" \
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
	cd "${pkgname}"

	export SKIP_SASS_BINARY_DOWNLOAD_FOR_CI=1
	export SASS_FORCE_BUILD=1
	export LIBSASS_EXT=auto
	export npm_config_nodedir=/usr
	export npm_config_optional=false
	export npm_config_build_from_source=true

	npm install
	npm install css-loader

	npx grunt build-web-app build-desktop-app-content

	asar p tmp/desktop/app tmp/app.asar
}

package() {
	cd "${pkgname}"

	install -Dm0755 ../keeweb.sh "${pkgdir}/usr/bin/keeweb"
	install -Dm0644 -t "${pkgdir}/usr/lib/keeweb" tmp/app.asar

	#TODO: requires a rebuild from source code
	install -Dm0644 -t "${pkgdir}/usr/lib/keeweb/node_modules/@keeweb/keeweb-native-modules" node_modules/@keeweb/keeweb-native-modules/*-linux-${_keeweb_arch}.node

	install -Dm0644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE DEPS-LICENSE

	install -Dm0644 -t "${pkgdir}/usr/share/mime/packages" package/deb/usr/share/mime/packages/keeweb.xml
	install -Dm0644 -t "${pkgdir}/usr/share/applications"  package/deb/usr/share/applications/keeweb.desktop

	install -Dm0644 graphics/128x128.png "${pkgdir}/usr/share/pixmaps/keeweb.png"
}
