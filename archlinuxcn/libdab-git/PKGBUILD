# Maintainer: xiretza <xiretza+aur@xiretza.xyz>
_pkgname=dab-cmdline
pkgname=libdab-git
pkgver=r333.d996709
pkgrel=2
pkgdesc="DAB decoding library"
arch=(x86_64)
url="https://github.com/JvanKatwijk/dab-cmdline"
license=('GPL')
depends=('fftw' 'faad2')
makedepends=('cmake' 'git')
provides=("${pkgname%-git}" 'libdab_lib.so')
conflicts=("${pkgname%-git}")
source=("git+$url.git")
sha256sums=('SKIP')

pkgver() {
	cd "$_pkgname"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
	cmake -B build -S "$_pkgname/library" \
		-Wno-dev \
		-DCMAKE_BUILD_TYPE='None' \
		-DCMAKE_INSTALL_PREFIX=/usr
	make -C build
}

package() {
	make -C build DESTDIR="$pkgdir/" install
}
