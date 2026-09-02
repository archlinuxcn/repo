# Maintainer: devome <evinedeng@hotmail.com>

pkgbase=sherpa-onnx
pkgname=("${pkgbase}" "python-${pkgbase}")
pkgver=1.13.7
pkgrel=1
pkgdesc="Speech-to-text, text-to-speech, speaker diarization, speech enhancement, source separation, and VAD using next-gen Kaldi with onnxruntime without Internet connection."
arch=("x86_64" "aarch64" "arm" "riscv64")
url="https://github.com/k2-fsa/${pkgbase}"
license=("Apache-2.0")
depends=("jack" "onnxruntime")
makedepends=("cargs" "cmake" "ninja" "pybind11" "python-build" "python-installer" "python-setuptools" "python-wheel")
source=("${pkgbase}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "asio-asio-1-24-0.tar.gz::https://github.com/chriskohlhoff/asio/archive/refs/tags/asio-1-24-0.tar.gz"
        "eigen-5.0.1.tar.gz::https://gitlab.com/libeigen/eigen/-/archive/5.0.1/eigen-5.0.1.tar.gz"
        "espeak-ng-ed530aa113046142eb5115cf2fc9157854d0ffe1.zip::https://github.com/csukuangfj/espeak-ng/archive/ed530aa113046142eb5115cf2fc9157854d0ffe1.zip"
        "hclust-cpp-2026-02-25.tar.gz::https://github.com/csukuangfj/hclust-cpp/archive/refs/tags/2026-02-25.tar.gz"
        "json-3.12.0.tar.gz::https://github.com/nlohmann/json/archive/refs/tags/v3.12.0.tar.gz"
        "kaldi-decoder-0.3.0.tar.gz::https://github.com/k2-fsa/kaldi-decoder/archive/refs/tags/v0.3.0.tar.gz"
        "kaldi-native-fbank-1.22.3.tar.gz::https://github.com/csukuangfj/kaldi-native-fbank/archive/refs/tags/v1.22.3.tar.gz"
        "kaldifst-1.8.0.tar.gz::https://github.com/k2-fsa/kaldifst/archive/refs/tags/v1.8.0.tar.gz"
        "kissfft-febd4caeed32e33ad8b2e0bb5ea77542c40f18ec.zip::https://github.com/mborgerding/kissfft/archive/febd4caeed32e33ad8b2e0bb5ea77542c40f18ec.zip"
        "openfst-1.8.5-2026-07-09.tar.gz::https://github.com/csukuangfj/openfst/archive/refs/tags/v1.8.5-2026-07-09.tar.gz"
        "pa_stable_v190700_20210406.tgz::http://files.portaudio.com/archives/pa_stable_v190700_20210406.tgz"
        "piper-phonemize-f3ff95afc03640bc1399e113e83361192a2fafb4.zip::https://github.com/csukuangfj/piper-phonemize/archive/f3ff95afc03640bc1399e113e83361192a2fafb4.zip"
        "simple-sentencepiece-0.7.tar.gz::https://github.com/pkufool/simple-sentencepiece/archive/refs/tags/v0.7.tar.gz"
        "websocketpp-b9aeec6eaf3d5610503439b4fae3581d9aff08e8.zip::https://github.com/zaphoyd/websocketpp/archive/b9aeec6eaf3d5610503439b4fae3581d9aff08e8.zip")
sha256sums=('ee0c20cafb34cc1f86afb2845babd941c26e46de4a9925cbe86fd55ff3557818'
            'cbcaaba0f66722787b1a7c33afe1befb3a012b5af3ad7da7ff0f6b8c9b7a8a5b'
            'e9c326dc8c05cd1e044c71f30f1b2e34a6161a3b6ecf445d56b53ff1669e3dec'
            'e4e262cbe34f7fe21f91f1ba3397f2728e1f30eafbae7853f2b753a9ed13f0dd'
            '8f14e024c709d73afb40ae69cb22de4b73dba67cbce40f2e518813da8139ab56'
            '4b92eb0c06d10683f7447ce9406cb97cd4b453be18d7279320f7b2f025c10187'
            'b9f34cfb4fd3b1344100eead79ef4d37aa15962274b9e3056de345021f76a1b0'
            '9176cc66fc7ce1edf85cf355b06e320c57db6297df74277f575183468893cf61'
            '3f247b7e5a2409071202f5e2bc6200060f66728c0a3443c03923ad2723e040b3'
            '497103e664168ebe39580b757adbe616f6cf85a16572af581ca7bc42d0ab13fd'
            '2ff712a32952fcb01d351121a6bc8ccf4fdc6b2aa06ce8df2b3095dedd518c0e'
            '47efbf42c77c19a05d22e627d42873e991ec0c1357219c0d74ce6a2948cb2def'
            'd9cca4e2bdc7d6dd8dffb96a4668283dbd3f77a9c194a3e530c1e8eba9406a5d'
            '1748a822060a35baa9f6609f84efc8eb54dc0e74b9ece3d82367b7119fdc75af'
            '1385135ede8191a7fbef9ec8099e3c5a673d48df0c143958216cd1690567f583')
noextract=( $(echo "${source[@]:1}" | sed -E 's|:\S+||g') )

prepare() {
    cd "${pkgbase}-${pkgver}"
    for file in ${noextract[@]}; do
        ln -sf ../"${file}" "${file}"
    done
    sed -i "s|include(cargs)|find_package(Cargs CONFIG REQUIRED)|" c-api-examples/CMakeLists.txt
    sed -i "s|^    .$|    lib/pkgconfig|g" CMakeLists.txt
    echo 'find_package(pybind11 REQUIRED)' > cmake/pybind11.cmake
    echo "After upgrading onnxruntime, you need to rebuild ${pkgbase}."
}

build() {
    local base_args=(
        --compile-no-warning-as-error
        -Wno-dev
        -G Ninja
        -DCMAKE_BUILD_TYPE=Release
        -DSHERPA_ONNX_USE_PRE_INSTALLED_ONNXRUNTIME_IF_AVAILABLE=ON
    )
    export CFLAGS+=" -Wno-error=format-security"
    export CXXFLAGS+=" -Wno-error=format-security"

    cd "${pkgbase}-${pkgver}"
    cmake "${base_args[@]}" \
        -Bbuild_bin \
        -DBUILD_SHARED_LIBS=ON \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DSHERPA_ONNX_ENABLE_BINARY=ON \
        -DSHERPA_ONNX_ENABLE_PYTHON=OFF
    cmake --build build_bin
    
    SHERPA_ONNX_CMAKE_ARGS="${base_args[@]} -DSHERPA_ONNX_ENABLE_BINARY=OFF" python -m build --wheel --no-isolation
}

package_sherpa-onnx() {
    cd "${pkgbase}-${pkgver}"
    DESTDIR="${pkgdir}" cmake --install build_bin
    install -Dm644 {README,CHANGELOG}.md -t "${pkgdir}/usr/share/doc/${pkgname}"
}

package_python-sherpa-onnx() {
    pkgdesc+=" (Python bindings)"
    depends=("alsa-lib" "onnxruntime" "pypinyin" "python-click" "python-onnxruntime" "python-sentencepiece")

    cd "${pkgbase}-${pkgver}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -Dm644 {README,CHANGELOG}.md -t "${pkgdir}/usr/share/doc/${pkgname}"
}
