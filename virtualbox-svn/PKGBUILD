# $Id$
# Maintainer: Sébastien "Seblu" Luttringer
# Contributor: Ionut Biru <ibiru@archlinux.org>

pkgbase=virtualbox-svn
pkgname=('virtualbox-svn'
         'virtualbox-host-dkms-svn'
         'virtualbox-guest-dkms-svn'
         'virtualbox-sdk-svn'
         'virtualbox-guest-utils-svn'
         'virtualbox-guest-utils-nox-svn'
         'virtualbox-ext-vnc-svn')
pkgver=68769
pkgrel=2
arch=('i686' 'x86_64')
url='http://virtualbox.org'
license=('GPL' 'custom')
makedepends=('alsa-lib'
             'bin86'
             'cdrkit'
             'curl'
             'dev86'
             'device-mapper'
             'glu'
             'gsoap'
             'iasl'
             'jdk7-openjdk'
             'libidl2'
             'libpulse'
             'libstdc++5'
             'libvncserver'
             'libvpx'
             'libxcomposite'
             'libxcursor'
             'libxinerama'
             'libxml2'
             'libxmu'
             'libxrandr'
             'libxslt'
             'libxtst'
             'linux-headers'
             'mesa'
             'python2'
             'qt5-base'
             'qt5-x11extras'
             'qt5-tools'
             'sdl'
             'sdl_ttf'
             'vde2'
             'xalan-c'
             'xf86driproto'
             'xorg-server-devel'
             'subversion')
makedepends_x86_64=('gcc-multilib' 'lib32-glibc')
source=("VirtualBox::svn+http://www.virtualbox.org/svn/vbox/trunk"
        'virtualbox-host-dkms.conf'
        'virtualbox-guest-dkms.conf'
        'virtualbox.sysusers'
        'virtualbox-guest-utils.sysusers'
        '60-vboxdrv.rules'
        '60-vboxguest.rules'
        'LocalConfig.kmk'
        'vboxservice.service'
        'vboxservice-nox.service'
        'vboxweb.service'
        'vboxreload'
        '002-dri-driver-path.patch'
        '003-ogl-include-path.patch'
        '005-gsoap-build.patch'
        '006-rdesktop-vrdp-keymap-path.patch'
        '007-python2-path.patch'
        '008-no-vboxvideo.patch'
        '009-glibc-2.26.patch'
        )
sha256sums=('SKIP'
            '292fa3a414c125cf9119c8f2d866f3bd3a36c37842c9f68e6bbf74801860cd8a'
            'f4c4ec1b2d25c64d3b334d487d4fbf6e06e072d252a0979f73a47a41e4afdcf7'
            '2101ebb58233bbfadf3aa74381f22f7e7e508559d2b46387114bc2d8e308554c'
            'da4c49f6ca94e047e196cdbcba2c321199f4760056ea66e0fbc659353e128c9e'
            '9c5238183019f9ebc7d92a8582cad232f471eab9d3278786225abc1a1c7bf66e'
            '033c597e0f5285d2ddb0490868e5b6f945f45c7b1b1152a02a9e6fea438b2c95'
            '0105ce26b79dbe533085423decf042ac0f5e6aa28edb5e6a9bc713cca2ab04c5'
            '94a808f46909a51b2d0cf2c6e0a6c9dea792034943e6413bf9649a036c921b21'
            '01dbb921bd57a852919cc78be5b73580a564f28ebab2fe8d6c9b8301265cbfce'
            'e6e875ef186578b53106d7f6af48e426cdaf1b4e86834f01696b8ef1c685787f'
            '2a9d7748dc58f9d091f791da06b733a696943114f7c0d580fa00a0752eb1d2ac'
            'ee54fe188e27b6e80e2044ea9ba1874db2ca2c026ad04f393be1be69c18d440d'
            'a094a37ce710452e45f14eaec3e10bd71054aa910cf463b36a8b3ec42be466a1'
            '7d2da8fe10a90f76bbfc80ad1f55df4414f118cd10e10abfb76070326abebd46'
            '5d5af2de5b1f1c61ec793503350f2440661cf8fd640f11b8a86f10bce499c0dc'
            '6bdb017459532537199c399eefd3d84d8dc7f1786e79997caebd3b6eb5c75d9f'
            '8b7f241107863f82a5b0ae336aead0b3366a40103ff72dbebf33f54b512a0cbc'
            '3b6ad08a80f9f8c02c0c3625b7c96150056b466b8f32740b242a55736c282ec7')

