# Maintainer: weilinfox <sakurakaze.fox at gmail.com>

pkgname=ruyi
pkgver=0.36.0
pkgrel=1
pkgdesc="RuyiSDK Package Manager"
arch=(any)
url="https://github.com/ruyisdk/ruyi"
license=(Apache-2.0)
depends=(
  'python>=3.11'
  'python-arpy'
  'python-certifi'
  'python-jinja'
  'python-packaging'
  'python-pygit2'
  'python-requests'
  'python-rich'
  'python-semver'
  'python-tomlkit'
  'python-typing_extensions'
  'python-yaml'
  'sh'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-poetry-core'
)
checkdepends=('python-pytest')
optdepends=(
  'android-tools: fastboot support'
  'bash: ruyi use bash as default shell'
  'bzip2: bzip file support'
  'curl: curl downloading support'
  'coreutils: dd support'
  'gzip: gunzip file support'
  'sudo: privileged operations support'
  'tar: untar tarball support'
  'unzip: zip file support'
  'wget: wget downloading support'
  'xz: xz file support'
  'zstd: zstd file support'
)
source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/ruyisdk/ruyi/archive/refs/tags/${pkgver}.tar.gz"
  "config.toml"
)
sha512sums=('239c1423adb3aa0c643e17e7a1bba98c6de8048d19c1e9eb557413d3c6a1786987c1a37fbf056bf6c19aeae3c8ca71c4d0a29e56536886e3e593b1083719385e'
            '03b9a18c495c37203e5c56518e1ab94118b3bf99e83c99924f3eeca7be64ac3b03d744c105ac99ab703c40e570195a7ed39785e5beef5f619bdf868bd6add6f6')
provides=(python-ruyi)

build() {
  cd "$pkgname-$pkgver"

  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd "$pkgname-$pkgver"

  # pluginhost/test_api.py failed during collection
  python -m pytest -v --ignore tests/pluginhost/test_api.py \
                      --ignore tests/config/test_editor.py \
                      --ignore tests/config/test_schema.py
}

package() {
  cd "$pkgname-$pkgver"

  python -m installer -d "$pkgdir" dist/*.whl

  install -Dm644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}/"
  install -Dm644 LICENSE*.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  install -Dm644 ../config.toml -t "${pkgdir}/usr/share/${pkgname}/"
}
