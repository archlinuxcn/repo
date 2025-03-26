# Maintainer: Robin Broda <robin at broda dot me>

pkgname=glava
pkgver=1.6.3
pkgrel=3
pkgdesc='OpenGL audio spectrum visualizer'
arch=('x86_64')
url='https://github.com/wacossusca34/glava'
license=('GPL3')
depends=('x-server' 'pulse-native-provider' 'libxext' 'libxcomposite' 'libxrender')
makedepends=('git' 'python')
_commit=094dec9b009268814751d3801fc7a5068381c90b  # tags/v1.6.3
source=("git+https://github.com/wacossusca34/glava#commit=${_commit}")
b2sums=('SKIP')

pkgver() {
	cd "${pkgname}"
	git describe --tags | sed 's/^v//;s/[^-]*-g/r&/;s/-/+/g'
}

prepare() {
	cd "${pkgname}"
}

build() {
	cd "${pkgname}"

	make
}

package() {
	cd "${pkgname}"

	make DESTDIR="${pkgdir}/" install
}
