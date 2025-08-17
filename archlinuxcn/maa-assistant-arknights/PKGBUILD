# Maintainer: Horror Proton <https://github.com/horror-proton>
# Maintainer: Cryolitia <cryolitia at gmail dot com>

# shellcheck disable=SC2034 disable=SC2164

: ${WITH_CUDA:=1}

_pkgname=maa-assistant-arknights
pkgname=(maa-assistant-arknights)
_pkgver=5.23.1
pkgver=${_pkgver//-/}
pkgrel=1
pkgdesc="An Arknights assistant"
arch=(x86_64)
url="https://github.com/MaaAssistantArknights/MaaAssistantArknights"
license=('AGPL-3.0-only')
depends=(opencv onnxruntime cpr)
makedepends=(asio eigen git cmake)
_fastdeploy_ref=2896b6d3641c18218209c496ea149a773373fa8b
source=("${_pkgname}-${_pkgver}.tar.gz::$url/archive/refs/tags/v$_pkgver.tar.gz"
"FastDeploy-${_fastdeploy_ref}.tar.gz::https://github.com/MaaAssistantArknights/FastDeploy/archive/$_fastdeploy_ref.tar.gz")
install="${_pkgname}.install"
md5sums=('199300bbbb1faba7fcb911b3bd6139c3'
         '795116aab12a8c2eda2a9c7498595ae7')

if ((WITH_CUDA)); then
    pkgname+=(maa-assistant-arknights-cuda)
    depends+=(cuda)
fi

build() {
    local _cmake_flags=(
        -DCMAKE_BUILD_TYPE=None
        -DUSE_MAADEPS=OFF
        -DINSTALL_RESOURCE=ON
        -DINSTALL_PYTHON=ON
        -DINSTALL_FLATTEN=OFF
        -DBUILD_SHARED_LIBS=ON
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON
        -DCMAKE_INSTALL_PREFIX="$pkgdir"/usr
        -DMAA_VERSION="v$_pkgver"
        -Dfastdeploy_SOURCE_DIR="$srcdir"/FastDeploy-"$_fastdeploy_ref"
        -Dfastdeploy_BINARY_DIR="$srcdir"/build-FastDeploy
    )
    
    CXXFLAGS+=" -fmacro-prefix-map=$srcdir=${DBGSRCDIR:-/usr/src/debug}/${pkgbase:?}"
    
    cmake -B build -S "MaaAssistantArknights-${_pkgver}" "${_cmake_flags[@]}"
    cmake --build build
    
    if ((WITH_CUDA)); then
        local _cmake_flags+=(
            -DWITH_CUDA=ON
            -DCUDA_DIRECTORY=/opt/cuda
            -DCUDA_ARCH_NAME=Auto
        )
        
        cmake -B build-cuda -S "MaaAssistantArknights-${_pkgver}" "${_cmake_flags[@]}"
        cmake --build build-cuda
    fi
}

package_maa-assistant-arknights() {
    cmake --install "$srcdir"/build --prefix "$pkgdir"/usr
    
    cd "$pkgdir"/usr/
    mkdir -p share/"$_pkgname"
    mv Python resource share/"$_pkgname"
    ln -sr lib/* share/"$_pkgname"
}

package_maa-assistant-arknights-cuda() {
    cmake --install "$srcdir"/build-cuda --prefix "$pkgdir"/usr
    
    cd "$pkgdir"/usr/
    mkdir -p share/"$_pkgname"
    mv Python resource share/"$_pkgname"
    ln -sr lib/* share/"$_pkgname"
}
