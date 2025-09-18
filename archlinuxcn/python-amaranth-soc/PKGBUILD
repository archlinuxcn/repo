# Maintainer: Scott Alfter <scott@alfter.us>

_pkgname=amaranth-soc
_git_commit=5c43cf58f15d9cd9c69ff83c97997708d386b2dc
pkgname="python-$_pkgname"
pkgver=0.1a.r24.g5c43cf5
pkgrel=1
pkgdesc="System on Chip toolkit for Amaranth"
arch=(any)
url="https://github.com/amaranth-lang/amaranth-soc"
license=('BSD-2')
depends=('python-amaranth')
makedepends=('git' 'python-build' 'python-installer' 'python-wheel' 'python-setuptools-scm' 'python-pdm-backend') # 'python-jschon')
optdepends=('python-paramiko: for remote builds')
# FIXME: symbiyosys
provides=("python-$_pkgname=$pkgver")
source=(
	"git+$url.git" 
	)
sha256sums=(
	'SKIP' 
	)

pkgver() {
	cd "$_pkgname"

	git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare()
{
	cd "$_pkgname"
	git checkout $_git_commit
	sed -i -e "s/pdm\\.backend\\._vendor\\.//" pdm_build.py
}

build() {
	cd "$_pkgname"

	python -m build --wheel --no-isolation
}

package() {
	cd "$_pkgname"

	python -m installer --destdir="$pkgdir" dist/*.whl

	install -Dm 644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
