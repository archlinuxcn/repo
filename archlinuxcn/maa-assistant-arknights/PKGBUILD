# Maintainer: Horror Proton <https://github.com/horror-proton>
# Maintainer: Cryolitia <cryolitia at gmail dot com>

# shellcheck disable=SC2034 disable=SC2164

: ${WITH_CUDA:=1}

_pkgname=maa-assistant-arknights
pkgname=(maa-assistant-arknights)
_pkgver=5.27.3
pkgver=${_pkgver//-/}
pkgrel=1
pkgdesc="An Arknights assistant"
arch=(x86_64)
url="https://github.com/MaaAssistantArknights/MaaAssistantArknights"
license=('AGPL-3.0-only')
depends=(opencv onnxruntime)
makedepends=(boost eigen git cmake)
_fastdeploy_ref=e962983da6daba7d0c12f6bf5f8ff7173be70982
source=("git+$url.git#tag=v${_pkgver}"
"git+https://github.com/MaaXYZ/MaaUtils.git"
"FastDeploy-${_fastdeploy_ref}.tar.gz::https://github.com/MaaXYZ/FastDeploy/archive/$_fastdeploy_ref.tar.gz")
install="${_pkgname}.install"
md5sums=('09a517212490b38fd1a6a6002764a764'
         'SKIP'
         '4555f8dce0cec02022356d50c8f2275c')

if ((WITH_CUDA)); then
    pkgname+=(maa-assistant-arknights-cuda)
    depends+=(cuda)
fi

prepare() {
    sed -e 's/35 50 52 60 61 70//g;' -i "${srcdir}/FastDeploy-${_fastdeploy_ref}/cmake/cuda.cmake"

    cd "${srcdir}/MaaAssistantArknights"

    git submodule init
    git config submodule.src/MaaUtils.url "${srcdir}/MaaUtils"
    git -c protocol.file.allow=always submodule update src/MaaUtils

    sed -e '/^find_package(fast/s/^/# /;' \
        -e '/maadeps/s/^/# /;' \
        -e 's/imgproc/imgproc calib3d videoio xfeatures2d/' \
        -e 's/ system)/ process)/'\
        -i CMakeLists.txt -i src/MaaUtils/MaaUtils.cmake

    sed -e '/copy_and_add_rpath_library(/s/^/# /;' \
        -e '/add_compile_options/s/^/# /;' \
        -i {,src/MaaUtils/}cmake/config.cmake
    sed -e '/maadeps/s/^/# /;' \
        -e 's/Boost::system/Boost::process/g;' \
        -i {,src/MaaUtils/}cmake/utils.cmake -i src/MaaCore/CMakeLists.txt

    sed -e '/MAADEPS_DIR/s/^/# /;' \
        -e '/system/s/^/# /;' \
        -i src/MaaUtils/MaaUtils.cmake
    sed -e 's/Boost::system//g' \
        -i src/MaaUtils/source/CMakeLists.txt

    cat <<_EOF >>CMakeLists.txt
add_subdirectory(\${fastdeploy_SOURCE_DIR} \${fastdeploy_BINARY_DIR} EXCLUDE_FROM_ALL SYSTEM)
target_include_directories(MaaCore SYSTEM PRIVATE \${fastdeploy_SOURCE_DIR})
install(TARGETS fastdeploy_ppocr MaaUtils)
_EOF

    # fix for boost 1.89
    cat <<_EOF >>src/MaaUtils/include/MaaUtils/IOStream/BoostIO.hpp
// #define BOOST_PROCESS_VERSION 1
#include <boost/process/v1/child.hpp>
#include <boost/process/v1/io.hpp>
#include <boost/process/v1/pipe.hpp>
#include <boost/process/v1/search_path.hpp>
_EOF
    sed -e 's/address::from_string/make_address/g' \
        -e 's/\*ios\.rdbuf/ios\.socket/' \
        -i src/MaaUtils/source/IOStream/SockIOStream.cpp

    sed -e '4i #include <unordered_map>' \
        -i src/MaaCore/Config/Roguelike/RoguelikeMapConfig.h
    sed -e '24i #include <cstring>' \
        -i src/MaaCore/./Utils/ExceptionStacktrace.hpp
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
    CXXFLAGS+=" -DBOOST_PROCESS_VERSION=1"
    
    CXXFLAGS+=" -fmacro-prefix-map=$srcdir=${DBGSRCDIR:-/usr/src/debug}/${pkgbase:?}"
    
    cmake -B build -S "MaaAssistantArknights" "${_cmake_flags[@]}"
    cmake --build build
    
    if ((WITH_CUDA)); then
        local _cmake_flags+=(
            -DWITH_CUDA=ON
            -DCUDA_DIRECTORY=/opt/cuda
            -DCUDA_ARCH_NAME=Auto
        )
        
        cmake -B build-cuda -S "MaaAssistantArknights" "${_cmake_flags[@]}"
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
