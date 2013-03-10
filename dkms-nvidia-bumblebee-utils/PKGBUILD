# Maintainer: jarda-wien <xstej70@gmail.com>
# Former maintainer: Jason Melton <jason.melton@gmail.com>
# Contributor: Atilla ÖNTAŞ <tarakbumba@gmail.com>
# Maintainer: xgdgsc<xgdgsc@gmail.com>

pkgname=dkms-nvidia-bumblebee-utils
_pkgname=nvidia
pkgver=313.26
pkgrel=1
pkgdesc="NVIDIA dynamic kernel module (DKMS) drivers WITH Utils, All in one package to simplify update process(merge of dkms-nvidia and nvidia-utils-bumblebee)"
arch=(i686 x86_64)
url="http://www.nvidia.com/"
license=(custom)
depends=("dkms" 'xorg-server' 'pangox-compat' )
optdepends=('gtk2: nvidia-settings' 'pkg-config: nvidia-xconfig'
            'opencl-nvidia: OpenCL support')
#optdepends=("nvidia-utils=${pkgver}")
provides=("nvidia=${pkgver}" "nvidia-utils=${pkgver}" "nvidia-utils-bumblebee=${pkgver}")
conflicts=("nvidia" "nvidia-utils" "nvidia-bumblebee" "nvidia-utils-bumblebee" "dkms-nvidia")
replaces=("dkms-nvidia" "nvidia-utils-bumblebee" )
install="${pkgname}.install"
options=(!strip)

if [ "$CARCH" = "i686" ]; then
	_arch='x86'
	_pkg="NVIDIA-Linux-${_arch}-${pkgver}"
  source=("ftp://download.nvidia.com/XFree86/Linux-${_arch}/${pkgver}/${_pkg}.run")
  md5sums=('3c2f5138d0fec58b27e26c5b37d845b8')
elif [ "$CARCH" = "x86_64" ]; then
	_arch='x86_64'
	_pkg="NVIDIA-Linux-${_arch}-${pkgver}-no-compat32"
  source=("ftp://download.nvidia.com/XFree86/Linux-${_arch}/${pkgver}/${_pkg}.run")
  md5sums=('2d35124fa5a4b009f170fe893b5d07e3')
fi

source[1]="dkms.conf"
md5sums[1]='addb093f1c42ca0f54760a5551eebae3'

#source[2]="linux-3.7.patch"
#md5sums[2]='e10a5daf9f53015427d8bc493cdf3928'

build() {
	cd $srcdir
	sh ${_pkg}.run --extract-only
	cd "${_pkg}/kernel"
	#patch -Np3 -i "${srcdir}"/linux-3.7.patch
}

create_links() {
    # create soname links
    while read -d '' _lib; do
        _soname="$(dirname "${_lib}")/$(readelf -d "${_lib}" | sed -nr 's/.*Library soname: \[(.*)\].*/\1/p')"
        [[ -e "${_soname}" ]] || ln -s "$(basename "${_lib}")" "${_soname}"
        [[ -e "${_soname/.[0-9]*/}" ]] || ln -s "$(basename "${_soname}")" "${_soname/.[0-9]*/}"
    done < <(find "${pkgdir}" -type f -name '*.so*' -print0)
}

