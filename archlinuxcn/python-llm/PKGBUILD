# Maintainer: Cameron Otsuka <cameron@otsuka.haus>
# Contributor: Cameron Otsuka <cameron@otsuka.haus>
# Contributor: Martin Harrigan <martinharrigan at gmail.com>
pkgname="python-llm"
_name=${pkgname#python-}
pkgver="0.37.2"
pkgrel=1
pkgdesc="Access large language models from the command-line"
arch=("any")
url="https://github.com/simonw/llm"
license=("Apache-2.0")
depends=("python" "python-click" "python-openai" "python-click-default-group" "python-httpx2" "python-condense-json" "sqlite-utils" "python-pydantic" "python-pyyaml" "python-pluggy" "python-ulid" "python-puremagic")
makedepends=("python-build" "python-installer" "python-setuptools" "python-wheel")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/simonw/llm/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('7c4f434914be615ab232b53d11bef27a97c41e8f3f29dfd5648d6eaa8ac35d60')

build() {
	cd "${_name}-${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "${_name}-${pkgver}"
	python -m installer --destdir="$pkgdir" dist/*.whl
}
