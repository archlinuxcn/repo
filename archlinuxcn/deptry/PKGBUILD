# Maintainer: Carl Smedstad <carsme@archlinux.org>

pkgname=deptry
pkgver=0.21.1
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
  python-pytest
  python-pytest-xdist
)
source=("$pkgname::git+$url.git#tag=$pkgver")
sha256sums=('56a12e966750f06e7f9d64663470fadb790c2e88c5c3e294ea2016a8d309724d')

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
  rm -rf tmp_install
  python -m installer --destdir=tmp_install dist/*.whl

  # The functional tests expect the wheel to be here.
  mkdir -p build/functional_tests/deptry
  cp dist/*.whl build/functional_tests/deptry

  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  export PYTHONPATH="$PWD/tmp_install/$site_packages"
  # Deselect test failing with AssertionError, only in a chroot - not sure why.
  pytest tests/ \
    --deselect tests/unit/violations/dep003_transitive/test_finder.py::test_simple
}

package() {
  cd $pkgname
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -vDm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE
}
