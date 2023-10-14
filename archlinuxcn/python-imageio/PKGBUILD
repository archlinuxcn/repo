# Maintainer: Leo Mao <leomaoyw at gmail dot com>

pkgname="python-imageio"
_pkgname="imageio"
pkgver=2.31.5
pkgrel=4
pkgdesc="a Python library that provides an easy interface to read and write a wide range of image data"
arch=('any')
_github="imageio/imageio"
_pypiname="imageio"
url="https://github.com/imageio/imageio"
license=('BSD')
depends=('python-numpy' 'python-pillow')
optdepends=('avbin' 'python-imageio-ffmpeg' 'freeimage' 'python-astropy' 'python-simpleitk')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/imageio/imageio/archive/v${pkgver}.tar.gz")
sha256sums=('a04e1d87e01734c8981c2989b1d2b5bd729821705b09066cfc6c31d5ffe0ffd7')

build() {
  msg "Building Python 3"
  cd "$srcdir/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" --compile-bytecode=1 dist/*.whl
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"

  # remove utilities for downloading binary dependencies
  rm $pkgdir/usr/bin/{imageio_download_bin,imageio_remove_bin}
  rmdir $pkgdir/usr/bin
}

# vim:set ts=2 sw=2 et:<Paste>
