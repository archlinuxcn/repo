# Maintainer: Oleksandr Natalenko <oleksandr@natalenko.name>

pkgname=7-zip
pkgver=22.01
pkgrel=2
pkgdesc="File archiver with a high compression ratio"
url=https://7-zip.org
license=('LGPL' 'BSD' 'custom:unRAR')
arch=(x86_64)
makedepends=(uasm meson)
source=(${url}/a/7z2201-src.tar.xz
		meson.build)
sha256sums=('393098730c70042392af808917e765945dc2437dee7aae3cfcc4966eb920fbc5'
            '8b47dd17a5094b487dc343f00113db3c08e94e929a494fbd582bd8c067e539e3')

build() {
	arch-meson . build

	meson compile -C build
}

package() {
	meson install -C build --destdir "${pkgdir}"
}

