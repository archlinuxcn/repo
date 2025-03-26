# Maintainer: Otreblan <otreblain@gmail.com>

pkgname=cmake-language-server
pkgver=0.1.11
pkgrel=1
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
sha256sums=('67c0ae4749d367f5f3c79f969ae1355f6dac6c287ac9bbfb2e2adcfbe57f7013')

build() {
	cd "$srcdir/$pkgname-$pkgver"

	PDM_BUILD_SCM_VERSION="$pkgver" python -m build --wheel --no-isolation
}

package() {
	cd "$srcdir/$pkgname-$pkgver"

	python -m installer --destdir="$pkgdir" dist/*.whl
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
