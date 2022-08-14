# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>

pkgname=python-torchaudio
_pkgname=audio
pkgver=0.12.1
_sox_ver=14.4.2
pkgrel=1
pkgdesc="Data manipulation and transformation for audio signal processing, powered by PyTorch"
arch=('x86_64' 'i686')
url="https://github.com/pytorch/audio"
license=('BSD')
depends=('python' 'python-pytorch' 'bzip2' 'xz' 'opencore-amr' 'lame' 'libogg' 'flac' 'libvorbis' 'opus' 'opusfile' 'zlib')
optdepends=('python-kaldi-io')
makedepends=('git' 'python-setuptools' 'cmake' 'ninja' 'gcc11' 'boost')
conflicts=('python-torchaudio-git')
source=("git+$url#tag=v${pkgver}"
        "git+https://github.com/kaldi-asr/kaldi.git"
        "git+https://github.com/kpu/kenlm.git"
        # Files downloaded by ExternalProject_Add
        "https://downloads.sourceforge.net/project/sox/sox/$_sox_ver/sox-$_sox_ver.tar.bz2"
        "use-system-libs.diff")
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            '81a6956d4330e75b5827316e44ae381e6f1e8928003c6aa45896da9041ea149c'
            '02e7c503a8b876246801d8d9e223992928ee7df8c2009239ffce96583faf52a0')

prepare() {
  cd "$srcdir/${_pkgname}"

  mkdir -p third_party/archives
  ln -s "$srcdir"/sox-$_sox_ver.tar.bz2 third_party/archives/

  patch -Np1 -i ../use-system-libs.diff

  # loop stolen from python-onnxruntime :)
  git submodule init
  for mod in kaldi kenlm; do
    git config submodule.third_party/$mod/submodule.url "$srcdir"/$mod
    git submodule update third_party/$mod/submodule
  done
}

build() {
  cd "$srcdir/${_pkgname}"

  # Allow this to build with CUDA, which is not compatible with GCC 12 yet
  export CC=/usr/bin/gcc-11
  export CXX=/usr/bin/g++-11
  export CUDACXX=/opt/cuda/bin/nvcc
  export CUDAHOSTCXX=$CXX
  # Follow architectures used by pytorch
  # https://github.com/archlinux/svntogit-community/blob/packages/python-pytorch/trunk/PKGBUILD
  export TORCH_CUDA_ARCH_LIST="5.2;6.0;6.2;7.0;7.2;7.5;8.0;8.6;8.6+PTX"

  CUDA_HOME=/opt/cuda/ BUILD_SOX=1 python setup.py build
}

package() {
  cd "$srcdir/${_pkgname}"
  BUILD_SOX=1 python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

