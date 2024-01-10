_name=7-zip
pkgname=${_name}-full
pkgver=23.01
pkgrel=2
pkgdesc="File archiver with a high compression ratio (full package to replace p7zip)"
url="https://7-zip.org/"
license=('LGPL')
arch=('x86_64' 'i686' 'aarch64' 'armv7h')
provides=("${_name}" 'p7zip')
conflicts=("${provides[@]}")
makedepends=('uasm')

source=(
    "${url}a/7z${pkgver//./}-src.tar.xz"
    'prepare.patch'
)

sha256sums=(
    '356071007360e5a1824d9904993e8b2480b51b570e8c9faf7c0f58ebe4bf9f74'
    '4db1d0e9bd0f156be35f264182c56724e36648510283e9e9187f334d7a1e6c06'
)

prepare() {
    chmod -R a=rw,a+X .
    patch -p0 --binary -i "${source[1]}"
}

build() {
    local targets=("Alone" "Alone2" "Alone7z" "Format7zF")
    local -A platforms=(['x86_64']='x64' ['i686']='x86' ['aarch64']='arm64' ['armv7h']='arm')

    (
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

        for target in "${targets[@]}"; do
            cd "${srcdir}/CPP/7zip/Bundles/${target}"
            mkdir -p '_o'
            make -f 'makefile.gcc'
        done
    )
}

package() {
    local bin="${pkgdir}/usr/bin"

    install -Dm755 -t "${bin}" \
        'CPP/7zip/Bundles/'{'Alone/_o/7za','Alone2/_o/7zz','Alone7z/_o/7zr'}

    install -Dm644 -t "${pkgdir}/usr/lib" \
        'CPP/7zip/Bundles/Format7zF/_o/7z.so'

    ln -sT "7zz" "${bin}/7z"

    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
        "DOC/"{"copying.txt","License.txt","unRarLicense.txt"}

    install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
        "DOC/"{"7zC.txt","7zFormat.txt","lzma.txt","Methods.txt","readme.txt","src-history.txt"}
}
