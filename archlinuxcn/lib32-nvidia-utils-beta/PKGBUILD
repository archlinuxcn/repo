# Maintainer : Daniel Bermond <dbermond@archlinux.org>
# Contributor: Det <nimetonmaili g-mail>
# Contributor: Ng Oon-Ee
# Contributor: Dan Vratil
# Contributor: Jeremy Sands
# Contributor: Erik Hardesty
# Contributor: josephgbr

pkgbase=lib32-nvidia-utils-beta
pkgname=('lib32-nvidia-utils-beta' 'lib32-opencl-nvidia-beta')
pkgver=525.85.05
pkgrel=1
pkgdesc='NVIDIA drivers utilities (32-bit, beta version)'
arch=('x86_64')
url='https://www.nvidia.com/'
license=('custom')
makedepends=("nvidia-utils-beta>=${pkgver}") # to avoid conflict during installation in the build chroot
options=('!strip')
_pkg="NVIDIA-Linux-${CARCH}-${pkgver}"
source=("https://us.download.nvidia.com/XFree86/Linux-${CARCH}/${pkgver}/${_pkg}.run")
sha256sums=('ea63b4253403b224bb7313a8977a920dfe9d203d661dd5f6fc26585a70179140')

# create soname links
_create_links() {
    local _lib
    local _soname
    local _base
    find "$pkgdir" -type f -name '*.so*' ! -path '*xorg/*' -print0 | while read -d $'\0' _lib
    do
        _soname="$(dirname "$_lib")/$(readelf -d "$_lib" | grep -Po 'SONAME.*: \[\K[^]]*' || true)"
        _base="$(printf '%s' "$_soname" | sed -r 's/(.*).so.*/\1.so/')"
        [ -e "$_soname" ] || ln -s "$(basename "$_lib")"    "$_soname"
        [ -e "$_base"   ] || ln -s "$(basename "$_soname")" "$_base"
    done
}

prepare() {
    # extract the source file
    [ -d "$_pkg" ] && rm -rf "$_pkg"
    printf '%s\n' "  -> Self-Extracting ${_pkg}.run..."
    sh "${_pkg}.run" --extract-only
}

package_lib32-opencl-nvidia-beta() {
    pkgdesc='OpenCL implemention for NVIDIA (32-bit, beta version)'
    depends=('lib32-zlib' 'lib32-gcc-libs' "lib32-nvidia-utils-beta>=${pkgver}")
    optdepends=('opencl-headers: headers necessary for OpenCL development')
    provides=("lib32-opencl-nvidia=${pkgver}" 'lib32-opencl-driver')
    conflicts=('lib32-opencl-nvidia')
    
    cd "${_pkg}/32"
    
    # OpenCL
    install -D -m755 "libnvidia-compiler.so.${pkgver}" -t "${pkgdir}/usr/lib32"
    install -D -m755 "libnvidia-opencl.so.${pkgver}"   -t "${pkgdir}/usr/lib32"
    
    _create_links
    
    # license
    install -D -m644 "${srcdir}/${_pkg}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_lib32-nvidia-utils-beta() {
    depends=('lib32-zlib' 'lib32-gcc-libs' 'lib32-libglvnd' "nvidia-utils-beta>=${pkgver}")
    optdepends=('lib32-opencl-nvidia-beta: for OpenCL support')
    provides=("lib32-nvidia-utils=${pkgver}" 'lib32-vulkan-driver' 'lib32-opengl-driver'
              "lib32-nvidia-libgl=${pkgver}" "lib32-nvidia-libgl-beta=${pkgver}")
    conflicts=('lib32-nvidia-utils' 'lib32-nvidia-libgl')
    replaces=('lib32-nvidia-libgl')
    
    cd "${_pkg}/32"
    
    install -D -m755 "libGLX_nvidia.so.${pkgver}" -t "${pkgdir}/usr/lib32"
    
    # OpenGL libraries
    install -D -m755 "libEGL_nvidia.so.${pkgver}"       -t "${pkgdir}/usr/lib32"
    install -D -m755 "libGLESv1_CM_nvidia.so.${pkgver}" -t "${pkgdir}/usr/lib32"
    install -D -m755 "libGLESv2_nvidia.so.${pkgver}"    -t "${pkgdir}/usr/lib32"
    
    # OpenGL core library
    install -D -m755 "libnvidia-glcore.so.${pkgver}"  -t "${pkgdir}/usr/lib32"
    install -D -m755 "libnvidia-eglcore.so.${pkgver}" -t "${pkgdir}/usr/lib32"
    install -D -m755 "libnvidia-glsi.so.${pkgver}"    -t "${pkgdir}/usr/lib32"
    
    # misc
    install -D -m755 "libnvidia-fbc.so.${pkgver}"       -t "${pkgdir}/usr/lib32"
    install -D -m755 "libnvidia-encode.so.${pkgver}"    -t "${pkgdir}/usr/lib32"
    install -D -m755 "libnvidia-ml.so.${pkgver}"        -t "${pkgdir}/usr/lib32"
    install -D -m755 "libnvidia-glvkspirv.so.${pkgver}" -t "${pkgdir}/usr/lib32"
    
    # VDPAU
    install -D -m755 "libvdpau_nvidia.so.${pkgver}" -t "${pkgdir}/usr/lib32/vdpau"
    
    # nvidia-tls library
    install -D -m755 "libnvidia-tls.so.${pkgver}" -t "${pkgdir}/usr/lib32"
    
    # CUDA
    install -D -m755 "libcuda.so.${pkgver}"    -t "${pkgdir}/usr/lib32"
    install -D -m755 "libnvcuvid.so.${pkgver}" -t "${pkgdir}/usr/lib32"
    
    # PTX JIT Compiler (Parallel Thread Execution (PTX) is a pseudo-assembly language for CUDA)
    install -D -m755 "libnvidia-ptxjitcompiler.so.${pkgver}" -t "${pkgdir}/usr/lib32"
    
    # Optical flow
    install -D -m755 "libnvidia-opticalflow.so.${pkgver}" -t "${pkgdir}/usr/lib32"
    
    _create_links
    
    # license
    install -D -m644 "${srcdir}/${_pkg}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
