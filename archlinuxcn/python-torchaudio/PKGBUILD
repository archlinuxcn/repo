# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>

pkgname=python-torchaudio
_pkgname=audio
pkgver=0.11.0
pkgrel=1
pkgdesc="Data manipulation and transformation for audio signal processing, powered by PyTorch"
arch=('any')
url="https://github.com/pytorch/audio"
license=('BSD')
depends=('python' 'python-pytorch')
optdepends=('python-kaldi-io')
makedepends=('git' 'python-setuptools' 'cmake' 'ninja')
conflicts=('python-torchaudio-git')
source=("git+$url#tag=v${pkgver}")
sha512sums=('SKIP')

prepare() {
  cd "$srcdir/${_pkgname}"
  # Use sourceforge url to fetch zlib
  # See https://github.com/pytorch/audio/pull/2297
  git cherry-pick -n e92a17c35fdff6b0622b0791b43e665c5d05c4b4
}

build() {
  cd "$srcdir/${_pkgname}"
  CUDA_HOME=/opt/cuda/ BUILD_SOX=1 python setup.py build
}

package() {
  cd "$srcdir/${_pkgname}"
  BUILD_SOX=1 python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

