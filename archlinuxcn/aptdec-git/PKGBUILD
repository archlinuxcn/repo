# Maintainer: xiretza <xiretza+aur@xiretza.xyz>
# Contributor: Shuyuan Liu (AUR)

pkgname=aptdec-git
pkgver=r212.4d4a0c9
pkgrel=1
pkgdesc='NOAA APT satellite imagery decoder'
arch=('x86_64' 'arm' 'aarch64')
url="https://github.com/Xerbo/aptdec"
license=('GPL2')
depends=('libsndfile' 'libpng')
makedepends=('git' 'cmake')
provides=('aptdec')
conflicts=('aptdec')
source=(
	"git+$url"
	"git+https://github.com/cofyc/argparse"
)
sha256sums=('SKIP'
            'SKIP')

pkgver() {
	cd aptdec
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
    cd aptdec

    git submodule init
    git config submodule.src/argparse.url "$srcdir/argparse"
    git -c protocol.file.allow=always submodule update
}

build() {
	cmake -B build -S aptdec \
		-DCMAKE_BUILD_TYPE=None \
		-DCMAKE_INSTALL_PREFIX='/usr'
	make -C build
}

package() {
	make -C build DESTDIR="$pkgdir/" install
}

# vim: set et ts=4:
