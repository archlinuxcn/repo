# Maintainer:
# Contributor: nblock <nblock [/at\] archlinux DOT us>

_pkgname="organize"
pkgname="$_pkgname"
pkgver=3.3.0
pkgrel=2
pkgdesc='A command line utility to automate file organization tasks'
url='https://github.com/tfeldmann/organize'
license=('MIT')
arch=('any')

depends=(
  'python'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-poetry'
  'python-wheel'
)

_pkgsrc="$_pkgname-$pkgver"
_pkgext="tar.gz"
source=("$_pkgsrc.$_pkgext"::"$url/archive/refs/tags/v$pkgver.$_pkgext")
sha256sums=('0b78928cc934cc60801ddf69f4910f8499e86070a1e256bb319c6863c71f73ea')

build() {
  cd "$_pkgsrc"
  python -m build --no-isolation --wheel --skip-dependency-check
}

package() {
  depends+=(
    'python-arrow'
    'python-jinja'
    'python-natsort'
    'python-pdfminer'
    'python-platformdirs'
    'python-pydantic'
    'python-rich'
    'python-send2trash'
    'python-yaml'

    ## AUR
    'python-docopt-ng'
    'python-docx2txt'
    'python-exifread'
    'python-simplematch'
  )

  cd "$_pkgsrc"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
