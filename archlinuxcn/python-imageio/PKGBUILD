# Maintainer: Leo Mao <leomaoyw at gmail dot com>

pkgname="python-imageio"
_pkgname="imageio"
pkgver=2.32.0
pkgrel=1
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
sha256sums=('87b6eeac48bfa4042cd78a8efd0bf67cc32d338b3fe484045086f7389bee7b2b')

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
