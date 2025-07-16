# Maintainer: txtsd <aur.archlinux@ihavea.quest>

pkgname=llama.cpp-cuda
_pkgname="${pkgname%-cuda}"
pkgver=b5904
pkgrel=1
pkgdesc="Port of Facebook's LLaMA model in C/C++ (with NVIDIA CUDA optimizations)"
arch=(x86_64 armv7h aarch64)
url='https://github.com/ggerganov/llama.cpp'
license=('MIT')
depends=(
  cuda
  curl
  gcc-libs
  glibc
  nvidia-utils
  python
  python-numpy
  python-sentencepiece
)
makedepends=(
  cmake
  git
)
optdepends=(python-pytorch)
provides=(${_pkgname})
conflicts=(${_pkgname} libggml ggml)
options=(lto !debug)
source=(
  "git+${url}#tag=${pkgver}"
  llama.cpp.conf
  llama.cpp.service
)
sha256sums=('67a6565fbbc960de66687f3d0a3695283f556a8c008ff06cd28e872d1708db60'
            '53fa70cfe40cb8a3ca432590e4f76561df0f129a31b121c9b4b34af0da7c4d87'
            '0377d08a07bda056785981d3352ccd2dbc0387c4836f91fb73e6b790d836620d')

build() {
  local _cmake_options=(
    -B build
    -S "${_pkgname}"
    -DCMAKE_BUILD_TYPE=Release
    -DCMAKE_INSTALL_PREFIX='/usr'
    -DBUILD_SHARED_LIBS=ON
    -DLLAMA_CURL=ON
    -DLLAMA_BUILD_TESTS=OFF
    -DLLAMA_USE_SYSTEM_GGML=OFF
    -DGGML_ALL_WARNINGS=OFF
    -DGGML_ALL_WARNINGS_3RD_PARTY=OFF
    -DGGML_BUILD_EXAMPLES=OFF
    -DGGML_BUILD_TESTS=OFF
    -DGGML_LTO=ON
    -DGGML_RPC=ON
    -DGGML_CUDA=ON
    -DGGML_NATIVE=ON
    -Wno-dev
  )
  cmake "${_cmake_options[@]}"
  cmake --build build
}

package() {
  DESTDIR="${pkgdir}" cmake --install build

  install -Dm644 "${_pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  install -Dm644 "llama.cpp.conf" "${pkgdir}/etc/conf.d/llama.cpp"
  install -Dm644 "llama.cpp.service" "${pkgdir}/usr/lib/systemd/system/llama.cpp.service"
}