pkgver() {
  cd "VirtualBox"
  local ver="$(svnversion)"
  printf "%s" "${ver//[[:alpha:]]}"
}

prepare() {
    cd "VirtualBox"

    # apply patch from the source array (should be a pacman feature)
    local filename
    for filename in "${source[@]}"; do
        if [[ "$filename" =~ \.patch$ ]]; then
            msg2 "Applying patch ${filename##*/}"
            patch -p1 -N -i "$srcdir/${filename##*/}"
        fi
    done

    msg2 'Applying local config'
    cp "$srcdir/LocalConfig.kmk" .

    msg2 'Use our CFLAGS'
    echo "VBOX_GCC_OPT=$CXXFLAGS" >> LocalConfig.kmk

    msg2 'Remove gcc version censorship'
    sed -i 's/^check_gcc$/#check_gcc/' configure
}

build() {
    cd "VirtualBox"

    msg2 'Build virtualbox'
    ./configure \
        --disable-docs \
        --enable-webservice \
        --enable-vde \
        --enable-vnc \
        --disable-kmods \
        --with-makeself=/usr/bin/echo
    # fake makeself binary to compile without nofatal
    # makeself is used by linux installer. we don't need it.
    source ./env.sh
    kmk

    msg2 'Build rdesktop-vrdp'
    kmk -C src/VBox/RDP/client-1.8.3

    msg2 'Build VNC extension pack'
    kmk -C src/VBox/ExtPacks/VNC packing
}

