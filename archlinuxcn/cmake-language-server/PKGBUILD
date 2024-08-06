# Maintainer: Otreblan <otreblain@gmail.com>

pkgname=cmake-language-server
pkgver=0.1.10
pkgrel=3
pkgdesc="Python based cmake language server"
arch=('any')
url="https://github.com/regen100/cmake-language-server"
license=('MIT')
groups=()
depends=("python-pygls" "python-pyparsing" "cmake-format" "cmake" "python-pdm-backend")
makedepends=("python-build" "python-installer" "python-pdm" "python-pdm-pep517")
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
noextract=()
sha256sums=('8faaf3bce811b4de5b060a0b9eb664b18b506310d4e96b6b77f958dbb24b3639')

build() {
	cd "$srcdir/$pkgname-$pkgver"

	PDM_BUILD_SCM_VERSION="$pkgver" python -m build --wheel --no-isolation
}

package() {
	cd "$srcdir/$pkgname-$pkgver"

	python -m installer --destdir="$pkgdir" dist/*.whl
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
