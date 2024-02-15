# Maintainer: Lex Black <autumn-wind at web dot de>
# Contributor: patlefort <northon_patrick3 at yahoo dot ca>
# Contributor: Daniel Larsson <znixen@live.se>

pkgbase=patool
pkgname='patool'
pkgver=2.2.0
pkgrel=1
pkgdesc="portable command line archive file manager"
arch=('any')
url="https://wummel.github.io/patool/"
license=('GPL')
depends=('python')
makedepends=(python-build python-installer python-wheel python-setuptools python-argcomplete)
optdepends=("lz4: extracting LZ4 archives"
    "p7zip: extracting ZIP and 7z files"
    "unarchiver: extracting various formats"
    "unrar: extracting RAR files"
    "zstd: extracting ZSTANDARD files")
#source=("https://pypi.python.org/packages/source/p/$pkgbase/$pkgbase-$pkgver.tar.gz")
source=("$pkgbase-$pkgver.tar.gz::https://github.com/wummel/patool/archive/upstream/${pkgver}.tar.gz")
sha256sums=('cbbb6e6803fb2828a2dbc40c6cd94a30c02c5a3a6b0ae2b04f316840a5593217')


build() {
  cd "${pkgbase}-upstream-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgbase}-upstream-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -dm755 "${pkgdir}/usr/share/bash-completion/completions"
  register-python-argcomplete patool > "${pkgdir}/usr/share/bash-completion/completions/patool"

  install -Dm644 'doc/patool.1' -t "${pkgdir}/usr/share/man/man1"
}
