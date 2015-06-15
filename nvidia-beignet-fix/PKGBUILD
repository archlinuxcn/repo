# Maintainer: Sven-Hendrik Haase <sh@lutzhaase.com>
# Maintainer: Thomas Baechler <thomas@archlinux.org>

pkgname=nvidia-beignet-fix
pkgver=352.09
_extramodules=extramodules-4.0-beignet-fix
pkgrel=1
pkgdesc="NVIDIA drivers for linux"
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
depends=('linux-beignet-fix>=4.0' 'linux-beignet-fix<4.1'
         "nvidia-libgl" "nvidia-utils=${pkgver}")
makedepends=('linux-beignet-fix-headers>=4.0' 'linux-beignet-fix-headers<4.1')
license=('custom')
install=nvidia.install
options=(!strip)
source=("ftp://download.nvidia.com/XFree86/Linux-x86/${pkgver}/NVIDIA-Linux-x86-${pkgver}.run"
        "ftp://download.nvidia.com/XFree86/Linux-x86_64/${pkgver}/NVIDIA-Linux-x86_64-${pkgver}-no-compat32.run")
md5sums=('0e009686400c522209eaa8ab835ff81f'
         'eb5ad6a07dc03e0a19d5f6fa069c494b')

[[ "$CARCH" = "i686" ]] && _pkg="NVIDIA-Linux-x86-${pkgver}"
[[ "$CARCH" = "x86_64" ]] && _pkg="NVIDIA-Linux-x86_64-${pkgver}-no-compat32"

prepare() {
  sh "${_pkg}.run" --extract-only
  cd "${_pkg}"
  # patches here
}

build() {
  _kernver="$(cat /usr/lib/modules/${_extramodules}/version)"
  cd "${_pkg}"/kernel
  make KERNEL_UNAME=${_kernver} module

  if [[ "$CARCH" = "x86_64" ]]; then
      cd uvm
      make KERNEL_UNAME=${_kernver} module
  fi
}

package() {
  install -D -m644 "${srcdir}/${_pkg}/kernel/nvidia.ko" \
          "${pkgdir}/usr/lib/modules/${_extramodules}/nvidia.ko"

  if [[ "$CARCH" = "x86_64" ]]; then
      install -D -m644 "${srcdir}/${_pkg}/kernel/uvm/nvidia-uvm.ko" \
              "${pkgdir}/usr/lib/modules/${_extramodules}/nvidia-uvm.ko"
  fi

  gzip "${pkgdir}/usr/lib/modules/${_extramodules}/"*.ko
  install -d -m755 "${pkgdir}/usr/lib/modprobe.d"
  echo "blacklist nouveau" >> "${pkgdir}/usr/lib/modprobe.d/nvidia-beignet-fix.conf"
}
