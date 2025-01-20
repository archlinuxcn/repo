# Maintainer: txtsd <aur.archlinux@ihavea.quest>
# Maintainer: Carl Smedstad <carsme@archlinux.org>
# Contributor: bpierre <benoit.pierre@gmail.com>
# Contributor: Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

pkgname=python-selenium
_pkgname="${pkgname#python-}"
pkgver=4.27.1
pkgrel=2
pkgdesc="Python language bindings for Selenium WebDriver"
arch=(x86_64)
url="https://github.com/SeleniumHQ/selenium"
license=(Apache-2.0)
depends=(
  bzip2
  gcc-libs
  glibc
  python
  python-certifi
  python-trio
  python-trio-websocket
  python-typing_extensions
  python-urllib3
  python-websocket-client
  zlib
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-setuptools-rust
  python-wheel
)
options=(!lto)
source=("https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('5296c425a75ff1b44d0d5199042b36a6d1ef76c04fb775b97b40be739a9caae2')

_archive="${_pkgname}-${pkgver}"

prepare() {
  cd "${_archive}"

  # Ensure `selenium.webdriver.common.fedcm` gets packaged
  touch ./selenium/webdriver/common/fedcm/__init__.py

  cd src
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd "${_archive}"
  export RUSTUP_TOOLCHAIN=stable
  python -m build --wheel --no-isolation
}

package() {
  cd "${_archive}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
