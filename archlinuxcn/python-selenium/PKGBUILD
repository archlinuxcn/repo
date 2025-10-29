# Maintainer: txtsd <aur.archlinux@ihavea.quest>
# Maintainer: Carl Smedstad <carsme@archlinux.org>
# Contributor: kbipinkumar <kbipinkumar@pm.me>
# Contributor: bpierre <benoit.pierre@gmail.com>
# Contributor: Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

pkgname=python-selenium
_pkgname="${pkgname#python-}"
pkgver=4.38.0
pkgrel=1
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
source=(
  "https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz"
)
sha256sums=('c117af6727859d50f622d6d0785b945c5db3e28a45ec12ad85cee2e7cc84fc4c')

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

  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  cp selenium/webdriver/remote/*.js "${pkgdir}/${site_packages}/selenium/webdriver/remote"
  cp selenium/webdriver/common/*.js "${pkgdir}/${site_packages}/selenium/webdriver/common"
}
