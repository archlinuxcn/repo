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
pkgver=76284
pkgrel=1
_vboxsf_commit='9451f61e6787e95aa51e42b6381db6b059bc49da'
arch=('x86_64')
url='http://virtualbox.org'
license=('GPL' 'custom')
makedepends=('alsa-lib'
             'bin86'
             'cdrkit'
             'curl'
             'dev86'
             'device-mapper'
             'git'
             'glu'
             'gsoap'
             'iasl'
             'opus'
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
             'python'
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
        # We need to build a modified version of vboxsf for Linux 4.16
        # https://bugzilla.redhat.com/show_bug.cgi?id=1481630#c65
        "git+https://github.com/jwrdegoede/vboxsf#commit=$_vboxsf_commit"
        'virtualbox-host-dkms.conf'
        'virtualbox-guest-dkms.conf'
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
        '002-dri-driver-path.patch'
        '005-gsoap-build.patch'
        '006-rdesktop-vrdp-keymap-path.patch'
        '008-no-vboxvideo.patch'
        '009-include-path.patch'
        '010-qt-5.11.patch'
        '011-python-3-7.patch'
        # The following patch and mount.vboxsf wrapper should be removed
        # once support for mainline-style options string gets upstreamed
        '012-vboxsf-automount.patch'
        'mount.vboxsf')
sha256sums=('SKIP'
            'SKIP'
            'deb03efa7ad0376aa55a087f2e882afe00935f10b0e7aa853ba9147090d341ec'
            'c328376b05183d269f98319ec660f54c55e298f77d229977606862b064651a7c'
            '43a97d07edd6f3f0e1181e84483759ad0a20c4e57ee93ca1a18530918979f9d8'
            '2101ebb58233bbfadf3aa74381f22f7e7e508559d2b46387114bc2d8e308554c'
            'da4c49f6ca94e047e196cdbcba2c321199f4760056ea66e0fbc659353e128c9e'
            '9c5238183019f9ebc7d92a8582cad232f471eab9d3278786225abc1a1c7bf66e'
            '033c597e0f5285d2ddb0490868e5b6f945f45c7b1b1152a02a9e6fea438b2c95'
            '918fe3ae7d60550181bcefedb55621f2c824087062c0df6ad03d148ed3f2ba01'
            '94a808f46909a51b2d0cf2c6e0a6c9dea792034943e6413bf9649a036c921b21'
            '01dbb921bd57a852919cc78be5b73580a564f28ebab2fe8d6c9b8301265cbfce'
            'e6e875ef186578b53106d7f6af48e426cdaf1b4e86834f01696b8ef1c685787f'
            '2a9d7748dc58f9d091f791da06b733a696943114f7c0d580fa00a0752eb1d2ac'
            'f67674931c30187f867233e3a4ae662f93c9110fbd0bfce50dd9f391f4533bc0'
            '7d2da8fe10a90f76bbfc80ad1f55df4414f118cd10e10abfb76070326abebd46'
            '5d5af2de5b1f1c61ec793503350f2440661cf8fd640f11b8a86f10bce499c0dc'
            '8b7f241107863f82a5b0ae336aead0b3366a40103ff72dbebf33f54b512a0cbc'
            '1acc7014bcb3d9ca6da29eed813c3d6e91a688c43f9d93802fd4e3814f67ace4'
            'c6ef35e6893d557c7c2269ff79bc299fe9058cfb2c933a7efdc7a8a7b6d9c5da'
            '55224cb74b54b331d691f171efc0d4c058a14f738551f1d8f559146c2908635d'
            'a784f3cc24652a16385cc63abac6c5178932ca5f3861be7650631b7dafa753a4'
            'f3ed6741f8977f40900c8aa372fa082df1f8723d497d4fff445153c543bc8947')
            
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

    msg2 'Use system GL headers'
    echo 'VBOX_USE_SYSTEM_GL_HEADERS=true' >> LocalConfig.kmk

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
    pkgdesc='Powerful x86 virtualization for enterprise as well as home use'
    depends=('glibc' 'openssl' 'curl' 'gcc-libs' 'libpng' 'python' 'sdl'
             'libvpx' 'libxml2' 'procps-ng' 'shared-mime-info' 'zlib'
             'libxcursor' 'libxinerama' 'libx11' 'libxext' 'libxmu' 'libxt'
             'qt5-base' 'qt5-x11extras' 'VIRTUALBOX-HOST-MODULES-SVN')
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
    install -m4755 VirtualBox VBoxSDL VBoxHeadless VBoxNetDHCP VBoxNetAdpCtl VBoxNetNAT -t "$pkgdir/usr/lib/virtualbox"
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
    install -Dm644 VirtualBox/COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

    # install systemd stuff
    install -Dm644 60-vboxdrv.rules "$pkgdir/usr/lib/udev/rules.d/60-vboxdrv.rules"
    install -Dm644 vboxweb.service "$pkgdir/usr/lib/systemd/system/vboxweb.service"
    install -Dm644 virtualbox.sysusers "$pkgdir/usr/lib/sysusers.d/virtualbox.conf"

    # install module reloading shortcut (with a symlink with default helper)
    install -Dm755 vboxreload "$pkgdir/usr/bin"
    ln -s vboxreload "$pkgdir/usr/bin/rcvboxdrv"
}

