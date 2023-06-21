# Maintainer: Oleksandr Natalenko <oleksandr@natalenko.name>

pkgname=7-zip
pkgver=23.01
pkgrel=1
pkgdesc="File archiver with a high compression ratio"
url=https://7-zip.org
license=('LGPL' 'BSD' 'custom:unRAR')
arch=(x86_64)
makedepends=(uasm meson)
source=(${url}/a/7z2301-src.tar.xz
		meson.build)
sha256sums=('356071007360e5a1824d9904993e8b2480b51b570e8c9faf7c0f58ebe4bf9f74'
            '211a57a476943e654de7408145b8d626a4dc242e74a3dcb8fc3afd0620792a03')

build() {
	arch-meson . build

	meson compile -C build
}

package() {
	meson install -C build --destdir "${pkgdir}"
}

