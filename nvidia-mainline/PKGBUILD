# Maintainer: Rouven Rastetter <r3ddr4gon@firaweb.de>
# Contributors: Mikael Eriksson <mikael_eriksson@miffe.org>
#               Cian Mc Govern <cianmcgovern91@gmail.com>
#               Tom Englund <tomenglund26@gmail.com>
#               Tomasz Przybył <fademind@gmail.com>
# Original arch package by: Thomas Baechler <thomas@archlinux.org>

pkgname=nvidia-mainline
pkgver=355.11
_extramodules=extramodules-4.3-mainline
pkgrel=1
pkgdesc="NVIDIA drivers for linux-mainline"
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
depends=('linux-mainline>=4.3rc1' 'linux-mainline<4.4rc1' "nvidia-libgl" "nvidia-utils=${pkgver}")
makedepends=('linux-mainline-headers>=4.3rc1' 'linux-mainline-headers<4.4rc1')
license=('custom')
install=nvidia.install
options=(!strip)
source=("nvidia-4.3.patch")
sha256sums=('1e252fdb7a7e6396a9fbe71a9501345d86b23080048fd1280b23c139e0299415')

if [ "$CARCH" = "i686" ]; then
    _arch='x86'
    _pkg="NVIDIA-Linux-${_arch}-${pkgver}"
    source+=("http://us.download.nvidia.com/XFree86/Linux-${_arch}/${pkgver}/${_pkg}.run")
    sha256sums+=('94ce6b879581b931b84d83a9111040b9a5aa9306b012b4380cd93f6ffede3066')
elif [ "$CARCH" = "x86_64" ]; then
    _arch='x86_64'
    _pkg="NVIDIA-Linux-${_arch}-${pkgver}-no-compat32"
    source+=("http://us.download.nvidia.com/XFree86/Linux-${_arch}/${pkgver}/${_pkg}.run")
    sha256sums+=('0fcc6a62a05fc11344aff375faaca56b358ee1252f6b2c98c00d628ea3d0f842')
fi

prepare() {
    sh "${_pkg}.run" --extract-only
    cd "${_pkg}"
    # patches here
    patch -Np1 -i ${srcdir}/nvidia-4.3.patch
}

build() {
    _kernver="$(cat /usr/lib/modules/${_extramodules}/version)"
    cd "${_pkg}"/kernel
    make SYSSRC=/usr/lib/modules/"${_kernver}/build" module
}

package() {
    install -D -m644 "${srcdir}/${_pkg}/kernel/nvidia.ko" \
        "${pkgdir}/usr/lib/modules/${_extramodules}/nvidia.ko"
    if [[ "$CARCH" = "x86_64" ]]; then
        install -D -m644 "${srcdir}/${_pkg}/kernel/nvidia-uvm.ko" \
            "${pkgdir}/usr/lib/modules/${_extramodules}/nvidia-uvm.ko"
    fi
    gzip "${pkgdir}/usr/lib/modules/${_extramodules}/"*.ko
    sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='${_extramodules}'/" "${startdir}/nvidia.install"
}