package_virtualbox-sdk-svn() {
    pkgdesc='VirtualBox Software Developer Kit (SDK)'
    depends=('python')
    provides=('virtualbox-sdk')
    conflicts=('virtualbox-sdk')

    install -dm755 "$pkgdir/usr/lib/virtualbox"

    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin"

    install -Dm755 vboxshell.py "$pkgdir/usr/lib/virtualbox/vboxshell.py"
    # python sdk
    pushd sdk/installer
    VBOX_INSTALL_PATH="/usr/lib/virtualbox" python vboxapisetup.py install --root "$pkgdir"
    popd
    cp -r sdk "$pkgdir/usr/lib/virtualbox"
    rm -r "$pkgdir/usr/lib/virtualbox/sdk/installer"
    # licence
    install -Dm644 "$srcdir/VirtualBox/COPYING" \
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

    install -dm755 "$pkgdir/usr/src"
    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin"
    cp -r src "$pkgdir/usr/src/vboxhost-svn_OSE"
    # licence
    install -Dm644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    # module loading
    local _p="$pkgdir/usr/lib/modules-load.d/virtualbox-host-dkms.conf"
    install -Dm644 /dev/null "$_p"
    printf "vboxdrv\nvboxpci\nvboxnetadp\nvboxnetflt\n" > "$_p"
    # starting vbox 5.1, dkms.conf file was dropped
    local _p="$pkgdir/usr/src/vboxhost-svn_OSE/dkms.conf"
    install -Dm644 "$srcdir/virtualbox-host-dkms.conf" "$_p"
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

    install -dm755 "$pkgdir/usr/src"
    source "VirtualBox/env.sh"
    cd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin/additions"
    cp -r src "$pkgdir/usr/src/vboxguest-svn_OSE"
    # licence
    install -Dm644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    # module loading
    local _p="$pkgdir/usr/lib/modules-load.d/virtualbox-guest-dkms.conf"
    install -Dm644 /dev/null "$_p"
    printf "vboxguest\nvboxsf\nvboxvideo\n" > "$_p"
    # starting vbox 5.1, dkms.conf file was dropped
    local _p="$pkgdir/usr/src/vboxguest-svn_OSE/dkms.conf"
    install -Dm644 "$srcdir/virtualbox-guest-dkms.conf" "$_p"
    sed -i "s,@VERSION@,svn," "$_p"

    # vboxsf module for Linux 4.16 and later
    install -d "$pkgdir/usr/src/vboxsf-svn_OSE"
    cp -rT "$srcdir/vboxsf" "$pkgdir/usr/src/vboxsf-svn_OSE/vboxsf"
    rm -rf "$pkgdir/usr/src/vboxsf-svn_OSE/vboxsf/.git"
    echo "obj-m = vboxsf/" >"$pkgdir/usr/src/vboxsf-svn_OSE/Makefile"
    local _p="$pkgdir/usr/src/vboxsf-svn_OSE/dkms.conf"
    install -Dm644 "$srcdir/virtualbox-vboxsf-dkms.conf" "$_p"
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
    install -m755 VBoxClient VBoxControl VBoxService "$srcdir/mount.vboxsf" "$pkgdir/usr/bin"
    install -Dm755 mount.vboxsf "$pkgdir/usr/lib/virtualbox/mount.vboxsf"
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
    install -Dm644 VirtualBox/COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_virtualbox-guest-utils-nox-svn() {
    pkgdesc='VirtualBox Guest userspace utilities without X support'
    depends=('glibc' 'pam' 'VIRTUALBOX-GUEST-MODULES-SVN')
    provides=('virtualbox-guest-utils-nox')
    conflicts=('virtualbox-guest-utils' 'virtualbox-guest-utils-nox')

    source "VirtualBox/env.sh"
    pushd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin/additions"
    install -d "$pkgdir/usr/bin"
    install -m755 VBoxControl VBoxService "$srcdir/mount.vboxsf" "$pkgdir/usr/bin"
    install -Dm755 mount.vboxsf "$pkgdir/usr/lib/virtualbox/mount.vboxsf"
    install -m755 -D pam_vbox.so "$pkgdir/usr/lib/security/pam_vbox.so"
    popd
    # systemd stuff
    install -Dm644 60-vboxguest.rules "$pkgdir/usr/lib/udev/rules.d/60-vboxguest.rules"
    install -Dm644 vboxservice-nox.service "$pkgdir/usr/lib/systemd/system/vboxservice.service"
    install -Dm644 virtualbox-guest-utils.sysusers "$pkgdir/usr/lib/sysusers.d/virtualbox-guest-utils.conf"
    # licence
    install -Dm644 "$srcdir/VirtualBox/COPYING" \
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
    install -Dm644 VNC-*.vbox-extpack "$pkgdir/usr/share/virtualbox/extensions/VNC-svn.vbox-extpack"
    # licence
    install -Dm644 "$srcdir/VirtualBox/COPYING" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=4 sw=4 et:
