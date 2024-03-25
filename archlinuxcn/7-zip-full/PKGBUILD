_name=7-zip
pkgname=${_name}-full
pkgver=23.01
pkgrel=4
pkgdesc="File archiver with a high compression ratio (full package to replace p7zip)"
url="https://7-zip.org/"
license=('LGPL')
arch=('x86_64' 'i686' 'aarch64' 'armv7h')
provides=("${_name}" 'p7zip')
conflicts=("${provides[@]}")
makedepends=('uasm')

_sver="${pkgver//./}"
source=(
    "${url}a/7z${_sver}-src.tar.xz"
    "${url}a/7z${_sver}-linux-x64.tar.xz" # To get the manual
    '01-make.patch'
    '02-lib-load-path.patch'
    '03-version-string.patch' # Fix for Ark https://invent.kde.org/utilities/ark/-/merge_requests/232
)

sha256sums=(
    '356071007360e5a1824d9904993e8b2480b51b570e8c9faf7c0f58ebe4bf9f74'
    '23babcab045b78016e443f862363e4ab63c77d75bc715c0b3463f6134cbcf318'
    '3c6b0ee8ecae06a4f0ff91205989e93e22d03a33e5b7cc6982396c32041fc0a8'
    '5b49bd8c22f2fcc4e6011adc36c2d7a3fb195ba86596b366974f7b6311d0df00'
    '272d0d5ad64738e38f21b4596114824160318322c79a6eb1d69867c57c8f487e'
)

_msrc="${source[1]##*/}"
noextract=("${_msrc}")

prepare() {
    chmod -R a=rw,a+X .

    for p in *.patch; do
        patch -p1 --binary -Z -i "${p}"
    done
}

_make() {
    echo "Building '${1}'..."
    cd "${1}"
    mkdir -p '_o'
    make -sf 'makefile.gcc'
}

_build() {
    local -A platforms=(['x86_64']='x64' ['i686']='x86' ['aarch64']='arm64' ['armv7h']='arm')

    set -a
    PLATFORM="${platforms["${CARCH}"]}"
    IS_X64=$([ "${CARCH}" = 'x86_64' ] && echo '1' || echo '')
    IS_X86=$([ "${CARCH}" = 'i686' ] && echo '1' || echo '')
    IS_ARM64=$([ "${CARCH}" = 'aarch64' ] && echo '1' || echo '')
    MY_ARCH=
    USE_ASM=1
    CFLAGS_WARN='-Wno-error'
    CFLAGS_ADD="${CFLAGS}"
    LDFLAGS_ADD="${LDFLAGS}"
    CXXFLAGS_ADD="${CXXFLAGS}"
    set +a

    local targets=('CPP/7zip/'{'UI/Console','Bundles/'{'Alone','Alone7z','Format7zF'}})
    for target in "${targets[@]}"; do
        (_make "${target}")
    done
}

build() {
    (_build)
}

package() {
    install -Dm755 -t "${pkgdir}/usr/bin" \
        'CPP/7zip/'{'UI/Console/_o/7z','Bundles/'{'Alone/_o/7za','Alone7z/_o/7zr'}}

    install -Dm644 -t "${pkgdir}/usr/lib" \
        'CPP/7zip/Bundles/Format7zF/_o/7z.so'

    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
        'DOC/'{'copying.txt','License.txt','unRarLicense.txt'}

    local doc="${pkgdir}/usr/share/doc/${pkgname}"
    install -Dm644 -t "${doc}" \
        'DOC/'{'7zC.txt','7zFormat.txt','lzma.txt','Methods.txt','readme.txt','src-history.txt'}

    bsdtar -C "${doc}" -xf "${_msrc}" 'MANUAL'
}
