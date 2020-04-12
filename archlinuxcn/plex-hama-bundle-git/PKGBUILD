# Maintainer: Frantic1048 <archer@frantic1048.com>
pkgdesc='Plex HTTP Anidb Metadata Agent (HAMA)'
pkgname='plex-hama-bundle-git'
pkgver=r883.6ab37e2
pkgrel=1
makedepends=('git')
depends=('plex-media-server')
conflicts=()
provides=()
arch=('x86_64' 'i686')
url='https://github.com/ZeroQI/Hama.bundle'
license=('GPL3')
source=(
"${pkgname}::git+${url}"
"https://raw.githubusercontent.com/ZeroQI/Absolute-Series-Scanner/master/Scanners/Series/Absolute%20Series%20Scanner.py"
)
sha512sums=('SKIP'
            'SKIP')

pkgver () {
	cd "${pkgname}"
	(
		set -o pipefail
		git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
		printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
	)
}

build () {
	:
}

package () {
	cd "${srcdir}"

    #https://wiki.archlinux.org/index.php/plex#Plugins
	plex_main_folder="${pkgdir}/var/lib/plex/Plex Media Server"

	plugins_dir="${plex_main_folder}/Plug-ins/hama.bundle"
	install -d "$plugins_dir"
	cp -r ./$pkgname/* "$plugins_dir"

	scanners_dir="${plex_main_folder}/Scanners/Series"
	install -d "$scanners_dir"
	cp "Absolute%20Series%20Scanner.py" "$scanners_dir"/"Absolute Series Scanner.py"
}
