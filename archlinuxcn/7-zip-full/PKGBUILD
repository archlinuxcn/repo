# To build without ASM (uasm), set NO_ASM variable. For example:
# NO_ASM=1 makepkg -si

_name=7-zip
pkgname=${_name}-full
pkgver=22.01
pkgrel=6
pkgdesc="File archiver with a high compression ratio (full package to replace p7zip)"
url="https://7-zip.org/"
license=('LGPL')
arch=('x86_64' 'i686' 'aarch64')
provides=("${_name}" 'p7zip')
conflicts=("${provides[@]}")
makedepends=()

if [ ! "${NO_ASM}" ]; then
    makedepends+=('uasm')
fi

source=(
    "${url}a/7z${pkgver//./}-src.tar.xz"
    'prepare.patch'
)

sha256sums=(
    '393098730c70042392af808917e765945dc2437dee7aae3cfcc4966eb920fbc5'
    'e79922f6c7d686a941011dc27472ce66c872f2f706251f060225d1bd2da40c6a'
)

prepare() {
    chmod -R a=rw,a+X .
    patch -p0 --binary -i "${source[1]}"
}

build() {
    local targets=("Alone" "Alone2" "Alone7z" "Format7zF")
    local -A platforms=(['x86_64']='x64' ['i686']='x86' ['aarch64']='arm64')
    mkdir -p "build"

    (
        set -a
        PLATFORM="${platforms["${CARCH}"]}"
        O="${srcdir}/build"
        IS_X64=$([ "${CARCH}" = 'x86_64' ] && echo '1' || echo '')
        IS_X86=$([ "${CARCH}" = 'i686' ] && echo '1' || echo '')
        IS_ARM64=$([ "${CARCH}" = 'aarch64' ] && echo '1' || echo '')
        MY_ARCH=
        USE_ASM=$([ ! "${NO_ASM}" ] && echo '1' || echo '')
        CFLAGS_WARN='-Wno-error'
        CFLAGS_ADD="${CFLAGS}"
        LDFLAGS_ADD="${LDFLAGS}"
        CXXFLAGS_ADD="${CXXFLAGS}"
        set +a

        for target in "${targets[@]}"; do
            make -C "CPP/7zip/Bundles/${target}" -f 'makefile.gcc'
        done
    )
}

package() {
    local bin="${pkgdir}/usr/bin"

    install -Dm755 -t "${bin}" \
        "build/"{"7za","7zz","7zr"}

    install -Dm644 -t "${pkgdir}/usr/lib" \
        "build/7z.so"

    ln -sT "7zz" "${bin}/7z"

    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
        "DOC/"{"copying.txt","License.txt","unRarLicense.txt"}

    install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
        "DOC/"{"7zC.txt","7zFormat.txt","lzma.txt","Methods.txt","readme.txt","src-history.txt"}
}
