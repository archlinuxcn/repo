# Maintainer: Horror Proton <https://github.com/horror-proton>
# Maintainer: Cryolitia <cryolitia at gmail dot com>

# shellcheck disable=SC2034 disable=SC2164

: ${WITH_CUDA:=1}

_pkgname=maa-assistant-arknights
pkgname=(maa-assistant-arknights)
_pkgver=5.26.2
pkgver=${_pkgver//-/}
pkgrel=1
pkgdesc="An Arknights assistant"
arch=(x86_64)
url="https://github.com/MaaAssistantArknights/MaaAssistantArknights"
license=('AGPL-3.0-only')
depends=(opencv onnxruntime)
makedepends=(boost eigen git cmake)
_fastdeploy_ref=e962983da6daba7d0c12f6bf5f8ff7173be70982
source=("${_pkgname}-${_pkgver}.tar.gz::$url/archive/refs/tags/v$_pkgver.tar.gz"
"FastDeploy-${_fastdeploy_ref}.tar.gz::https://github.com/MaaXYZ/FastDeploy/archive/$_fastdeploy_ref.tar.gz")
install="${_pkgname}.install"
md5sums=('4d9fb677cb06e898b520dd883097e24c'
         '4555f8dce0cec02022356d50c8f2275c')

if ((WITH_CUDA)); then
    pkgname+=(maa-assistant-arknights-cuda)
    depends+=(cuda)
fi

prepare() {
    sed -e 's/35 50 52 60 61 70//g;' -i "${srcdir}/FastDeploy-${_fastdeploy_ref}/cmake/cuda.cmake"

    cd "${srcdir}/MaaAssistantArknights-${_pkgver}"

    sed -e '/^find_package(fast/s/^/# /;' \
        -e '/maadeps/s/^/# /;' \
        -e 's/imgproc/imgproc calib3d videoio xfeatures2d/' \
        -i CMakeLists.txt

    sed -e '/copy_and_add_rpath_library(/s/^/# /;' \
        -e '/add_compile_options/s/^/# /;' \
        -i cmake/config.cmake
    sed -e '/maadeps/s/^/# /;' -i cmake/utils.cmake -i src/MaaCore/CMakeLists.txt

    cat <<_EOF >>CMakeLists.txt
add_subdirectory(\${fastdeploy_SOURCE_DIR} \${fastdeploy_BINARY_DIR} EXCLUDE_FROM_ALL SYSTEM)
target_include_directories(MaaCore SYSTEM PRIVATE \${fastdeploy_SOURCE_DIR})
install(TARGETS fastdeploy_ppocr)
_EOF
}

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
