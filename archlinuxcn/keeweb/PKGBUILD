# Maintainer: surefire@cryptomile.net

pkgname=keeweb
pkgver=1.10.0
pkgrel=2
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
	'hide-menubar.patch'
	'keeweb.sh'
	'package.json.patch.js'
)

sha1sums=('SKIP'
          'a55c2ed276c6073b7954452cdc88209633d51ace'
          'c925527f25e732d58438ee16b1c93b33be7bf9c4'
          '914afdd9651e71091d4b927cabd25d75786ec7d4')

prepare() {
	cd "${pkgname}"

	patch -Np1 -i ../hide-menubar.patch

	# remove extra dependencies
	node ../package.json.patch.js

	sed -i \
		-e "/const electronVersion/       s/pkg.dependencies.electron/'$(</usr/lib/electron/version)'/" \
	Gruntfile.js

	sed -i \
		-e "/'eslint',/                 d" \
		-e "/'uglify',/                 d" \
	grunt.tasks.js

	sed -i \
		-e '/Exec=/ c \Exec=keeweb %u' \
	package/deb/usr/share/applications/keeweb.desktop

	sed -i \
		-e 's/: "[^@]*@github:/: "github:/' \
	package-lock.json
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

	install -Dm0644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE DEPS-LICENSE

	install -Dm0644 -t "${pkgdir}/usr/share/mime/packages" package/deb/usr/share/mime/packages/keeweb.xml
	install -Dm0644 -t "${pkgdir}/usr/share/applications"  package/deb/usr/share/applications/keeweb.desktop

	install -Dm0644 graphics/128x128.png "${pkgdir}/usr/share/pixmaps/keeweb.png"
}
