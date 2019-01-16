# Maintainer: Frantic1048 <archer@frantic1048.com>
pkgdesc='Plex HTTP Anidb Metadata Agent (HAMA)'
pkgname='plex-hama-bundle-git'
pkgver=r621.42c040f
pkgrel=1
makedepends=('git')
depends=('plex-media-server')
conflicts=('')
provides=('')
arch=('x86_64' 'i686')
url='https://github.com/ZeroQI/Hama.bundle'
license=('GPL3')
source=(
"${pkgname}::git+${url}"
"${url}/releases/download/v1.0/Plug-in.Support.folders.zip"
"https://raw.githubusercontent.com/ZeroQI/Absolute-Series-Scanner/master/Scanners/Series/Absolute%20Series%20Scanner.py"
)
sha512sums=('SKIP'
            '835ba0d4dd472c39dbb275fc9a6fb9d531e3d965fdd37d9ab82874ccdf2a8a415b75f1c5c7db0b316b12a390dd39188cc292804482ea9e6c15d448dd04628521'
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

	plugins_dir="${pkgdir}/var/lib/plex/Plex Media Server/Plug-ins/hama.bundle"
	install -d "$plugins_dir"
	cp -r ./$pkgname/* "$plugins_dir"

	plugins_support_dir="${pkgdir}/var/lib/plex/Plex Media Server/Plug-in Support"
	install -d "$plugins_support_dir"
	cp -r ./"Plug-in Support"/* "$plugins_support_dir"

	scanners_dir="${pkgdir}/var/lib/plex/Plex Media Server/Scanners/Series"
	install -d "$scanners_dir"
	cp "Absolute%20Series%20Scanner.py" "$scanners_dir"/"Absolute Series Scanner.py"
}
