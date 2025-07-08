# Maintainer Chris Werner Rau <aur@cwrau.io>
# Maintainer: Robin Broda <robin at broda dot me>

pkgname=glava
pkgver=1.6.3 # renovate: datasource=github-tags depName=wacossusca34/glava
pkgrel=5
pkgdesc='OpenGL audio spectrum visualizer'
arch=('x86_64')
url='https://github.com/wacossusca34/glava'
license=('GPL3')
depends=('libpulse' 'libx11' 'libxcomposite' 'libxext' 'libxrender' 'pulse-native-provider' 'x-server')
makedepends=('git' 'libpulse' 'libx11' 'libxcomposite' 'libxext' 'libxrender' 'python')
source=("git+https://github.com/wacossusca34/glava#tag=v${pkgver}")
b2sums=('426ab5e654ba677379a98d15b629eeb9fc86d1c067f4dde20a1a1686276097a78a75cc01e6b032564a291c1bec1c4bd0a71d044fcf1bcb87f3209f5e5c035418')

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
