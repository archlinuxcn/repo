# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=python-skia-pathops
_pkgname=${pkgname#python-}
pkgver=0.9.2
pkgrel=1
pkgdesc='Python bindings for the Skia library’s Path Ops (wheel)'
arch=(x86_64)
url="https://github.com/fonttools/$_pkgname"
license=(BSD-3-Clause)
depends=(python)
makedepends=(python-installer)
options=(!strip)
_py=cp310
_wheel="${_pkgname/-/_}-${pkgver}-${_py}-abi3-manylinux2014_${CARCH}.manylinux_2_17_${CARCH}.whl"
source=("https://files.pythonhosted.org/packages/$_py/${_pkgname::1}/$_pkgname/$_wheel")
sha256sums=('d94c18a60b1e56910240a65dcc841cca37067f6432a4881d20baff17b6d77915')

# If anybody wants to mess around with the Chromium tree and figure out how to
# build skia from source on Arch I'm open to patches, but even after mucking
# around with ninja and python2 and various patched build toolchains I have
# come up short of a way to build this against Arch packages as dependencies.
# Drop a comment on the AUR page if you have ideas.

package() {
	python -m installer --destdir="$pkgdir" $_wheel
	python -O -m compileall "$pkgdir"
}
