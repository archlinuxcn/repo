# Maintainer: Kimiblock Moe
# Contributor: Francesco Masala <mail@francescomasala.me>
# Contributor: lotation <xlapsiu@gmail.com>

pkgname=bottles-bwrap
_pkgname=Bottles
pkgver=51.24
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
sha256sums=('c946c4316250ec311ffa0f7275f0604f4920a2d5a556d6da19c07acda711c40b'
            '95f644fff5b9579be60a391c49f16c3c765b6c02ebbffcf91e4001b3ffc7dd76'
            'afc4d4d5f8242f1f5cdb13845c4067b8bb28253ce7814bd7deeaf2c094ef89a4'
            'e8151fe783b4c202c99e206535f6f2b3e025b070d7237cb6f8bbb1f23ad0eb94')

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
