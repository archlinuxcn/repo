# Maintainer: Rasmus Moorats <xx+aur@nns.ee>

pkgname=opensnitch-ebpf-module
_pkgname=opensnitch
pkgver=1.6.5
pkgrel=1
pkgdesc="eBPF process monitor module for opensnitch"
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/evilsocket/opensnitch"
license=('GPL3')
makedepends=('bc' 'clang' 'libelf' 'linux-headers' 'llvm')
checkdepends=('llvm')
depends=('opensnitch')
source=("${_pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('5ebbd5c40c6efcfee8656c50e8b1523078f2633d93bab0dd1d529b1aa2ff36e8')
options=('!strip') # we're stripping with llvm-strip

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}/ebpf_prog"
  KDIR="/usr/src/linux"

  # we set -fno-stack-protector here to work around a clang regression
  # this is fine - bpf programs do not use stack protectors
  CLANG="clang -fno-stack-protector" ARCH="$CARCH" KERNEL_DIR="$KDIR" KERNEL_HEADERS="$KDIR" make
  llvm-strip -g opensnitch*.o
}

check() {
  REQUIRED_SECTIONS=(
    kprobe/{tcp_v{4,6}_connect,udp{,v6}_sendmsg,iptunnel_xmit}
    maps/{{tcp,udp}{,v6}Map,tcp{,v6}sock,bytes,debug}
  )

  SECTIONS=$(llvm-readelf \
    "${srcdir}/${_pkgname}-${pkgver}/ebpf_prog/opensnitch.o" \
    --section-headers)

  for section in "${REQUIRED_SECTIONS[@]}"; do
    grep -q " ${section}" <<< "$SECTIONS" || {
      echo "Failed to build opensnitch.o properly, section ${section} missing!"
      return 1
    }
  done
}

package() {
  install -Dm644 "${srcdir}/${_pkgname}-${pkgver}/ebpf_prog/opensnitch"*".o" -t \
    "${pkgdir}/usr/lib/opensnitchd/ebpf"
}
