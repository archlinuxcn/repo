# Maintainer: Leo Mao <leomaoyw at gmail dot com>

pkgname="python-imageio"
_pkgname="imageio"
pkgver=2.19.3
pkgrel=1
pkgdesc="a Python library that provides an easy interface to read and write a wide range of image data"
arch=('x86_64')
_github="imageio/imageio"
_pypiname="imageio"
url="https://github.com/imageio/imageio"
license=('BSD')
depends=('python-numpy' 'python-pillow')
optdepends=('avbin' 'python-imageio-ffmpeg' 'freeimage' 'python-astropy' 'python-simpleitk')
makedepends=('python' 'python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/imageio/imageio/archive/v${pkgver}.tar.gz")
sha256sums=('2ca858a8c178a252779b3c2fbcc19671d196385184e69fc763b151c155633fe3')

build() {
  msg "Building Python 3"
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1 --skip-build
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"

  # remove utilities for downloading binary dependencies
  rm $pkgdir/usr/bin/{imageio_download_bin,imageio_remove_bin}
  rmdir $pkgdir/usr/bin
}

# vim:set ts=2 sw=2 et:<Paste>
