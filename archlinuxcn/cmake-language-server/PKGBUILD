# Maintainer: Otreblan <otreblain@gmail.com>

pkgname=cmake-language-server
pkgver=0.1.8
pkgrel=2
pkgdesc="Python based cmake language server"
arch=('any')
url="https://github.com/regen100/cmake-language-server"
license=('MIT')
groups=()
depends=("python-pygls" "python-pyparsing" "cmake-format" "cmake")
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
sha256sums=('799a1d69e14a8f9ce4a9f26470fd5cb8c61b6305c4f7d3dd97b9974744a32ebd')

build() {
	cd "$srcdir/$pkgname-$pkgver"

	PDM_BUILD_SCM_VERSION="$pkgver" python -m build --wheel --no-isolation
}

package() {
	cd "$srcdir/$pkgname-$pkgver"

	python -m installer --destdir="$pkgdir" dist/*.whl
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
