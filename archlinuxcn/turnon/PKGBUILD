# Maintainer: Kimiblock Moe

pkgname=turnon
pkgdesc="Turn on devices in your local network"
url="https://codeberg.org/swsnr/turnon"
license=("EUPL-1.2")
arch=("x86_64" "aarch64")
pkgver=3.0.3
pkgrel=1
makedepends=(python-wheel git python-installer python-hatchling python-build blueprint-compiler)
checkdepends=(
	'python-pytest'
	'python-pytest-asyncio'
)
depends=(libadwaita gtk4 hicolor-icon-theme graphene dconf gcc-libs glib2 glibc python-gobject python-packaging)
source=("source::git+https://codeberg.org/swsnr/turnon.git#tag=v${pkgver}")
md5sums=('cb704c717d3b6d4ab1811a03048ff3b3')

function prepare() {
	cd source
	git clean -fdx
}

function build() {
	cd source
	python -m build --wheel --skip-dependency-check --no-isolation
}

function check() {
	cd source
	python \
		-m venv \
		--clear \
		--without-pip \
		--system-site-packages \
		test-venv
	test-venv/bin/python -m installer dist/*.whl
	test-venv/bin/python -m pytest
}

function package() {
	cd source
	python -m installer --destdir="${pkgdir}" dist/*.whl
	ln -s "/usr/bin/de.swsnr.turnon" "${pkgdir}/usr/bin/turnon"
	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}



