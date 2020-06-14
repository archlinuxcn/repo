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
pkgver=84727
pkgrel=2
_vboxsf_commit='5aba938bcabd978e4615186ad7d8617d633e6f30'
arch=('x86_64')
url='http://virtualbox.org'
license=('GPL' 'custom')
makedepends=('subversion'
             'alsa-lib'
             'bin86'
             'cdrkit'
             'curl'
             'dev86'
             'device-mapper'
             'git'
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
             'opus'
             'python'
             'qt5-base'
             'qt5-x11extras'
             'qt5-tools'
             'sdl'
             'sdl_ttf'
             'vde2'
             'xalan-c'
             'xorgproto'
             'xorg-server-devel')
source=("VirtualBox::svn+http://www.virtualbox.org/svn/vbox/trunk"
        # We need to build a modified version of vboxsf for Linux 4.16
        # https://bugzilla.redhat.com/show_bug.cgi?id=1481630#c65
        "git+https://github.com/jwrdegoede/vboxsf#commit=$_vboxsf_commit"
        'virtualbox-host-dkms.conf'
        'virtualbox-vboxsf-dkms.conf'
        'virtualbox.sysusers'
        'virtualbox-guest-utils.sysusers'
        '60-vboxdrv.rules'
        '60-vboxguest.rules'
        'LocalConfig.kmk'
        'vboxservice.service'
        'vboxservice-nox.service'
        'vboxweb.service'
        'vboxreload'
        '001-disable-update.patch'
        '005-gsoap-build.patch'
        '006-rdesktop-vrdp-keymap-path.patch'
        '008-no-vboxvideo.patch'
        '012-vbglR3GuestCtrlDetectPeekGetCancelSupport.patch'
        '013-Makefile.patch'
        '016-VBoxServiceAutoMount-Change-Linux-mount-code-to-use-.patch'
        '017-fix-narrowing-conversion.patch'
        '018-work-around-black-screen.patch'
        '019-qt-5-15.patch'
        '020-gsoap.patch')
sha256sums=('SKIP'
            'SKIP'
            '76d98ea062fcad9e5e3fa981d046a6eb12a3e718a296544a68b66f4b65cb56db'
            'c1ccfaa3a37d6b227cd65de944df2d68cbf178a857b6ab15c04b8fa05693f252'
            '2101ebb58233bbfadf3aa74381f22f7e7e508559d2b46387114bc2d8e308554c'
            'da4c49f6ca94e047e196cdbcba2c321199f4760056ea66e0fbc659353e128c9e'
            '9c5238183019f9ebc7d92a8582cad232f471eab9d3278786225abc1a1c7bf66e'
            '033c597e0f5285d2ddb0490868e5b6f945f45c7b1b1152a02a9e6fea438b2c95'
            '2be313b98bffde482aad93b00c419f1d5f7645fd9e6053175ffb0d925067f96a'
            '94a808f46909a51b2d0cf2c6e0a6c9dea792034943e6413bf9649a036c921b21'
            '01dbb921bd57a852919cc78be5b73580a564f28ebab2fe8d6c9b8301265cbfce'
            'e6e875ef186578b53106d7f6af48e426cdaf1b4e86834f01696b8ef1c685787f'
            '4001b5927348fe669a541e80526d4f9ea91b883805f102f7d571edbb482a9b9d'
            '9ee947c9b5ec5b25f52d3e72340fc3a57ca6e65a604e15b669ac582a3fb0dc1b'
            '7d2da8fe10a90f76bbfc80ad1f55df4414f118cd10e10abfb76070326abebd46'
            '13c6ca9be0f91582445fd2a14a8c58a0625a15d9cb98cb6e8c2736d77ea976ab'
            '053bfeee8863f3ffdf2f0e3f9f0d77dc61dd32764700a97a7635fd8611e20491'
            '81900e13d36630488accd8c0bfd2ceb69563fb2c4f0f171caba1cca59d438024'
            'da7e58ed37dc23c6202aab3017864579a99e78417f3421ddcc98a198198fe2c9'
            '100c9e14e9cfb12ae65364e830153d2481cf272ceeb39d11c6b203bc6e35bf0c'
            '5aac692909a0a0ec56b08bdece9e42cf7463abdca9da2f990d441ff463be6a99'
            'c64a4f284a4e91a42df5b30939d9190127ea5aa25470b5d31507a8309c20e1fc'
            '24d73181ad544233a5e9365c911940a162f7bb0ed7ffde592f91f59ec555dcce'
            'c6892a3561a72a9b308cb33fa6647cc53e54a3bd40cb41780cad7f8e9d7df9f6')

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
            echo "Applying patch ${filename##*/}"
            patch -p1 -N -i "$srcdir/${filename##*/}"
        fi
    done
    
    sed -i '#include<QPainter>/a #include<QPainterPath>' src/VBox/Frontends/VirtualBox/src/monitor/UIMonitorCommon.cpp
    echo 'Applying local config'
    cp "$srcdir/LocalConfig.kmk" .
    
    echo 'Use our CFLAGS'
    echo "VBOX_GCC_OPT=$CXXFLAGS" >> LocalConfig.kmk
}

