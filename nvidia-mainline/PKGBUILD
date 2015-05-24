# Maintainer: Rouven Rastetter <r3ddr4gon@firaweb.de>
# Contributors: Mikael Eriksson <mikael_eriksson@miffe.org>
#               Cian Mc Govern <cianmcgovern91@gmail.com>
#               Tom Englund <tomenglund26@gmail.com>
#               Tomasz Przybył <fademind@gmail.com>
# Original arch package by: Thomas Baechler <thomas@archlinux.org>

pkgname=nvidia-mainline
pkgver=352.09
_extramodules=extramodules-4.1-mainline
pkgrel=1
pkgdesc="NVIDIA drivers for linux-mainline"
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
depends=('linux-mainline>=4.1rc1' 'linux-mainline<4.2rc1' "nvidia-libgl" "nvidia-utils=${pkgver}")
makedepends=('linux-mainline-headers>=4.1rc1' 'linux-mainline-headers<4.2rc1')
license=('custom')
install=nvidia.install
options=(!strip)

if [ "$CARCH" = "i686" ]; then
    _arch='x86'
    _pkg="NVIDIA-Linux-${_arch}-${pkgver}"
    source=("http://us.download.nvidia.com/XFree86/Linux-${_arch}/${pkgver}/${_pkg}.run")
    sha256sums=('a799e5e9016f23dd7f69a74844652dcebdf0f655bf2d8b72370e22b19e8b98d3')
elif [ "$CARCH" = "x86_64" ]; then
    _arch='x86_64'
    _pkg="NVIDIA-Linux-${_arch}-${pkgver}-no-compat32"
    source=("http://us.download.nvidia.com/XFree86/Linux-${_arch}/${pkgver}/${_pkg}.run")
    sha256sums=('385137b4e6492710890f621cc09a0ef14f0ab5d90829a1f9b14c689b0b663848')
fi

prepare() {
    sh "${_pkg}.run" --extract-only
    cd "${_pkg}"
    # patches here
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
