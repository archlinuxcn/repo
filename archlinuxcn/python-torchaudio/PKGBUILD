# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>

pkgname=python-torchaudio
_pkgname=audio
pkgver=0.10.1
pkgrel=1
pkgdesc="Data manipulation and transformation for audio signal processing, powered by PyTorch"
arch=('any')
url="https://github.com/pytorch/audio"
license=('BSD')
depends=('python' 'sox' 'python-pytorch')
optdepends=('python-kaldi-io')
makedepends=('git' 'python-setuptools' 'cmake' 'ninja')
conflicts=('python-torchaudio-git')
source=("git+$url#tag=v${pkgver}")
sha512sums=('SKIP')

build() {
  cd "$srcdir/${_pkgname}"
  CUDA_HOME=/opt/cuda/ BUILD_SOX=1 python setup.py build
}

package() {
  cd "$srcdir/${_pkgname}"
  BUILD_SOX=1 python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

