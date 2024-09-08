# Maintainer: Martin Rys <https://rys.rs/contact> | Toss a coin on https://rys.rs/donate

pkgname=sc-controller
pkgver=0.4.8.21
pkgrel=1
pkgdesc='User-mode driver and GTK3 based GUI for Steam Controller'
arch=('x86_64' 'aarch64')
url='https://github.com/C0rn3j/sc-controller'
license=('GPL-2.0-only')
depends=(
	'gtk3'
	'gtk-layer-shell'
	'libayatana-appindicator'
	'python-cairo'
	'python-evdev'
	'python-gobject'
	'python-pylibacl'
	'python-setuptools'
	'python-vdf'
	'xorg-xinput'
)
conflicts=("${pkgname}-git" 'scc')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/C0rn3j/sc-controller/archive/v${pkgver}.tar.gz")
sha256sums=('d02b3407531b23c96e52d3e7f0e525502a0dbc6c714e61c368c143e8b2e5b428')

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	python setup.py build
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	python setup.py install --root="${pkgdir}" --optimize=1
}
