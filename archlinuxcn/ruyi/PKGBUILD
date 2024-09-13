# Maintainer: weilinfox <sakurakaze.fox at gmail.com>

pkgname=ruyi
pkgver=0.18.0
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
  'python-xingque'
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
  "ruyi"
)
sha512sums=(
  '0d887e21fe5d46241e7e71e012d4dc9ce09cbd675c09db31df903a70a85484547a35081003ccd3f89764780dbfff16d6569259492c58580d3cb88342cab7abf4'
  '49d2d53b91e343d029d20b4830098dbcfb04161d323f6fa9c3e1fdc0c02df1335871d0f44627916e076a2062fcb97d52ea87368e6cabc0d7167591022ce293ea'
)
provides=(python-ruyi)

build() {
  cd "$pkgname-$pkgver"

  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd "$pkgname-$pkgver"

  python -m pytest -v
}

package() {
  cd "$pkgname-$pkgver"

  python -m installer -d "$pkgdir" dist/*.whl

  install -Dm644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}/"
  install -Dm644 LICENSE*.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  install -Dm755 ../ruyi "${pkgdir}/usr/bin/ruyi"
}
