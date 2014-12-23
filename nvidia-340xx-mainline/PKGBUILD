# Maintainer: ykelvis < yk [at] archlinuxcn [dot] org >
# Original arch package <nvidia-340xx-ck> by: graysky <graysky AT archlnux.us>

pkgname=nvidia-340xx-mainline
pkgver=340.65
_extramodules=extramodules-3.19-mainline
pkgrel=4
pkgdesc="NVIDIA drivers for linux-mainline, 340xx legacy branch."
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
depends=('linux-mainline>=3.19rc1' 'linux-mainline<3.20rc1' "nvidia-340xx-libgl" "nvidia-340xx-utils=${pkgver}")
makedepends=('linux-mainline-headers>=3.19rc1' 'linux-mainline-headers<3.20rc1')
conflicts=('nvidia-96xx' 'nvidia-173xx' 'nvidia-mainline')
license=('custom')
install=nvidia.install
options=(!strip)
source=('nvidia-3.18.patch' 'nvidia-3.19.patch')
sha256sums=('c9986c306f452614fcf23990c55ffe12bdc451bcbd65a5200269f90a722a3d35'
 'ab04f61c52fa2e0caf133cb5bfd8f42ed124af82d8cafd73f11e2e5ddc685056')
 
 
if [ "$CARCH" = "i686" ]; then
    _arch='x86'
    _pkg="NVIDIA-Linux-${_arch}-${pkgver}"
    source+=("ftp://download.nvidia.com/XFree86/Linux-x86/${pkgver}/NVIDIA-Linux-x86-${pkgver}.run")
    sha256sums+=('e78511435d7794cac09916b98857d98d0c36607ac4dfde0b05ea4aef26ecd973')
elif [ "$CARCH" = "x86_64" ]; then
    _arch='x86_64'
   _pkg="NVIDIA-Linux-${_arch}-${pkgver}-no-compat32"
    source+=("ftp://download.nvidia.com/XFree86/Linux-x86_64/${pkgver}/NVIDIA-Linux-x86_64-${pkgver}-no-compat32.run")
    sha256sums+=('03c2c8d2041d4734d57e831e2b703bbed4a6152d3e25de3fad586035da704b79')
fi

prepare() {
    sh "${_pkg}.run" --extract-only
    cd "${_pkg}"
    # patches here
    # https://devtalk.nvidia.com/default/topic/783364/343-22-driver-incompatible-with-linux-3-18-/
    patch -Np0 -i ${srcdir}/nvidia-3.18.patch
    patch -Np1 -i ${srcdir}/nvidia-3.19.patch
}

build() {
    _kernver="$(cat /usr/lib/modules/${_extramodules}/version)"
    cd "${_pkg}"/kernel
    make SYSSRC=/usr/lib/modules/"${_kernver}/build" module

    cd uvm
    make SYSSRC=/usr/lib/modules/"${_kernver}/build" module
}

package() {
    install -D -m644 "${srcdir}/${_pkg}/kernel/nvidia.ko" \
        "${pkgdir}/usr/lib/modules/${_extramodules}/nvidia.ko"
    install -D -m644 "${srcdir}/${_pkg}/kernel/uvm/nvidia-uvm.ko" \
        "${pkgdir}/usr/lib/modules/${_extramodules}/nvidia-uvm.ko"
    gzip "${pkgdir}/usr/lib/modules/${_extramodules}/"*.ko
    sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='${_extramodules}'/" "${startdir}/nvidia.install"
}

