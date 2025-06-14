# Maintainer: weilinfox <sakurakaze.fox at gmail.com>

pkgname=ruyi
pkgver=0.35.0
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
sha512sums=('f7b790bedf19b3b91ba05438492cab84675e4ee2fd325c8ee81f39eee5d8e939f17206043ff4e070ec4175e835bdf6abb141e0054b0042a32cfe0f52cddb3239'
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
