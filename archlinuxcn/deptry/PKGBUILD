# Maintainer: Carl Smedstad <carsme@archlinux.org>

pkgname=deptry
pkgver=0.23.0
pkgrel=1
pkgdesc="Find unused, missing and transitive dependencies in a Python project"
arch=(x86_64)
url="https://github.com/fpgmaas/deptry"
license=(MIT)
depends=(
  gcc-libs
  glibc
  python
  python-click
  python-packaging
  python-requirements-parser
)
makedepends=(
  git
  python-build
  python-installer
  python-maturin
  python-wheel
)
checkdepends=(
  python-pdm
  python-poetry
  python-pytest
  python-pytest-xdist
  uv
)
source=("$pkgname::git+$url.git#tag=$pkgver")
sha256sums=('b4edf0f7e5e6004f45ba21980e6dd1796774f4f36635e8cca6428c94344686a9')

prepare() {
  cd $pkgname
  sed -i "s|^version = \".*\"|version = \"$pkgver\"|" pyproject.toml

  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd $pkgname
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  python -m build --wheel --no-isolation
}

check() {
  cd $pkgname
  # The functional tests expect the wheel to be here.
  mkdir -p build/functional_tests/deptry
  cp dist/*.whl build/functional_tests/deptry

  test -d test-env && rm -r test-env
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  # Deselected test fails due to Poetry error:
  #   The Poetry configuration is invalid:
  #     - The fields ['authors', 'description', 'name', 'version'] are required
  #       in package mode.
  test-env/bin/python -m pytest tests/ \
    --deselect tests/functional/cli/test_cli_poetry_pep_621.py::test_cli_with_poetry_pep_621
}

package() {
  cd $pkgname
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -vDm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE
}
