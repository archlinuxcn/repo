# Maintainer: FadeMind <fademind@gmail.com>
# Contributor: Lev Lybin <aur@devtrue.net>
# Contributor: Rouven Rastetter <r3ddr4gon@firaweb.de>
# Contributor: Mikael Eriksson <mikael_eriksson@miffe.org>
# Contributor: Cian Mc Govern <cianmcgovern91@gmail.com>
# Contributor: Tom Englund <tomenglund26@gmail.com>

pkgbase=nvidia-mainline
pkgname=(nvidia-mainline nvidia-mainline-dkms)
pkgver=375.26
_extramodules=extramodules-4.10-mainline
pkgrel=1
pkgdesc="NVIDIA drivers for linux-mainline"
arch=('i686' 'x86_64')
url="http://www.nvidia.com/"
makedepends=('nvidia-libgl' "nvidia-utils=${pkgver}" 'linux-mainline' 'linux-mainline-headers')
license=('custom')
options=('!strip')
source=("linux-4.10-rc1.patch")
source_i686=("http://us.download.nvidia.com/XFree86/Linux-x86/${pkgver}/NVIDIA-Linux-x86-${pkgver}.run")
source_x86_64=("http://us.download.nvidia.com/XFree86/Linux-x86_64/${pkgver}/NVIDIA-Linux-x86_64-${pkgver}-no-compat32.run" "linux-4.10-rc1-x86_64.patch")
sha512sums=('db48665e2e68bdf3e1381ff5b9b8c70056c6a2b9f6ed27d9882be2b62258d68c595f6230552f03b5addcde16cc3216722f3811a6fa4bfd9cb3f1ca9d0aa57ab5')
sha512sums_i686=('3bc859a95469a45f3c627018248d83e178d160385c3d17d9f890b0d142ecd1220fb21c442e4fe7755b831227a9c820736f447b162acd9699819c6e8145d6d841')
sha512sums_x86_64=('f52f6597daa1eaf4cbd934d785da6028ef23ecef98e14746143e3738504f8d65b73788abbcf9fd812317fc2c53cdf1c4d4839de57fafdea1930a08c6b21f1992'
                   'd3adcd8af6f1bd4672c40ae37a979798d6a00e9fcf4aef48a15b525201a22fa43bed91cc0aca57fe75f1673afb1f0018d8f31494c64592897fb51e0d090cca17')

[[ "$CARCH" = "i686" ]] && _pkg="NVIDIA-Linux-x86-${pkgver}"
[[ "$CARCH" = "x86_64" ]] && _pkg="NVIDIA-Linux-x86_64-${pkgver}-no-compat32"

prepare() { 
    sh "${_pkg}.run" --extract-only
    cd "${_pkg}"
    # patches here
    patch -p1 -i "$srcdir/linux-4.10-rc1.patch"
    if [[ "$CARCH" = "x86_64" ]];
       then patch -p1 -i "$srcdir/linux-4.10-rc1-x86_64.patch"
    fi

    cp -a kernel kernel-dkms
    cd kernel-dkms
    sed -i "s/__VERSION_STRING/${pkgver}/" dkms.conf
    sed -i 's/__JOBS/`nproc`/' dkms.conf
    sed -i 's/__DKMS_MODULES//' dkms.conf
    sed -i '$iBUILT_MODULE_NAME[0]="nvidia"\
DEST_MODULE_LOCATION[0]="/kernel/drivers/video"\
BUILT_MODULE_NAME[1]="nvidia-uvm"\
DEST_MODULE_LOCATION[1]="/kernel/drivers/video"\
BUILT_MODULE_NAME[2]="nvidia-modeset"\
DEST_MODULE_LOCATION[2]="/kernel/drivers/video"\
BUILT_MODULE_NAME[3]="nvidia-drm"\
DEST_MODULE_LOCATION[3]="/kernel/drivers/video"' dkms.conf
}

build() {
    _kernver="$(cat /usr/lib/modules/${_extramodules}/version)"
    cd "${_pkg}"/kernel
    make SYSSRC=/usr/lib/modules/"${_kernver}/build" module
}

package_nvidia-mainline() {
    pkgdesc="NVIDIA drivers for linux-mainline"
    depends=('linux-mainline' 'linux-mainline' "nvidia-utils=${pkgver}" 'libgl')
    install="${pkgbase}.install"

    install -D -m644 "${srcdir}/${_pkg}/kernel/nvidia.ko" \
        "${pkgdir}/usr/lib/modules/${_extramodules}/nvidia.ko"
    install -D -m644 "${srcdir}/${_pkg}/kernel/nvidia-modeset.ko" \
         "${pkgdir}/usr/lib/modules/${_extramodules}/nvidia-modeset.ko"
    install -D -m644 "${srcdir}/${_pkg}/kernel/nvidia-drm.ko" \
         "${pkgdir}/usr/lib/modules/${_extramodules}/nvidia-drm.ko"

    if [[ "$CARCH" = "x86_64" ]]; then
        install -D -m644 "${srcdir}/${_pkg}/kernel/nvidia-uvm.ko" \
            "${pkgdir}/usr/lib/modules/${_extramodules}/nvidia-uvm.ko"
    fi

    sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='${_extramodules}'/" "${startdir}/${pkgbase}.install"
    
    gzip "${pkgdir}/usr/lib/modules/${_extramodules}/"*.ko
    install -d -m755 "${pkgdir}/usr/lib/modprobe.d"

    echo "blacklist nouveau" >> "${pkgdir}/usr/lib/modprobe.d/nvidia-mainline.conf"
}

package_nvidia-mainline-dkms() {
    pkgdesc="NVIDIA driver sources for linux-mainline"
    depends=('dkms' "nvidia-utils=$pkgver" 'libgl')
    optdepends=('linux-mainline-headers: Build the module for linux-mainline kernel')
    conflicts+=('nvidia-mainline')

    cd ${_pkg}
    install -dm 755 "${pkgdir}"/usr/{lib/modprobe.d,src}
    cp -dr --no-preserve='ownership' kernel-dkms "${pkgdir}/usr/src/nvidia-${pkgver}"
    echo 'blacklist nouveau' > "${pkgdir}/usr/lib/modprobe.d/nvidia-mainline.conf"
}
