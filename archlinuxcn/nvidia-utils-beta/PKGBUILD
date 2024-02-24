# Maintainer : Daniel Bermond <dbermond@archlinux.org>
# Contributor: Det <nimetonmaili g-mail>
# Contributor: Ng Oon-Ee
# Contributor: Dan Vratil

pkgbase=nvidia-utils-beta
pkgname=('nvidia-utils-beta' 'opencl-nvidia-beta' 'nvidia-settings-beta')
pkgver=550.54.14
pkgrel=1
pkgdesc='NVIDIA drivers utilities (beta version)'
arch=('x86_64')
url='https://www.nvidia.com/'
license=('custom')
options=('!strip')
_pkg="NVIDIA-Linux-${CARCH}-${pkgver}"
source=("https://us.download.nvidia.com/XFree86/Linux-${CARCH}/${pkgver}/${_pkg}.run"
        'nvidia-drm-outputclass.conf'
        'nvidia-utils.sysusers'
        'nvidia.rules'
        '120-nvidia-settings-change-desktop-paths.patch')
sha256sums=('8c497ff1cfc7c310fb875149bc30faa4fd26d2237b2cba6cd2e8b0780157cfe3'
            'be99ff3def641bb900c2486cce96530394c5dc60548fc4642f19d3a4c784134d'
            'd8d1caa5d72c71c6430c2a0d9ce1a674787e9272ccce28b9d5898ca24e60a167'
            '0fe174c53c1ed4618c6a611481aac6b314946478669c1fe426a0b8fd0f3d22ff'
            '6f0f4a23706241e9e37e0fe30a09bd30ca29bb446d8fe7861cb4959f0a010ef4')

# create soname links
_create_links() {
    local _lib
    local _soname
    local _base
    find "$pkgdir" -type f -name '*.so*' ! -path '*xorg/*' -print0 | while read -d $'\0' _lib
    do
        _soname="$(dirname "$_lib")/$(readelf -d "$_lib" | grep -Po 'SONAME.*: \[\K[^]]*' || true)"
        _base="$(printf '%s' "$_soname" | sed -r 's/(.*)\.so.*/\1.so/')"
        [ -e "$_soname" ] || ln -s "$(basename "$_lib")"    "$_soname"
        [ -e "$_base"   ] || ln -s "$(basename "$_soname")" "$_base"
    done
}

prepare() {
    # extract the source file
    [ -d "$_pkg" ] && rm -rf "$_pkg"
    printf '%s\n' "  -> Self-Extracting ${_pkg}.run..."
    sh "${_pkg}.run" --extract-only
    bsdtar -C "$_pkg" -xf "${_pkg}/nvidia-persistenced-init.tar.bz2"
    gunzip "$_pkg"/nvidia-{cuda-mps-control,modprobe,persistenced,settings,smi,xconfig}.1.gz
    
    patch -d "$_pkg" -Np1 -i "${srcdir}/120-nvidia-settings-change-desktop-paths.patch"
}

