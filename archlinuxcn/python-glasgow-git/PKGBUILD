# Maintainer: Markus Koch <markus@notsyncing.net>

pkgname=python-glasgow-git
pkgver=0.2253
pkgrel=1
pkgdesc="Software for the Glasgow Interface Explorer, the Scots Army Knife for electronics"
arch=('any')
url='https://github.com/GlasgowEmbedded/glasgow.git'
license=('0BSD' 'Apache-2.0')
depends=(python python-pyvcd python-libusb1 python-fx2 python-amaranth yosys nextpnr icestorm)
optdepends=('python-aiohttp: For specific plugins (applets, loggers, etc.)',
	    'python-aiohttp_remotes: For specific plugins (applets, loggers, etc.)'
)
makedepends=('python-build' 'python-pdm' 'python-pdm-backend')
source=("git+https://github.com/GlasgowEmbedded/glasgow.git")
sha256sums=('SKIP')
provides=(python-glasgow)
conflicts=(python-glasgow)

pkgver() {
	cd "$srcdir/glasgow"
	#git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
	git rev-list HEAD --count | sed "s/^/0./"
}

prepare() {
	cd "$srcdir/glasgow"

	git submodule update --init
}

build() {
	cd "$srcdir/glasgow/software"

	python -m build --wheel --no-isolation
}

package() {
	cd "$srcdir/glasgow/software"

	python -m installer --destdir="$pkgdir" dist/*.whl

	install -Dm 644 $srcdir/glasgow/config/70-glasgow.rules $pkgdir/etc/udev/rules.d/70-glasgow.rules
}
