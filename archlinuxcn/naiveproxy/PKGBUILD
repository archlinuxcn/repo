# Maintainer: bgme <i@bgme.me>
# Contributor: navigaid <navigaid@gmail.com>

pkgname=naiveproxy
pkgdesc="A Proxy using Chrome's network stack to camouflage traffic with strong censorship resistence and low detectablility."
pkgver=149.0.7827.114_1
pkgrel=1
_pkgver=149.0.7827.114
_pkgrel=1
arch=('x86_64')
url='https://github.com/klzgrad/naiveproxy'
license=('BSD-3-Clause')
depends=("gcc-libs" "glibc")
makedepends=("ninja" "gn" "ccache" "python")
checkdepends=("python" "openssl")

_PGO_PATH='chrome-linux-7827-1780682012-f62c73d731b52a07fffe1a178a38103191b0fddd-4185813e9f60e6a1ea3ac12cbce62f4e511cb234.profdata'
_clang_path='clang-llvmorg-23-init-10931-g20b6ec66-8.tar.xz'

source=(
  "naiveproxy.service"
  "naiveproxy@.service"
  "${pkgname}-${_pkgver}-${_pkgrel}.tar.gz::https://github.com/klzgrad/naiveproxy/archive/refs/tags/v${_pkgver}-${_pkgrel}.tar.gz"
  "${_PGO_PATH}::https://storage.googleapis.com/chromium-optimization-profiles/pgo_profiles/${_PGO_PATH}"
  "${_clang_path}::https://commondatastorage.googleapis.com/chromium-browser-clang/Linux_x64/${_clang_path}"
)

noextract=(
  "${_clang_path}"
)

sha1sums=('f959ceed9d451e3344d99b2a1572ca27416a5675'
          '278983a6edd5477e8f6f0557ea206f236fdc51dc'
          'a994037e9517b1a1a42ceb41ef6011ed895203c4'
          'f62c73d731b52a07fffe1a178a38103191b0fddd'
          'bff7967f159d8fece6bc1eefae42849a53fdc0fb')
sha256sums=('8b56b5a401cb7f77b50376ec27e40445f4bdbe85890ab717327de187ded92c53'
            'dd8f8e154832d49795be417557db9cc408976cc324452715f5d796b40e5a752d'
            '0080c344e05f1df0f3f083654800a19ff89dbd8aa96b98b28b4b3bab4fe3baa8'
            '2788d18df98ca5240a5cb2cdbdb6fb94ea154be1ce7b51f9a9eb91e8093f725a'
            '6aa45b7398e915919ce07a5e1e15e8710327957f61c1d97d18e77e5f167e9d14')

backup=('etc/naiveproxy/config.json')
provides=('naiveproxy')
conflicts=('naiveproxy')

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
    chrome_pgo_phase=2
    symbol_level=0"

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

    use_udev=false
    use_aura=false
    use_ozone=false
    use_gio=false
    use_platform_icu_alternatives=true
    use_glib=false
    is_perfetto_embedder=true

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
    enable_quic_proxy_support=true
    enable_disk_cache_sql_backend=false

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
  popd

  pushd "${srcdir}/${pkgname}-${_pkgver}-${_pkgrel}"
  install -d -m750 "${pkgdir}/etc/naiveproxy"
  install -Dm644 src/config.json "${pkgdir}/etc/naiveproxy/config.json"
  install -Dm755 src/out/Release/naive "${pkgdir}/usr/bin/naiveproxy"
  install -Dm644 README.md "${pkgdir}/usr/share/doc/naiveproxy/README.md"
  install -Dm644 USAGE.txt "${pkgdir}/usr/share/doc/naiveproxy/USAGE.txt"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/naiveproxy/LICENSE"
  popd
}
