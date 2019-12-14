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
pkgver=82582
pkgrel=1
_vboxsf_commit='87b9015c57dd7f226c768131bf8b4c0249de9835'
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
        '005-gsoap-build.patch'
        '006-rdesktop-vrdp-keymap-path.patch'
        '008-no-vboxvideo.patch'
        '012-vbglR3GuestCtrlDetectPeekGetCancelSupport.patch'
        '013-Makefile.patch'
        # The following patch and mount.vboxsf wrapper should be removed
        # once support for mainline-style options string gets upstreamed
        '101-vboxsf-automount.patch'
        'mount.vboxsf')
sha256sums=('SKIP'
            'SKIP'
            '76d98ea062fcad9e5e3fa981d046a6eb12a3e718a296544a68b66f4b65cb56db'
            'c328376b05183d269f98319ec660f54c55e298f77d229977606862b064651a7c'
            'e37712bcbbafbdee47230a962446d63b0ae882801a89931d93ad9e704e70ad4b'
            '2101ebb58233bbfadf3aa74381f22f7e7e508559d2b46387114bc2d8e308554c'
            'da4c49f6ca94e047e196cdbcba2c321199f4760056ea66e0fbc659353e128c9e'
            '9c5238183019f9ebc7d92a8582cad232f471eab9d3278786225abc1a1c7bf66e'
            '033c597e0f5285d2ddb0490868e5b6f945f45c7b1b1152a02a9e6fea438b2c95'
            '2be313b98bffde482aad93b00c419f1d5f7645fd9e6053175ffb0d925067f96a'
            '94a808f46909a51b2d0cf2c6e0a6c9dea792034943e6413bf9649a036c921b21'
            '01dbb921bd57a852919cc78be5b73580a564f28ebab2fe8d6c9b8301265cbfce'
            'e6e875ef186578b53106d7f6af48e426cdaf1b4e86834f01696b8ef1c685787f'
            '4001b5927348fe669a541e80526d4f9ea91b883805f102f7d571edbb482a9b9d'
            '7d2da8fe10a90f76bbfc80ad1f55df4414f118cd10e10abfb76070326abebd46'
            '13c6ca9be0f91582445fd2a14a8c58a0625a15d9cb98cb6e8c2736d77ea976ab'
            '8b7f241107863f82a5b0ae336aead0b3366a40103ff72dbebf33f54b512a0cbc'
            '06485dce54a5f21b85f4360db884d98c1ab091d3f2535881ec9fcd82feb06b7e'
            'da7e58ed37dc23c6202aab3017864579a99e78417f3421ddcc98a198198fe2c9'
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
    kmk -C src/VBox/RDP/client-1.8.4

    msg2 'Build VNC extension pack'
    kmk -C src/VBox/ExtPacks/VNC packing
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

    # libraries
    install -dm0755 "$pkgdir/usr/lib/virtualbox"
    install -m0755 *.so "$pkgdir/usr/lib/virtualbox"
    install -m0644 VBoxEFI*.fd "$pkgdir/usr/lib/virtualbox"
    ## setuid root binaries
    install -m4755 VBoxSDL VirtualBoxVM VBoxHeadless VBoxNetDHCP VBoxNetAdpCtl VBoxNetNAT -t "$pkgdir/usr/lib/virtualbox"
    ## other binaries
    install -m0755 VirtualBox VBoxManage VBoxSVC VBoxExtPackHelperApp VBoxXPCOMIPCD VBoxTestOGL VBoxBalloonCtrl vboxwebsrv webtest -t "$pkgdir/usr/lib/virtualbox"

    # components
    # [heavysink] Temporary remove non-existent symlink VBoxREM.so
    rm components/VBoxREM.so
    install -dm0755 "$pkgdir/usr/lib/virtualbox/components"
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
    # starting vbox 5.1, dkms.conf file was dropped
    local _p="$pkgdir/usr/src/vboxguest-svn_OSE/dkms.conf"
    install -Dm0644 "$srcdir/virtualbox-guest-dkms.conf" "$_p"
    sed -i "s,@VERSION@,svn," "$_p"

    # vboxsf module for Linux 4.16 and later
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
             'libxdamage' 'libxrandr' 'libxext' 'libxfixes' 'libxmu' 'libxt' 'xorg-xrandr'
             'VIRTUALBOX-GUEST-MODULES-SVN')
    replaces=('virtualbox-archlinux-additions' 'virtualbox-guest-additions')
    provides=('virtualbox-guest-utils')
    conflicts=('virtualbox-archlinux-additions' 'virtualbox-guest-additions' 'virtualbox-guest-utils-nox' 'virtualbox-guest-utils')

    source "VirtualBox/env.sh"
    pushd "VirtualBox/out/linux.$BUILD_PLATFORM_ARCH/release/bin/additions"
    install -d "$pkgdir/usr/bin"
    install -m0755 VBoxClient VBoxControl VBoxService "$srcdir/mount.vboxsf" "$pkgdir/usr/bin"
    install -Dm0755 mount.vboxsf "$pkgdir/usr/lib/virtualbox/mount.vboxsf"
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
    install -m0755 VBoxControl VBoxService "$srcdir/mount.vboxsf" "$pkgdir/usr/bin"
    install -Dm0755 mount.vboxsf "$pkgdir/usr/lib/virtualbox/mount.vboxsf"
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
