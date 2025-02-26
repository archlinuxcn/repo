# Maintainer: Leo Mao <leomaoyw at gmail dot com>

pkgname="python-imageio"
_pkgname="imageio"
pkgver=2.37.0
pkgrel=2
pkgdesc="a Python library that provides an easy interface to read and write a wide range of image data"
arch=('any')
_github="imageio/imageio"
_pypiname="imageio"
url="https://github.com/imageio/imageio"
license=('BSD-2-Clause')
depends=('python-numpy' 'python-pillow')
optdepends=('python-imageio-ffmpeg' 'python-av' 'freeimage' 'python-astropy' 'python-simpleitk' 'python-tifffile')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/imageio/imageio/archive/v${pkgver}.tar.gz")
sha256sums=('e9d1dc913a480339a8adacd31917327964bab4706e7f97dac621278a3180328a')

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
  rm -f $pkgdir/usr/bin/{imageio_download_bin,imageio_remove_bin}
  rmdir --ignore-fail-on-non-empty $pkgdir/usr/bin
}

# vim:set ts=2 sw=2 et:<Paste>