build() {
    cd "VirtualBox"

    echo 'Build virtualbox'
    ./configure \
        --disable-docs \
        --disable-kmods \
        --disable-vmmraw \
        --enable-vde \
        --enable-vnc \
        --enable-webservice \
        --with-makeself=/usr/bin/echo
    # fake makeself binary to compile without nofatal
    # makeself is used by linux installer. we don't need it.
    source ./env.sh
    kmk

    echo 'Build rdesktop-vrdp'
    kmk -C src/VBox/RDP/client-1.8.4

    echo 'Build VNC extension pack'
    kmk -C src/VBox/ExtPacks/VNC packing

    echo 'Build vboximg-mount'
    kmk -C src/VBox/ImageMounter/vboximg-mount
}

package_virtualbox-svn() {
    pkgdesc='Powerful x86 virtualization for enterprise as well as home use'
    depends=('glibc' 'openssl' 'curl' 'gcc-libs' 'libpng' 'python' 'sdl'
             'libvpx' 'libxml2' 'procps-ng' 'shared-mime-info' 'zlib'
             'libxcursor' 'libxinerama' 'libx11' 'libxext' 'libxmu' 'libxt'
             'opus' 'desktop-file-utils' 'hicolor-icon-theme' 'qt5-base' 'qt5-x11extras' 'VIRTUALBOX-HOST-MODULES-SVN')
    optdepends=('vde2: Virtual Distributed Ethernet support'
                'virtualbox-guest-iso: Guest Additions CD image'
                'virtualbox-ext-vnc: VNC server support'
                'virtualbox-sdk: Developer kit')
    backup=('etc/vbox/vbox.cfg')
    provides=('virtualbox')
    replaces=('virtualbox-ose')
    conflicts=('virtualbox-ose' 'virtualbox')
    install=virtualbox.install

    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin"

    # binaries
    install -dm0755 "$pkgdir/usr/bin"
    install -m0755 VBox.sh "$pkgdir/usr/bin/VBox"
    for i in VBoxHeadless VBoxManage VBoxSDL VirtualBox vboxwebsrv VBoxBalloonCtrl; do
        ln -sf VBox "$pkgdir/usr/bin/$i"
        ln -sf VBox "$pkgdir/usr/bin/${i,,}"
    done
    install -m0755 VBoxTunctl "$pkgdir/usr/bin"
    install -m0755 rdesktop-vrdp "$pkgdir/usr/bin"
    install -m0755 vboximg-mount "$pkgdir/usr/bin"

    # libraries
    install -dm0755 "$pkgdir/usr/lib/virtualbox"
    install -m0755 *.so "$pkgdir/usr/lib/virtualbox"
    install -m0644 *.r0 VBoxEFI*.fd "$pkgdir/usr/lib/virtualbox"
    ## setuid root binaries
    install -m4755 VBoxSDL VirtualBoxVM VBoxHeadless VBoxNetDHCP VBoxNetAdpCtl VBoxNetNAT -t "$pkgdir/usr/lib/virtualbox"
    ## other binaries
    install -m0755 VirtualBox VBoxManage VBoxSVC VBoxExtPackHelperApp VBoxXPCOMIPCD VBoxTestOGL VBoxBalloonCtrl vboxwebsrv webtest -t "$pkgdir/usr/lib/virtualbox"

    # components
    install -dm0755 "$pkgdir/usr/lib/virtualbox/components"
    #rm components/VBoxREM.so # TODO: remove when dead link is fixed
    install -m0755 components/* -t "$pkgdir/usr/lib/virtualbox/components"

    # extensions packs
    ## as virtualbox install itself stuff in this directory, move it to /var and
    ## trick it with a symlink
    ## FIXME: trick is disabled for now
    #install -dm0755 "$pkgdir/var/lib/virtualbox/extensions"
    #install -dm0755 "$pkgdir/usr/share/virtualbox/extensions"
    #ln -s ../../../var/lib/virtualbox/extensions "$pkgdir/usr/lib/virtualbox/ExtensionPacks"
    install -dm0755 "$pkgdir/usr/lib/virtualbox/ExtensionPacks"

    # languages
    install -dm0755 "$pkgdir/usr/share/virtualbox/nls"
    install -m0755 nls/*.qm -t "$pkgdir/usr/share/virtualbox/nls"

    # rdesktop keymaps
    install -dm0755 "$pkgdir/usr/share/virtualbox/rdesktop-vrdp-keymaps"
    install -m0644 rdesktop-vrdp-keymaps/* "$pkgdir/usr/share/virtualbox/rdesktop-vrdp-keymaps"

    # useless scripts
    install -m0755 VBoxCreateUSBNode.sh VBoxSysInfo.sh -t "$pkgdir/usr/share/virtualbox"

    # icons
    install -Dm0644 VBox.png "$pkgdir/usr/share/pixmaps/VBox.png"

    pushd icons >/dev/null
    for i in *; do
        install -d "$pkgdir/usr/share/icons/hicolor/$i/mimetypes"
        cp $i/* "$pkgdir/usr/share/icons/hicolor/$i/mimetypes"
    done
    popd >/dev/null

    #desktop
    install -Dm0644 virtualbox.desktop "$pkgdir/usr/share/applications/virtualbox.desktop"
    install -Dm0644 virtualbox.xml "$pkgdir/usr/share/mime/packages/virtualbox.xml"

    #install configuration
    install -dm0755 "$pkgdir/etc/vbox"
    echo 'INSTALL_DIR=/usr/lib/virtualbox' > "$pkgdir/etc/vbox/vbox.cfg"

    # back to srcdir
    cd "$srcdir"

    #licence
    install -Dm0644 VirtualBox/COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

    # install systemd stuff
    install -Dm0644 60-vboxdrv.rules "$pkgdir/usr/lib/udev/rules.d/60-vboxdrv.rules"
    install -Dm0644 vboxweb.service "$pkgdir/usr/lib/systemd/system/vboxweb.service"
    install -Dm0644 virtualbox.sysusers "$pkgdir/usr/lib/sysusers.d/virtualbox.conf"

    # install module reloading shortcut (with a symlink with default helper)
    install -Dm0755 vboxreload "$pkgdir/usr/bin"
    ln -s vboxreload "$pkgdir/usr/bin/rcvboxdrv"
}

package_virtualbox-sdk-svn() {
    pkgdesc='VirtualBox Software Developer Kit (SDK)'
    depends=('python')
    provides=('virtualbox-sdk')
    conflicts=('virtualbox-sdk')

    install -dm0755 "$pkgdir/usr/lib/virtualbox"

    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin"

    install -Dm0755 vboxshell.py "$pkgdir/usr/lib/virtualbox/vboxshell.py"
    # python sdk
    pushd sdk/installer
    VBOX_INSTALL_PATH="/usr/lib/virtualbox" python vboxapisetup.py install --root "$pkgdir"
    popd
    cp -r sdk "$pkgdir/usr/lib/virtualbox"
    rm -r "$pkgdir/usr/lib/virtualbox/sdk/installer"
    # licence
    install -Dm0644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_virtualbox-host-dkms-svn() {
    pkgdesc='VirtualBox Host kernel modules sources'
    depends=('dkms' 'gcc' 'make')
    replaces=('virtualbox-source'
              'virtualbox-host-source'
              'virtualbox-host-modules-lts')
    conflicts=('virtualbox-source' 'virtualbox-host-source' 'virtualbox-host-dkms')
    provides=('VIRTUALBOX-HOST-MODULES-SVN')
    optdepends=('linux-headers: build modules against Arch kernel'
                'linux-lts-headers: build modules against LTS kernel'
                'linux-zen-headers: build modules against ZEN kernel')
    install=virtualbox-host-dkms.install

    install -dm0755 "$pkgdir/usr/src"
    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin"
    cp -r src "$pkgdir/usr/src/vboxhost-svn_OSE"
    # licence
    install -Dm0644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    # module loading
    local _p="$pkgdir/usr/lib/modules-load.d/virtualbox-host-dkms.conf"
    install -Dm0644 /dev/null "$_p"
    printf "vboxdrv\nvboxnetadp\nvboxnetflt\n" > "$_p"
    # starting vbox 5.1, dkms.conf file was dropped
    local _p="$pkgdir/usr/src/vboxhost-svn_OSE/dkms.conf"
    install -Dm0644 "$srcdir/virtualbox-host-dkms.conf" "$_p"
    sed -i "s,@VERSION@,svn," "$_p"
}

package_virtualbox-guest-dkms-svn() {
    pkgdesc='VirtualBox Guest kernel modules sources'
    depends=('dkms' 'gcc' 'make')
    replaces=('virtualbox-archlinux-source'
              'virtualbox-guest-source'
              'virtualbox-guest-modules-lts')
    provides=('VIRTUALBOX-GUEST-MODULES-SVN')
    conflicts=('virtualbox-archlinux-source' 'virtualbox-guest-source' 'virtualbox-guest-dkms')
    optdepends=('linux-headers: build modules against Arch kernel'
                'linux-lts-headers: build modules against LTS kernel'
                'linux-zen-headers: build modules against ZEN kernel')
    install=virtualbox-guest-dkms.install

    install -dm0755 "$pkgdir/usr/src"
    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin/additions"
    cp -r src "$pkgdir/usr/src/vboxguest-svn_OSE"
    # licence
    install -Dm0644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    # module loading
    local _p="$pkgdir/usr/lib/modules-load.d/virtualbox-guest-dkms.conf"
    install -Dm0644 /dev/null "$_p"
    printf "vboxguest\nvboxsf\nvboxvideo\n" > "$_p"

    # vboxsf module for Linux 4.16 to Linux 5.5
    install -d "$pkgdir/usr/src/vboxsf-svn_OSE"
    cp -rT "$srcdir/vboxsf" "$pkgdir/usr/src/vboxsf-svn_OSE/vboxsf"
    rm -rf "$pkgdir/usr/src/vboxsf-svn_OSE/vboxsf/.git"
    echo "obj-m = vboxsf/" >"$pkgdir/usr/src/vboxsf-svn_OSE/Makefile"
    local _p="$pkgdir/usr/src/vboxsf-svn_OSE/dkms.conf"
    install -Dm0644 "$srcdir/virtualbox-vboxsf-dkms.conf" "$_p"
    sed -i "s,@VERSION@,svn," "$_p"
}

package_virtualbox-guest-utils-svn() {
    pkgdesc='VirtualBox Guest userspace utilities'
    depends=('glibc' 'pam' 'libx11' 'libxcomposite'
             'libxdamage' 'libxext' 'libxfixes' 'libxmu' 'libxt' 'xorg-xrandr'
             'VIRTUALBOX-GUEST-MODULES-SVN')
    replaces=('virtualbox-archlinux-additions' 'virtualbox-guest-additions')
    provides=('virtualbox-guest-utils')
    conflicts=('virtualbox-archlinux-additions' 'virtualbox-guest-additions' 'virtualbox-guest-utils-nox' 'virtualbox-guest-utils')

    source "VirtualBox/env.sh"
    pushd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin/additions"
    install -d "$pkgdir/usr/bin"
    install -m0755 VBoxClient VBoxControl VBoxService "$pkgdir/usr/bin"
    install -m0755 -D "$srcdir"/VirtualBox/src/VBox/Additions/x11/Installer/98vboxadd-xclient \
        "$pkgdir"/usr/bin/VBoxClient-all
    install -m0644 -D "$srcdir"/VirtualBox/src/VBox/Additions/x11/Installer/vboxclient.desktop \
        "$pkgdir"/etc/xdg/autostart/vboxclient.desktop
    install -d "$pkgdir/usr/lib/xorg/modules/dri"
    install -m0755 -D pam_vbox.so "$pkgdir/usr/lib/security/pam_vbox.so"
    popd
    # systemd stuff
    install -Dm0644 60-vboxguest.rules "$pkgdir/usr/lib/udev/rules.d/60-vboxguest.rules"
    install -Dm0644 vboxservice.service "$pkgdir/usr/lib/systemd/system/vboxservice.service"
    install -Dm0644 virtualbox-guest-utils.sysusers "$pkgdir/usr/lib/sysusers.d/virtualbox-guest-utils.conf"
    # licence
    install -Dm0644 VirtualBox/COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_virtualbox-guest-utils-nox-svn() {
    pkgdesc='VirtualBox Guest userspace utilities without X support'
    depends=('glibc' 'pam' 'VIRTUALBOX-GUEST-MODULES-SVN')
    provides=('virtualbox-guest-utils-nox')
    conflicts=('virtualbox-guest-utils' 'virtualbox-guest-utils-nox')

    source "VirtualBox/env.sh"
    pushd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin/additions"
    install -d "$pkgdir/usr/bin"
    install -m0755 VBoxControl VBoxService "$pkgdir/usr/bin"
    install -m0755 -D pam_vbox.so "$pkgdir/usr/lib/security/pam_vbox.so"
    popd
    # systemd stuff
    install -Dm0644 60-vboxguest.rules "$pkgdir/usr/lib/udev/rules.d/60-vboxguest.rules"
    install -Dm0644 vboxservice-nox.service "$pkgdir/usr/lib/systemd/system/vboxservice.service"
    install -Dm0644 virtualbox-guest-utils.sysusers "$pkgdir/usr/lib/sysusers.d/virtualbox-guest-utils.conf"
    # licence
    install -Dm0644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_virtualbox-ext-vnc-svn() {
    pkgdesc='VirtualBox VNC extension pack'
    depends=('virtualbox' 'libvncserver')
    optdepends=('tigervnc: vnc client')
    provides=('virtualbox-ext-vnc')
    conflicts=('virtualbox-ext-vnc')
    install=virtualbox-ext-vnc.install

    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/packages"
    install -Dm0644 VNC-*.vbox-extpack "$pkgdir/usr/share/virtualbox/extensions/VNC-svn.vbox-extpack"
    # licence
    install -Dm0644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=4 sw=4 et:
