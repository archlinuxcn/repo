# Maintainer:
# Contributor: xiretza <xiretza+aur@xiretza.xyz>
# Contributor: Graham Edgecombe <gpe@grahamedgecombe.com>

_ARCHS=('ecp5' 'ice40' 'himbaechel' 'nexus' 'generic')

_pkgname="nextpnr"
pkgname="$_pkgname-git"
pkgver=0.8.r20.g5206162
pkgrel=1
pkgdesc='Portable FPGA place and route tool'
url='https://github.com/YosysHQ/nextpnr'
license=('ISC')
arch=('i686' 'x86_64')

depends=(
  'boost-libs'
  'python'
  'qt5-base'
)
makedepends=(
  'boost'
  'cmake'
  'eigen'
  'git'
  'ninja'
)

provides=("nextpnr=$pkgver")
conflicts=('nextpnr')

_source_main() {
  _pkgsrc="$_pkgname"
  source=("$_pkgsrc"::"git+$url.git")
  sha256sums=('SKIP')
}

_source_nextpnr() {
  local _sources_add=(
    #'corrosion-rs.corrosion'::'git+https://github.com/corrosion-rs/corrosion.git'
    #'gatecat.nextpnr-xilinx-meta'::'git+https://github.com/gatecat/nextpnr-xilinx-meta.git'
    'yosyshq.nextpnr-tests'::'git+https://github.com/YosysHQ/nextpnr-tests.git'
  )

  local _p
  for _p in ${_sources_add[@]}; do
    source+=("$_p")
    sha256sums+=('SKIP')
  done

  _prepare_nextpnr() (
    cd "$srcdir/$_pkgsrc"
    local _submodules=(
      #'corrosion-rs.corrosion'::'3rdparty/corrosion'
      #'gatecat.nextpnr-xilinx-meta'::'himbaechel/uarch/xilinx/meta'
      'yosyshq.nextpnr-tests'::'tests'
    )
    _submodule_update
  )
}

_source_main
_source_nextpnr

pkgver() {
  cd "$_pkgsrc"
  git describe --long --tags --abbrev=7 \
    | sed -E 's/^[^0-9]*//;s/([^-]*-g)/r\1/;s/-/./g'
}

prepare() {
  _submodule_update() {
    local _module
    for _module in "${_submodules[@]}"; do
      git submodule init "${_module##*::}"
      git submodule set-url "${_module##*::}" "$srcdir/${_module%%::*}"
      git -c protocol.file.allow=always submodule update "${_module##*::}"
    done
  }

  _prepare_nextpnr
}

build() {
  local _cmake_options=(
    -B build
    -S "$_pkgsrc"
    -G Ninja
    -DCMAKE_BUILD_TYPE=None
    -DCMAKE_INSTALL_PREFIX='/usr'
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5
    -DUSE_OPENMP=ON
    -DUSE_IPO=OFF
    -DBUILD_GUI=ON
    -DBUILD_TESTS=ON
    -Wno-dev

    -DARCH=$(
      IFS=';'
      echo "${_ARCHS[*]}"
    )
    "${_CONFIG[@]}"
  )

  cmake "${_cmake_options[@]}"
  cmake --build build
}

check() {
  ctest --test-dir build --output-on-failure
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 "$_pkgsrc"/COPYING -t "$pkgdir/usr/share/licenses/$pkgname/"
}

_CONFIG=()
for _arch in ${_ARCHS[@]}; do
  case $_arch in
    ice40)
      makedepends+=(
        'icestorm' # AUR
      )
      _CONFIG+=('-DICESTORM_INSTALL_PREFIX=/usr')
      ;;
    ecp5)
      makedepends+=(
        'prjtrellis'
        'prjtrellis-db>=r269' # AUR
      )
      _CONFIG+=('-DTRELLIS_INSTALL_PREFIX=/usr')
      ;;
    nexus)
      makedepends+=(
        'prjoxide' # AUR
        # capnproto-java # AUR
      )
      _CONFIG+=('-DOXIDE_INSTALL_PREFIX=/usr')
      ;;
    himbaechel)
      makedepends+=(
        'prjapicula-git' # AUR
        # 'python-crc' # AUR
      )
      _CONFIG+=('-DHIMBAECHEL_UARCH=gowin')
      ;;
    generic)
      # NOOP
      ;;
    *)
      echo "Unhandled architecture: $_arch" >&2
      exit 1
      ;;
  esac
done