package() 
{

  #Utils :
   cd "${srcdir}/${_pkg}"
    # X driver
    install -D -m755 nvidia_drv.so "${pkgdir}/usr/lib/xorg/modules/drivers/nvidia_drv.so"
    # GLX extension module for X
    install -D -m755 "libglx.so.${pkgver}" "${pkgdir}/usr/lib/nvidia-bumblebee/xorg/modules/extensions/libglx.so.${pkgver}"
    ln -s "libglx.so.${pkgver}" "${pkgdir}/usr/lib/nvidia-bumblebee/xorg/modules/extensions/libglx.so"	# X doesn't find glx otherwise
    # OpenGL library
    install -D -m755 "libGL.so.${pkgver}" "${pkgdir}/usr/lib/nvidia-bumblebee/libGL.so.${pkgver}"
    ln -s "libGL.so.${pkgver}" "${pkgdir}/usr/lib/nvidia-bumblebee/libGL.so.1"
    # OpenGL core library
    install -D -m755 "libnvidia-glcore.so.${pkgver}" "${pkgdir}/usr/lib/libnvidia-glcore.so.${pkgver}"
    # XvMC
    #install -D -m644 libXvMCNVIDIA.a "${pkgdir}/usr/lib/libXvMCNVIDIA.a"
    #install -D -m755 "libXvMCNVIDIA.so.${pkgver}" "${pkgdir}/usr/lib/libXvMCNVIDIA.so.${pkgver}"
    # VDPAU
    install -D -m755 "libvdpau_nvidia.so.${pkgver}" "${pkgdir}/usr/lib/vdpau/libvdpau_nvidia.so.${pkgver}"
    # nvidia-tls library
    install -D -m755 "tls/libnvidia-tls.so.${pkgver}" "${pkgdir}/usr/lib/libnvidia-tls.so.${pkgver}"
    install -D -m755 "libnvidia-cfg.so.${pkgver}" "${pkgdir}/usr/lib/libnvidia-cfg.so.${pkgver}"

    install -D -m755 "libnvidia-ml.so.${pkgver}" "${pkgdir}/usr/lib/libnvidia-ml.so.${pkgver}"

    # CUDA
    install -D -m755 "libcuda.so.${pkgver}" "${pkgdir}/usr/lib/libcuda.so.${pkgver}"
    install -D -m755 "libnvcuvid.so.${pkgver}" "${pkgdir}/usr/lib/libnvcuvid.so.${pkgver}"

    # nvidia-xconfig
    install -D -m755 nvidia-xconfig "${pkgdir}/usr/bin/nvidia-xconfig"
    install -D -m644 nvidia-xconfig.1.gz "${pkgdir}/usr/share/man/man1/nvidia-xconfig.1.gz"
    # nvidia-settings
    install -D -m755 nvidia-settings "${pkgdir}/usr/bin/nvidia-settings"
    install -D -m644 nvidia-settings.1.gz "${pkgdir}/usr/share/man/man1/nvidia-settings.1.gz"
    install -D -m644 nvidia-settings.desktop "${pkgdir}/usr/share/applications/nvidia-settings.desktop"
    install -D -m644 nvidia-settings.png "${pkgdir}/usr/share/pixmaps/nvidia-settings.png"
    sed -e 's:__UTILS_PATH__:/usr/bin:' -e 's:__PIXMAP_PATH__:/usr/share/pixmaps:' -i "${pkgdir}/usr/share/applications/nvidia-settings.desktop"
    # nvidia-bug-report
    install -D -m755 nvidia-bug-report.sh "${pkgdir}/usr/bin/nvidia-bug-report.sh"
    # nvidia-smi
    install -D -m755 nvidia-smi "${pkgdir}/usr/bin/nvidia-smi"
    install -D -m644 nvidia-smi.1.gz "${pkgdir}/usr/share/man/man1/nvidia-smi.1.gz"


    install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/nvidia/LICENSE"
    ln -s nvidia "${pkgdir}/usr/share/licenses/nvidia-utils"
    install -D -m644 README.txt "${pkgdir}/usr/share/doc/nvidia/README"
    install -D -m644 NVIDIA_Changelog "${pkgdir}/usr/share/doc/nvidia/NVIDIA_Changelog"
    ln -s nvidia "${pkgdir}/usr/share/doc/nvidia-utils"
    
     create_links
     
     
#dkms-nvidia
 	mkdir -p                                ${pkgdir}/usr/src/${_pkgname}-${pkgver}
 	cp -a       ${srcdir}/${_pkg}/kernel/*  ${pkgdir}/usr/src/${_pkgname}-${pkgver}
	cp          ${srcdir}/dkms.conf         ${pkgdir}/usr/src/${_pkgname}-${pkgver}

  install -d -m755 $pkgdir/etc/modprobe.d
  echo "blacklist nouveau" >> $pkgdir/etc/modprobe.d/nouveau_blacklist.conf
  
  
}