package_virtualbox-svn() {
    _pkgname=virtualbox
    pkgdesc='Powerful x86 virtualization for enterprise as well as home use'
    depends=('glibc' 'openssl' 'curl' 'gcc-libs' 'libpng' 'python2' 'sdl'
             'libvpx' 'libxml2' 'procps-ng' 'shared-mime-info' 'zlib'
             'libxcursor' 'libxinerama' 'libx11' 'libxext' 'libxmu' 'libxt'
             'qt5-base' 'qt5-x11extras' 'VIRTUALBOX-HOST-MODULES-SVN')
    optdepends=('vde2: Virtual Distributed Ethernet support'
                'virtualbox-guest-iso: Guest Additions CD image'
                'virtualbox-ext-vnc: VNC server support'
                'virtualbox-sdk: Developer kit')
    backup=('etc/vbox/vbox.cfg')
    replaces=('virtualbox-ose')
    conflicts=('virtualbox-ose' 'virtualbox')
    provides=('virtualbox')
    install=virtualbox.install

    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin"

    # binaries
    install -dm755 "$pkgdir/usr/bin"
    install -m755 VBox.sh "$pkgdir/usr/bin/VBox"
    for i in VBoxHeadless VBoxManage VBoxSDL VirtualBox vboxwebsrv VBoxBalloonCtrl; do
        ln -sf VBox "$pkgdir/usr/bin/$i"
        ln -sf VBox "$pkgdir/usr/bin/${i,,}"
    done
    install -m755 VBoxTunctl "$pkgdir/usr/bin"
    install -m755 rdesktop-vrdp "$pkgdir/usr/bin"

    # libraries
    install -dm755 "$pkgdir/usr/lib/virtualbox"
    install -m755 *.so "$pkgdir/usr/lib/virtualbox"
    install -m644 *.rc *.r0 VBoxEFI*.fd "$pkgdir/usr/lib/virtualbox"
    ## setuid root binaries
    install -m4755 VBoxSDL VirtualBox VBoxHeadless VBoxNetDHCP VBoxNetAdpCtl VBoxNetNAT -t "$pkgdir/usr/lib/virtualbox"
    ## other binaries
    install -m755 VBoxManage VBoxSVC VBoxExtPackHelperApp VBoxXPCOMIPCD VBoxTestOGL VBoxBalloonCtrl vboxwebsrv webtest -t "$pkgdir/usr/lib/virtualbox"

    # components
    install -dm755 "$pkgdir/usr/lib/virtualbox/components"
    install -m755 components/* -t "$pkgdir/usr/lib/virtualbox/components"

    # extensions packs
    ## as virtualbox install itself stuff in this directory, move it to /var and
    ## trick it with a symlink
    ## FIXME: trick is disabled for now
    #install -dm755 "$pkgdir/var/lib/virtualbox/extensions"
    #install -dm755 "$pkgdir/usr/share/virtualbox/extensions"
    #ln -s ../../../var/lib/virtualbox/extensions "$pkgdir/usr/lib/virtualbox/ExtensionPacks"
    install -dm755 "$pkgdir/usr/lib/virtualbox/ExtensionPacks"

    # languages
    install -dm755 "$pkgdir/usr/share/virtualbox/nls"
    install -m755 nls/*.qm -t "$pkgdir/usr/share/virtualbox/nls"

    # rdesktop keymaps
    install -dm755 "$pkgdir/usr/share/virtualbox/rdesktop-vrdp-keymaps"
    install -m644 rdesktop-vrdp-keymaps/* "$pkgdir/usr/share/virtualbox/rdesktop-vrdp-keymaps"

    # useless scripts
    install -m755 VBoxCreateUSBNode.sh VBoxSysInfo.sh -t "$pkgdir/usr/share/virtualbox"

    # icons
    install -Dm644 VBox.png "$pkgdir/usr/share/pixmaps/VBox.png"

    pushd icons >/dev/null
    for i in *; do
        install -d "$pkgdir/usr/share/icons/hicolor/$i/mimetypes"
        cp $i/* "$pkgdir/usr/share/icons/hicolor/$i/mimetypes"
    done
    popd >/dev/null

    #desktop
    install -Dm644 virtualbox.desktop "$pkgdir/usr/share/applications/virtualbox.desktop"
    install -Dm644 virtualbox.xml "$pkgdir/usr/share/mime/packages/virtualbox.xml"

    #install configuration
    install -dm755 "$pkgdir/etc/vbox"
    echo 'INSTALL_DIR=/usr/lib/virtualbox' > "$pkgdir/etc/vbox/vbox.cfg"

    # back to srcdir
    cd "$srcdir"

    #licence
    install -Dm644 VirtualBox/COPYING "$pkgdir/usr/share/licenses/$_pkgname/LICENSE"

    # install systemd stuff
    install -Dm644 60-vboxdrv.rules "$pkgdir/usr/lib/udev/rules.d/60-vboxdrv.rules"
    install -Dm644 vboxweb.service "$pkgdir/usr/lib/systemd/system/vboxweb.service"
    install -Dm644 virtualbox.sysusers "$pkgdir/usr/lib/sysusers.d/virtualbox.conf"

    # install module reloading shortcut (with a symlink with default helper)
    install -Dm755 vboxreload "$pkgdir/usr/bin"
    ln -s vboxreload "$pkgdir/usr/bin/rcvboxdrv"
}

package_virtualbox-sdk-svn() {
    _pkgname=virtualbox-sdk
    pkgdesc='VirtualBox Software Developer Kit (SDK)'
    depends=('python2')
    provides=('virtualbox-sdk')
    conflicts=('virtualbox-sdk')

    install -dm755 "$pkgdir/usr/lib/virtualbox"

    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin"

    install -Dm755 vboxshell.py "$pkgdir/usr/lib/virtualbox/vboxshell.py"
    # python sdk
    pushd sdk/installer
    VBOX_INSTALL_PATH="/usr/lib/virtualbox" python2 vboxapisetup.py install --root "$pkgdir"
    popd
    rm -rf sdk/installer
    cp -r sdk "$pkgdir/usr/lib/virtualbox"
    # licence
    install -Dm644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$_pkgname/LICENSE"
}

package_virtualbox-host-dkms-svn() {
    _pkgname=virtualbox-host-dkms
    pkgdesc='VirtualBox Host kernel modules sources'
    depends=('dkms' 'gcc' 'make')
    replaces=('virtualbox-source'
              'virtualbox-host-source'
              'virtualbox-host-modules-lts')
    conflicts=('virtualbox-source' 'virtualbox-host-source' 'virtualbox-host-dkms')
    provides=('VIRTUALBOX-HOST-MODULES-SVN' 'virtualbox-host-dkms')
    optdepends=('linux-headers: build modules against Arch kernel'
                'linux-lts-headers: build modules against LTS kernel'
                'linux-zen-headers: build modules against ZEN kernel')
    install=virtualbox-host-dkms.install

    install -dm755 "$pkgdir/usr/src"
    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin"
    cp -r src "$pkgdir/usr/src/vboxhost-svn_OSE"
    # licence
    install -Dm644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$_pkgname/LICENSE"
    # module loading
    local _p="$pkgdir/usr/lib/modules-load.d/$_pkgname.conf"
    install -Dm644 /dev/null "$_p"
    printf "vboxdrv\nvboxpci\nvboxnetadp\nvboxnetflt\n" > "$_p"
    # starting vbox 5.1, dkms.conf file was dropped
    local _p="$pkgdir/usr/src/vboxhost-svn_OSE/dkms.conf"
    install -Dm644 "$srcdir/$_pkgname.conf" "$_p"
    sed -i "s,@VERSION@,svn," "$_p"
}

package_virtualbox-guest-dkms-svn() {
    _pkgname=virtualbox-guest-dkms
    pkgdesc='VirtualBox Guest kernel modules sources'
    depends=('dkms' 'gcc' 'make')
    replaces=('virtualbox-archlinux-source'
              'virtualbox-guest-source'
              'virtualbox-guest-modules-lts')
    provides=('VIRTUALBOX-GUEST-MODULES-SVN' 'virtualbox-guest-dkms')
    conflicts=('virtualbox-archlinux-source' 'virtualbox-guest-source' 'virtualbox-guest-dkms')
    optdepends=('linux-headers: build modules against Arch kernel'
                'linux-lts-headers: build modules against LTS kernel'
                'linux-zen-headers: build modules against ZEN kernel')
    install=virtualbox-guest-dkms.install

    install -dm755 "$pkgdir/usr/src"
    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin/additions"
    cp -r src "$pkgdir/usr/src/vboxguest-svn_OSE"
    # licence
    install -Dm644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$_pkgname/LICENSE"
    # module loading
    local _p="$pkgdir/usr/lib/modules-load.d/$_pkgname.conf"
    install -Dm644 /dev/null "$_p"
    printf "vboxguest\nvboxsf\nvboxvideo\n" > "$_p"
    # starting vbox 5.1, dkms.conf file was dropped
    local _p="$pkgdir/usr/src/vboxguest-svn_OSE/dkms.conf"
    install -Dm644 "$srcdir/$_pkgname.conf" "$_p"
    sed -i "s,@VERSION@,svn," "$_p"
}

package_virtualbox-guest-utils-svn() {
    _pkgname=virtualbox-guest-utils
    pkgdesc='VirtualBox Guest userspace utilities'
    depends=('glibc' 'pam' 'libx11' 'libxcomposite'
             'libxdamage' 'libxext' 'libxfixes' 'libxmu' 'libxt' 'xorg-xrandr'
             'VIRTUALBOX-GUEST-MODULES-SVN')
    replaces=('virtualbox-archlinux-additions' 'virtualbox-guest-additions')
    conflicts=('virtualbox-archlinux-additions' 'virtualbox-guest-additions' 'virtualbox-guest-utils-nox' 'virtualbox-guest-utils')
    provides=('virtualbox-guest-utils')

    source "VirtualBox/env.sh"
    pushd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin/additions"
    install -d "$pkgdir/usr/bin"
    install -m755 VBoxClient VBoxControl VBoxService mount.vboxsf "$pkgdir/usr/bin"
    install -m755 -D "$srcdir"/VirtualBox/src/VBox/Additions/x11/Installer/98vboxadd-xclient \
        "$pkgdir"/usr/bin/VBoxClient-all
    install -m644 -D "$srcdir"/VirtualBox/src/VBox/Additions/x11/Installer/vboxclient.desktop \
        "$pkgdir"/etc/xdg/autostart/vboxclient.desktop
    install -d "$pkgdir/usr/lib/xorg/modules/dri"
    install -m755 VBoxOGL*.so "$pkgdir/usr/lib"
    ln -s /usr/lib/VBoxOGL.so "$pkgdir/usr/lib/xorg/modules/dri/vboxvideo_dri.so"
    install -m755 -D pam_vbox.so "$pkgdir/usr/lib/security/pam_vbox.so"
    popd
    # systemd stuff
    install -Dm644 60-vboxguest.rules "$pkgdir/usr/lib/udev/rules.d/60-vboxguest.rules"
    install -Dm644 vboxservice.service "$pkgdir/usr/lib/systemd/system/vboxservice.service"
    install -Dm644 virtualbox-guest-utils.sysusers "$pkgdir/usr/lib/sysusers.d/virtualbox-guest-utils.conf"
    # licence
    install -Dm644 VirtualBox/COPYING "$pkgdir/usr/share/licenses/$_pkgname/LICENSE"
}

package_virtualbox-guest-utils-nox-svn() {
    _pkgname=virtualbox-guest-utils-nox
    pkgdesc='VirtualBox Guest userspace utilities without X support'
    depends=('glibc' 'pam' 'VIRTUALBOX-GUEST-MODULES-SVN')
    provides=('virtualbox-guest-utils-nox')
    conflicts=('virtualbox-guest-utils' 'virtualbox-guest-utils-nox')

    source "VirtualBox/env.sh"
    pushd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin/additions"
    install -d "$pkgdir/usr/bin"
    install -m755 VBoxControl VBoxService mount.vboxsf "$pkgdir/usr/bin"
    install -m755 -D pam_vbox.so "$pkgdir/usr/lib/security/pam_vbox.so"
    popd
    # systemd stuff
    install -Dm644 60-vboxguest.rules "$pkgdir/usr/lib/udev/rules.d/60-vboxguest.rules"
    install -Dm644 vboxservice-nox.service "$pkgdir/usr/lib/systemd/system/vboxservice.service"
    install -Dm644 virtualbox-guest-utils.sysusers "$pkgdir/usr/lib/sysusers.d/virtualbox-guest-utils.conf"
    # licence
    install -Dm644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$_pkgname/LICENSE"
}

package_virtualbox-ext-vnc-svn() {
    _pkgname=virtualbox-ext-vnc
    pkgdesc='VirtualBox VNC extension pack'
    depends=('virtualbox' 'libvncserver')
    optdepends=('tigervnc: vnc client')
    provides=('virtualbox-ext-vnc')
    conflicts=('virtualbox-ext-vnc')
    install=virtualbox-ext-vnc.install

    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/packages"
    install -Dm644 VNC-*.vbox-extpack "$pkgdir/usr/share/virtualbox/extensions/VNC-svn.vbox-extpack"
    # licence
    install -Dm644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$_pkgname/LICENSE"
}

# vim:set ts=4 sw=4 et:
