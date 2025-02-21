# Maintainer: txtsd <aur.archlinux@ihavea.quest>
# Maintainer: Carl Smedstad <carsme@archlinux.org>
# Contributor: kbipinkumar <kbipinkumar@pm.me>
# Contributor: bpierre <benoit.pierre@gmail.com>
# Contributor: Anton Kudelin <kudelin at proton dot me>
# Contributor: Jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Aaron DeVore <aaron.devore@gmail.com>

pkgname=python-selenium
_pkgname="${pkgname#python-}"
pkgver=4.29.0
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
  pyo3.patch
  cargo.patch
)
sha256sums=('3a62f7ec33e669364a6c0562a701deb69745b569c50d55f1a912bf8eb33358ba'
            '41da6ac9e2e6c23a396e091b8dbac4ba8af738956ac23be43f573c7f1bed24ae'
            'e119e188b826e5fecdf4fdd2fea814318dc7fd9564347f055825befbd9d2542f')

_archive="${_pkgname}-${pkgver}"

prepare() {
  cd "${_archive}"

  # fixes for build failures mentioned in upstream repo (https://github.com/SeleniumHQ/selenium/pull/15128#issuecomment-2609736932)
  patch -Np1 -i ../pyo3.patch
  patch -Np1 -i ../cargo.patch

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
