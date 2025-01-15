# Maintainer: bgme <i@bgme.me>
# Contributor: navigaid <navigaid@gmail.com>

pkgname=naiveproxy
pkgdesc="A Proxy using Chrome's network stack to camouflage traffic with strong censorship resistence and low detectablility."
pkgver=132.0.6834.79_1
pkgrel=1
_pkgver=132.0.6834.79
_pkgrel=1
arch=('x86_64')
url='https://github.com/klzgrad/naiveproxy'
license=('BSD-3-Clause')
depends=("gcc-libs" "glibc")
makedepends=("ninja" "gn" "ccache" "python")
checkdepends=("python" "openssl")

_PGO_PATH='chrome-linux-6834-1736251055-c6875f294105fb21f11dbeeba26322cc336d42b4-afcffa295c0905266759c32ddd4e3f29d85e820c.profdata'
_clang_path='clang-llvmorg-20-init-9764-gb81d8e90-6.tar.xz'

source=(
  "naiveproxy.service"
  "naiveproxy@.service"
  "naiveproxy.sysusers"
  "${pkgname}-${_pkgver}-${_pkgrel}.tar.gz::https://github.com/klzgrad/naiveproxy/archive/refs/tags/v${_pkgver}-${_pkgrel}.tar.gz"
  "${_PGO_PATH}::https://storage.googleapis.com/chromium-optimization-profiles/pgo_profiles/${_PGO_PATH}"
  "${_clang_path}::https://commondatastorage.googleapis.com/chromium-browser-clang/Linux_x64/${_clang_path}"
)

noextract=(
  "${_clang_path}"
)

sha1sums=('4c18f44ba51d40bfd7e6ae8ecb30b8e812acb8e8'
          '013b31ae43e309bc6560b61e8b4196f8f14f738f'
          '3727d7da81b1480d60e593a7d6878d981b35c4f6'
          'cdb87a0fb982f84aef0bca3f7b8733b4b5f9a8a3'
          'c6875f294105fb21f11dbeeba26322cc336d42b4'
          'b5a58e97fdfd57c34a6163ddd75441aebac14466')
sha256sums=('c05026423ca08e2c712745b717c23395e344f2c99b2dad30beed8e26922d268f'
            'daa0f591233625730168f3ea006f1d5a7e439e26b35a1051d957e394aa8a4440'
            '5bc9ef361e6303e151b6e63deb31b47e24a4f34ade4d8f092a04bc98e89a2edb'
            '75534ef7ea132aa077b627a8faac71b0b91b94de4db3f305ebbf1a411a774bec'
            '8eb1229f30fa9a74aff86db8499b2cee425883de648a621f0a76af56c56ced7e'
            '10fbc53c0730a50e2117b3414a45784667d6cf7d91a3bcaab2b3a78ede08c5d2')

backup=('etc/naiveproxy/config.json')
provides=('naiveproxy')
conflicts=('naiveproxy-git' 'naiveproxy-bin')

prepare() {
  SRC_DIR="${srcdir}/${pkgname}-${_pkgver}-${_pkgrel}/src"

  mkdir -p "${SRC_DIR}/chrome/build/pgo_profiles"
  cp ${_PGO_PATH} "${SRC_DIR}/chrome/build/pgo_profiles/"

  mkdir -p "${SRC_DIR}/third_party/llvm-build/Release+Asserts"
  tar xJf ${_clang_path} -C "${SRC_DIR}/third_party/llvm-build/Release+Asserts/"
}

build() {
  SRC_DIR="${srcdir}/${pkgname}-${_pkgver}-${_pkgrel}/src"

  cd "${SRC_DIR}"

  export TMPDIR="$PWD/tmp"
  rm -rf "$TMPDIR"
  mkdir -p "$TMPDIR"

  out=out/Release
  flags="
    is_official_build=true
    exclude_unwind_tables=true
    enable_resource_allowlist_generation=false
    symbol_level=0"

  PYTHON=$(which python3 2>/dev/null)

  export CCACHE_SLOPPINESS=time_macros
  export CCACHE_BASEDIR="$PWD"
  export CCACHE_CPP2=yes
  CCACHE=ccache

  flags="$flags
    cc_wrapper=\"$CCACHE\""

  flags="$flags"'
    is_clang=true
    use_sysroot=false

    fatal_linker_warnings=false
    treat_warnings_as_errors=false

    is_cronet_build=true
    chrome_pgo_phase=2

    enable_base_tracing=false
    use_udev=false
    use_aura=false
    use_ozone=false
    use_gio=false
    use_gtk=false
    use_platform_icu_alternatives=true
    use_glib=false

    disable_file_support=true
    enable_websockets=false
    use_kerberos=false
    disable_file_support=true
    disable_zstd_filter=false
    enable_mdns=false
    enable_reporting=false
    include_transport_security_state_preload_list=false
    enable_device_bound_sessions=false
    enable_bracketed_proxy_uris=true

    use_nss_certs=false
  
    enable_backup_ref_ptr_support=false
    enable_dangling_raw_ptr_checks=false
  '

  # Disable CFI icall for linux x64
  # See https://github.com/llvm/llvm-project/issues/86430
  flags="$flags"'
    use_cfi_icall=false'

  rm -rf "./$out"
  mkdir -p out

  export DEPOT_TOOLS_WIN_TOOLCHAIN=0

  gn gen "$out" "--args=$flags $EXTRA_FLAGS"

  ninja -C "$out" naive
}

check() {
  SRC_DIR="${srcdir}/${pkgname}-${_pkgver}-${_pkgrel}"
  script_dir="${SRC_DIR}/tests"
  naive="${SRC_DIR}/src/out/Release/naive"

  cd /tmp
  python "${script_dir}/basic.py" --naive="$naive"
}

package() {
  pushd "${srcdir}"
  install -Dm644 naiveproxy.service "${pkgdir}/usr/lib/systemd/system/naiveproxy.service"
  install -Dm644 naiveproxy@.service "${pkgdir}/usr/lib/systemd/system/naiveproxy@.service"
  install -Dm644 naiveproxy.sysusers "${pkgdir}/usr/lib/sysusers.d/naiveproxy.conf"
  popd

  pushd "${srcdir}/${pkgname}-${_pkgver}-${_pkgrel}"
  install -d -m750 -o 0 -g 287 "${pkgdir}/etc/naiveproxy"
  install -Dm644 src/config.json "${pkgdir}/etc/naiveproxy/config.json"
  install -Dm755 src/out/Release/naive "${pkgdir}/usr/bin/naiveproxy"
  install -Dm644 README.md "${pkgdir}/usr/share/doc/naiveproxy/README.md"
  install -Dm644 USAGE.txt "${pkgdir}/usr/share/doc/naiveproxy/USAGE.txt"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/naiveproxy/LICENSE"
  popd
}
