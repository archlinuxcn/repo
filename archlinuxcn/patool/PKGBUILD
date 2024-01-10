# Maintainer: Lex Black <autumn-wind at web dot de>
# Contributor: patlefort <northon_patrick3 at yahoo dot ca>
# Contributor: Daniel Larsson <znixen@live.se>

pkgbase=patool
pkgname='patool'
pkgver=2.0.0
pkgrel=2
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
sha256sums=('0e71f28da032878eb871201dd59e43b8008fb731c665ca481cd4b20135764603')


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
