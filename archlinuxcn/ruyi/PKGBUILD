# Maintainer: weilinfox <sakurakaze.fox at gmail.com>

pkgname=ruyi
pkgver=0.47.0
pkgrel=1
pkgdesc="RuyiSDK Package Manager"
arch=(any)
url="https://github.com/ruyisdk/ruyi"
license=(Apache-2.0)
depends=(
  'python>=3.11'
  'python-argcomplete'
  'python-arpy'
  'python-babel'
  'python-certifi'
  'python-fastjsonschema'
  'python-jinja'
  'python-packaging'
  'python-pygit2'
  'python-requests'
  'python-rich'
  'python-semver'
  'python-tomlkit'
  'python-typing_extensions'
  'python-yaml'
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
  "ruyi-completion"
)
sha512sums=('38b7b566ca2c85d2cc0baa36b5b26aee7d34de53fe6876e3904739a408fa4ea9a9afd97d1a950fa9c9d07086baf13fdad421a69b21db994331779d959a8d9314'
            '03b9a18c495c37203e5c56518e1ab94118b3bf99e83c99924f3eeca7be64ac3b03d744c105ac99ab703c40e570195a7ed39785e5beef5f619bdf868bd6add6f6'
            '8fb7bdd45b70ee740fcf279037a62463e13da589221bb52793a074e4063bf8b7d306fef0879980a1be893d76a0536c4ab6b124aec576b96372a8898f5307d609')
provides=(python-ruyi)

build() {
  cd "$pkgname-$pkgver"

  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd "$pkgname-$pkgver"

  python -m pytest -v --ignore tests/pluginhost/test_api.py
}

package() {
  cd "$pkgname-$pkgver"

  python -m installer -d "$pkgdir" dist/*.whl

  install -Dm644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}/"
  install -Dm644 LICENSE*.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  install -Dm644 ../config.toml -t "${pkgdir}/usr/share/${pkgname}/"
  install -Dm644 ../ruyi-completion "${pkgdir}/usr/share/bash-completion/completions/${pkgname}"
}
