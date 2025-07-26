# Maintainer: Kimiblock Moe
# Contributor: Francesco Masala <mail@francescomasala.me>
# Contributor: lotation <xlapsiu@gmail.com>

pkgname=bottles-bwrap
_pkgname=Bottles
pkgver=51.21
pkgrel=1
epoch=2
pkgdesc='Easily manage wine and proton prefix. Sandboxed by portable.'
arch=(any)
url="https://github.com/bottlesdevs/Bottles"
license=(GPL-3.0-only)
provides+=(bottles)
conflicts+=(bottles)
depends=(
	cabextract
	dconf
	gtk4
	gtksourceview5
	hicolor-icon-theme
	icoextract
	imagemagick
	libadwaita
	libportal-gtk4
	p7zip
	patool
	python
	python-chardet
	python-fvs
	python-gobject
	python-markdown
	python-orjson
	python-pathvalidate
	python-pycurl
	python-requests
	python-steamgriddb
	python-yaml
	webkit2gtk
	xorg-xdpyinfo
	vkbasalt-cli
	portable
	gamemode
)

optdepends=(
	gvfs
	lib32-gamemode
	lib32-gnutls
	lib32-vkd3d
	lib32-vulkan-icd-loader
	vkd3d
	vulkan-icd-loader
	wine
)
makedepends=(
	blueprint-compiler
	meson
	ninja
	git
)
source=(
	"Bottles::git+https://github.com/bottlesdevs/Bottles.git#tag=${pkgver}"
	disable-flatpak-check.patch
	portable-config
	start.sh
)
sha256sums=('3f341e90c88f2d48d0b1899cd5141cb5599e154a81a57c398991e67d320b70f5'
            '012f00b6678ff20bb0a43c592c8f6b6af0d315053bf0473aa3f3b56c74845b73'
            '27902d2558373e9a1129702d2cfb27a2b608430b3e88f73868fbd61da57f74f4'
            '6441bfac93fa2a859eb4a78e6e818d972787abc4190aea0032a331c153696f27')

function prepare() {
	patch --forward --directory="${srcdir}/${_pkgname}" --strip=1 --input="${srcdir}/disable-flatpak-check.patch"
}

build() {
	cd "${srcdir}/${_pkgname}"
	meson setup --prefix='/usr' build
	ninja -C build
}

package() {
	install -vDm755 "${srcdir}/portable-config" \
		"${pkgdir}/usr/lib/portable/info/com.usebottles.bottles/config"
	install -vDm755 "${srcdir}/start.sh" \
		"${pkgdir}/usr/bin/bottles-bwrap"
	cd "${srcdir}/${_pkgname}"
	DESTDIR="${pkgdir}" ninja -C build install
	install -d "${pkgdir}/usr/lib/bottles-bwrap"
	mv ${pkgdir}/usr/bin/bottles{,-cli} "${pkgdir}/usr/lib/bottles-bwrap"
	ln -srf "${pkgdir}/usr/bin/bottles-bwrap" "${pkgdir}/usr/bin/bottles"
}
