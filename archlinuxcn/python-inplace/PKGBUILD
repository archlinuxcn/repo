# Maintainer: Claudia Pellegrino <aur ät cpellegrino.de>

pkgname=python-inplace
_gitpkgname=inplace
pkgver=1.0.1
pkgrel=1
pkgdesc='In-place file processing in Python'
arch=('any')
url='https://github.com/jwodder/inplace'
license=('MIT')
depends=(
  'python'
)
makedepends=(
  'python-build'
  'python-hatchling'
  'python-installer'
)

source=(
  "${_gitpkgname}-${pkgver}.tar.gz::https://github.com/jwodder/inplace/archive/v${pkgver}.tar.gz"
)

sha512sums=('71c92f5b9b53996338bb79b2a3184a9299849504d9b6a4fc99849b8e5360c65dc918965c95a6a3127a5e6c36a4d2bf541700c954904ceced271e42b28c714c02')

build() {
  cd "${_gitpkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_gitpkgname}-${pkgver}"

  echo >&2 'Packaging the wheel'
  python -I -m installer --destdir="${pkgdir}" dist/*.whl

  echo >&2 'Packaging the documentation'
  install -D -m 644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
    'README.rst'

  echo >&2 'Packaging the license'
  install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
    'LICENSE'
}
