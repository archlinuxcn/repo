# Maintainer: devome <evinedeng@hotmail.com>

pkgbase=sherpa-onnx
pkgname=("${pkgbase}" "python-${pkgbase}")
pkgver=2.0.3
pkgrel=1
pkgdesc="Speech-to-text, text-to-speech, speaker diarization, speech enhancement, source separation, and VAD using next-gen Kaldi with onnxruntime without Internet connection."
arch=("x86_64" "aarch64" "arm" "riscv64")
url="https://github.com/k2-fsa/${pkgbase}"
license=("Apache-2.0")
depends=("jack" "onnxruntime")
makedepends=("cmake" "ninja" "pybind11" "python-build" "python-installer" "python-setuptools" "python-wheel")
source=("${pkgbase}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "asio-asio-1-24-0.tar.gz::https://github.com/chriskohlhoff/asio/archive/refs/tags/asio-1-24-0.tar.gz"
        "eigen-5.0.1.tar.gz::https://gitlab.com/libeigen/eigen/-/archive/5.0.1/eigen-5.0.1.tar.gz"
        "hclust-cpp-2026-02-25.tar.gz::https://github.com/csukuangfj/hclust-cpp/archive/refs/tags/2026-02-25.tar.gz"
        "json-3.12.0.tar.gz::https://github.com/nlohmann/json/archive/refs/tags/v3.12.0.tar.gz"
        "kaldi-decoder-0.4.0.tar.gz::https://github.com/k2-fsa/kaldi-decoder/archive/refs/tags/v0.4.0.tar.gz"
        "kaldi-hmm-gmm-1.2.1.tar.gz::https://github.com/csukuangfj/kaldi-hmm-gmm/archive/refs/tags/v1.2.1.tar.gz"
        "kaldi-native-fbank-1.23.1.tar.gz::https://github.com/csukuangfj/kaldi-native-fbank/archive/refs/tags/v1.23.1.tar.gz"
        "kaldi_native_io-1.23.2.tar.gz::https://github.com/csukuangfj/kaldi_native_io/archive/refs/tags/v1.23.2.tar.gz"
        "kaldifst-1.8.0.tar.gz::https://github.com/k2-fsa/kaldifst/archive/refs/tags/v1.8.0.tar.gz"
        "kaldifst-1.9.0.tar.gz::https://github.com/k2-fsa/kaldifst/archive/refs/tags/v1.9.0.tar.gz"
        "kissfft-febd4caeed32e33ad8b2e0bb5ea77542c40f18ec.zip::https://github.com/mborgerding/kissfft/archive/febd4caeed32e33ad8b2e0bb5ea77542c40f18ec.zip"
        "openfst-1.8.5-2026-07-09.tar.gz::https://github.com/csukuangfj/openfst/archive/refs/tags/v1.8.5-2026-07-09.tar.gz"
        "simple-sentencepiece-0.7.tar.gz::https://github.com/pkufool/simple-sentencepiece/archive/refs/tags/v0.7.tar.gz"
        "utf8proc-2.12.0.tar.gz::https://github.com/JuliaStrings/utf8proc/archive/refs/tags/v2.12.0.tar.gz"
        "websocketpp-b9aeec6eaf3d5610503439b4fae3581d9aff08e8.zip::https://github.com/zaphoyd/websocketpp/archive/b9aeec6eaf3d5610503439b4fae3581d9aff08e8.zip")
sha256sums=('40e2ded061e16eda9750a49d1dee78ba308d5c37fc544108d8a660611d3b4c8d'
            'cbcaaba0f66722787b1a7c33afe1befb3a012b5af3ad7da7ff0f6b8c9b7a8a5b'
            'e9c326dc8c05cd1e044c71f30f1b2e34a6161a3b6ecf445d56b53ff1669e3dec'
            '8f14e024c709d73afb40ae69cb22de4b73dba67cbce40f2e518813da8139ab56'
            '4b92eb0c06d10683f7447ce9406cb97cd4b453be18d7279320f7b2f025c10187'
            '078f2ebb9927c19445096549f880b4ac6db14b7eeb263062f50697873901c955'
            '8344681ef464373bab54d548877ffa1cc82c16097e4f0975ce7b497c2e5b6e33'
            'c9722d55bf791d591baf6f79c8db8c66b7eeacf3bec59a4ac37864eacf2e8f37'
            '8c0eadd3aa2d9cafe62e82c2e3075a57bc41cac7e83f9553671413f07b070426'
            '3f247b7e5a2409071202f5e2bc6200060f66728c0a3443c03923ad2723e040b3'
            '225d8377d1d262e3aedab23558fead106b4cbc83462fb29f1c5e7d9e3b0c14dd'
            '497103e664168ebe39580b757adbe616f6cf85a16572af581ca7bc42d0ab13fd'
            '2ff712a32952fcb01d351121a6bc8ccf4fdc6b2aa06ce8df2b3095dedd518c0e'
            '1748a822060a35baa9f6609f84efc8eb54dc0e74b9ece3d82367b7119fdc75af'
            'f564011d38b2888d583d510b08e69ffa15aa117155db1b9b49ef1dfe1fa25111'
            '1385135ede8191a7fbef9ec8099e3c5a673d48df0c143958216cd1690567f583')
noextract=( $(echo "${source[@]:1}" | sed -E 's|:\S+||g') )

prepare() {
    cd "${pkgbase}-${pkgver}"
    for file in ${noextract[@]}; do
        ln -sf ../"${file}" "${file}"
    done
    sed -i "s|^    .$|    lib/pkgconfig|g" CMakeLists.txt
    echo 'find_package(pybind11 REQUIRED)' > cmake/pybind11.cmake
    echo "After upgrading onnxruntime, you need to rebuild ${pkgbase}."
}

build() {
    local base_args=(
        --compile-no-warning-as-error
        -Wno-dev
        -G Ninja
        -DCMAKE_BUILD_TYPE=None
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