package_nvidia-settings-beta() {
    pkgdesc='Tool for configuring the NVIDIA graphics driver (beta version)'
    depends=("nvidia-utils-beta>=${pkgver}" 'gtk3')
    provides=("nvidia-settings=${pkgver}" "nvidia-settings-beta=${pkgver}")
    conflicts=('nvidia-settings')
    
    cd "$_pkg"
    
    install -D -m755 nvidia-settings         -t "${pkgdir}/usr/bin"
    install -D -m644 nvidia-settings.1       -t "${pkgdir}/usr/share/man/man1"
    install -D -m644 nvidia-settings.png     -t "${pkgdir}/usr/share/icons/hicolor/128x128/apps"
    install -D -m644 nvidia-settings.desktop -t "${pkgdir}/usr/share/applications"
    install -D -m755 "libnvidia-gtk3.so.${pkgver}" -t "${pkgdir}/usr/lib"
    install -D -m755 "libnvidia-wayland-client.so.${pkgver}" -t "${pkgdir}/usr/lib"
    
    # license
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_opencl-nvidia-beta() {
    pkgdesc='OpenCL implemention for NVIDIA (beta version)'
    depends=('zlib' "nvidia-utils-beta>=${pkgver}")
    optdepends=('opencl-headers: headers necessary for OpenCL development')
    provides=("opencl-nvidia=${pkgver}" 'opencl-driver')
    conflicts=('opencl-nvidia')
    
    cd "$_pkg"
    
    # OpenCL
    install -D -m644 nvidia.icd "${pkgdir}/etc/OpenCL/vendors/nvidia.icd"
    install -D -m755 "libnvidia-opencl.so.${pkgver}" -t "${pkgdir}/usr/lib"
    
    _create_links

    # license
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_nvidia-utils-beta() {
    depends=('xorg-server' 'libglvnd' 'egl-wayland')
    optdepends=('nvidia-settings-beta: for the configuration tool'
                'xorg-server-devel: for nvidia-xconfig'
                'opencl-nvidia-beta: for OpenCL support')
    provides=("nvidia-utils=${pkgver}" 'vulkan-driver' 'opengl-driver' "nvidia-libgl=${pkgver}"
              "nvidia-libgl-beta=${pkgver}")
    conflicts=('nvidia-utils' 'nvidia-libgl')
    replaces=('nvidia-libgl')
    install=nvidia-utils.install
    
    cd "$_pkg"
    
    # X driver
    install -D -m755 nvidia_drv.so -t "${pkgdir}/usr/lib/xorg/modules/drivers"
    
    # firmware
    install -D -m644 firmware/*.bin -t "${pkgdir}/usr/lib/firmware/nvidia/${pkgver}"
    
    # GLX extension module for X
    install -D -m755 "libglxserver_nvidia.so.${pkgver}" -t "${pkgdir}/usr/lib/nvidia/xorg"
    # Ensure that X finds glx
    ln -s "libglxserver_nvidia.so.${pkgver}" "${pkgdir}/usr/lib/nvidia/xorg/libglxserver_nvidia.so.1"
    ln -s "libglxserver_nvidia.so.${pkgver}" "${pkgdir}/usr/lib/nvidia/xorg/libglxserver_nvidia.so"
    
    install -D -m755 "libGLX_nvidia.so.${pkgver}" -t "${pkgdir}/usr/lib"
    
    # OpenGL libraries
    install -D -m755 "libEGL_nvidia.so.${pkgver}"       -t "${pkgdir}/usr/lib"
    install -D -m755 "libGLESv1_CM_nvidia.so.${pkgver}" -t "${pkgdir}/usr/lib"
    install -D -m755 "libGLESv2_nvidia.so.${pkgver}"    -t "${pkgdir}/usr/lib"
    install -D -m644 10_nvidia.json                     -t "${pkgdir}/usr/share/glvnd/egl_vendor.d"
    
    # OpenGL core library
    install -D -m755 "libnvidia-glcore.so.${pkgver}"  -t "${pkgdir}/usr/lib"
    install -D -m755 "libnvidia-eglcore.so.${pkgver}" -t "${pkgdir}/usr/lib"
    install -D -m755 "libnvidia-glsi.so.${pkgver}"    -t "${pkgdir}/usr/lib"
    
    # misc
    install -D -m755  libnvidia-api.so.1                -t "${pkgdir}/usr/lib"
    install -D -m755 "libnvidia-fbc.so.${pkgver}"       -t "${pkgdir}/usr/lib"
    install -D -m755 "libnvidia-encode.so.${pkgver}"    -t "${pkgdir}/usr/lib"
    install -D -m755 "libnvidia-cfg.so.${pkgver}"       -t "${pkgdir}/usr/lib"
    install -D -m755 "libnvidia-ml.so.${pkgver}"        -t "${pkgdir}/usr/lib"
    install -D -m755 "libnvidia-glvkspirv.so.${pkgver}" -t "${pkgdir}/usr/lib"
    install -D -m755 "libnvidia-gpucomp.so.${pkgver}"   -t "${pkgdir}/usr/lib"
    
    # Vulkan ICD
    install -D -m644 nvidia_icd.json    -t "${pkgdir}/usr/share/vulkan/icd.d"
    install -D -m644 nvidia_layers.json -t "${pkgdir}/usr/share/vulkan/implicit_layer.d"
    
    # VDPAU
    install -D -m755 "libvdpau_nvidia.so.${pkgver}" -t "${pkgdir}/usr/lib/vdpau"
    
    # nvidia-tls library
    install -D -m755 "libnvidia-tls.so.${pkgver}" -t "${pkgdir}/usr/lib"
    
    # CUDA
    install -D -m755 "libcuda.so.${pkgver}"    -t "${pkgdir}/usr/lib"
    install -D -m755 "libnvcuvid.so.${pkgver}" -t "${pkgdir}/usr/lib"
    
    # PTX JIT Compiler (Parallel Thread Execution (PTX) is a pseudo-assembly language for CUDA)
    install -D -m755 "libnvidia-ptxjitcompiler.so.${pkgver}" -t "${pkgdir}/usr/lib"
    
    # NVVM Compiler (JIT link-time-optimization for CUDA)
    install -D -m755 "libnvidia-nvvm.so.${pkgver}" -t "${pkgdir}/usr/lib"
    
    # raytracing
    install -D -m755 "libnvoptix.so.${pkgver}"       -t "${pkgdir}/usr/lib"
    install -D -m755 "libnvidia-rtcore.so.${pkgver}" -t "${pkgdir}/usr/lib"
    install -D -m755 "nvoptix.bin"                   -t "${pkgdir}/usr/share/nvidia/nvoptix.bin"
    
    # Optical flow
    install -D -m755 "libnvidia-opticalflow.so.${pkgver}" -t "${pkgdir}/usr/lib"
    
    # NGX
    install -D -m755 "libnvidia-ngx.so.${pkgver}" -t "${pkgdir}/usr/lib"
    
    # DLSS
    install -D -m755 nvidia-ngx-updater -t "${pkgdir}/usr/bin"
    install -D -m644 {,_}nvngx.dll -t "${pkgdir}/usr/lib/nvidia/wine"
    
    # Wayland/GBM
    install -D -m755 "libnvidia-allocator.so.${pkgver}" -t "${pkgdir}/usr/lib"
    install -D -m755 libnvidia-egl-gbm.so.1.1.1         -t "${pkgdir}/usr/lib"
    install -D -m644 15_nvidia_gbm.json -t "${pkgdir}/usr/share/egl/egl_external_platform.d"
    install -d -m755 "${pkgdir}/usr/lib/gbm"
    ln -s "../libnvidia-allocator.so.${pkgver}" "${pkgdir}/usr/lib/gbm/nvidia-drm_gbm.so"
    
    # Debug
    install -D -m755 nvidia-debugdump -t "${pkgdir}/usr/bin"
    
    # nvidia-xconfig
    install -D -m755 nvidia-xconfig   -t "${pkgdir}/usr/bin"
    install -D -m644 nvidia-xconfig.1 -t "${pkgdir}/usr/share/man/man1"
    
    # nvidia-bug-report
    install -D -m755 nvidia-bug-report.sh -t "${pkgdir}/usr/bin"
    
    # nvidia-smi
    install -D -m755 nvidia-smi   -t "${pkgdir}/usr/bin"
    install -D -m644 nvidia-smi.1 -t "${pkgdir}/usr/share/man/man1"
    
    # nvidia-cuda-mps
    install -D -m755 nvidia-cuda-mps-server    -t "${pkgdir}/usr/bin"
    install -D -m755 nvidia-cuda-mps-control   -t "${pkgdir}/usr/bin"
    install -D -m644 nvidia-cuda-mps-control.1 -t "${pkgdir}/usr/share/man/man1"
    
    # nvidia-modprobe
    # This should be removed if nvidia fixed their uvm module!
    install -D -m4755 nvidia-modprobe  -t "${pkgdir}/usr/bin"
    install -D -m644 nvidia-modprobe.1 -t "${pkgdir}/usr/share/man/man1"
    
    # nvidia-persistenced
    install -D -m755 nvidia-persistenced   -t "${pkgdir}/usr/bin"
    install -D -m644 nvidia-persistenced.1 -t "${pkgdir}/usr/share/man/man1"
    install -D -m644 nvidia-persistenced-init/systemd/nvidia-persistenced.service.template "${pkgdir}/usr/lib/systemd/system/nvidia-persistenced.service"
    sed -i 's/__USER__/nvidia-persistenced/' "${pkgdir}/usr/lib/systemd/system/nvidia-persistenced.service"
    
    # application profiles
    install -D -m644 "nvidia-application-profiles-${pkgver}-rc"                -t "${pkgdir}/usr/share/nvidia"
    install -D -m644 "nvidia-application-profiles-${pkgver}-key-documentation" -t "${pkgdir}/usr/share/nvidia"
    
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.txt "${pkgdir}/usr/share/doc/${pkgname}/README"
    install -D -m644 NVIDIA_Changelog -t "${pkgdir}/usr/share/doc/${pkgname}"
    install -D -m644 supported-gpus/supported-gpus.json -t "${pkgdir}/usr/share/doc/${pkgname}"
    cp -dr --no-preserve='ownership' html "${pkgdir}/usr/share/doc/${pkgname}/"
    #ln -s nvidia "${pkgdir}/usr/share/doc/nvidia-utils"
    
    # new power management support
    install -D -m644 systemd/system/*.service -t "${pkgdir}/usr/lib/systemd/system"
    install -D -m755 systemd/system-sleep/nvidia -t "${pkgdir}/usr/lib/systemd/system-sleep"
    install -D -m755 systemd/nvidia-sleep.sh -t "${pkgdir}/usr/bin"
    
    # dynamic boost power management
    install -D -m755 nvidia-powerd -t "${pkgdir}/usr/bin"
    install -D -m644 nvidia-dbus.conf -t "${pkgdir}/usr/share/dbus-1/system.d"
    
    # distro specific files must be installed in /usr/share/X11/xorg.conf.d
    install -D -m644 "${srcdir}/nvidia-drm-outputclass.conf" "${pkgdir}/usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf"
    
    install -D -m644 "${srcdir}/nvidia-utils.sysusers" "${pkgdir}/usr/lib/sysusers.d/${pkgname}.conf"
    install -D -m644 "${srcdir}/nvidia.rules" "${pkgdir}/usr/lib/udev/rules.d/60-nvidia.rules"
    
    install -D -m644 <(printf '%s\n' 'blacklist nouveau') "${pkgdir}/usr/lib/modprobe.d/${pkgname}.conf"
    install -D -m644 <(printf '%s\n' 'nvidia-uvm') "${pkgdir}/usr/lib/modules-load.d/${pkgname}.conf"
    
    _create_links
}
