# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=python-skia-pathops
_pkgname=${pkgname#python-}
pkgver=0.8.0.post2
pkgrel=3
pkgdesc='Python bindings for the Skia library’s Path Ops (wheel)'
arch=(x86_64)
url="https://github.com/fonttools/$_pkgname"
license=(BSD-3-Clause)
depends=(python)
makedepends=(python-installer)
options=(!strip)
_py=cp313
_wheel="${_pkgname/-/_}-$pkgver-$_py-$_py-manylinux_2_17_$CARCH.manylinux2014_$CARCH.whl"
source=("https://files.pythonhosted.org/packages/$_py/${_pkgname::1}/$_pkgname/$_wheel")
sha256sums=('7db6b12d5cd85d0dec27f8f4ff41f8e2befa76a40170cda9715f98d2002d0da1')

# If anybody wants to mess around with the Chromium tree and figure out how to
# build skia from source on Arch I'm open to patches, but even after mucking
# around with ninja and python2 and various patched build toolchains I have
# come up short of a way to build this against Arch packages as dependencies.
# Drop a comment on the AUR page if you have ideas.

package() {
	python -m installer --destdir="$pkgdir" $_wheel
	python -O -m compileall "$pkgdir"
}
