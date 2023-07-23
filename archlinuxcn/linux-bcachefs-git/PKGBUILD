# Maintainer: Kyle De'Vir (QuartzDragon) <kyle[dot]devir[at]mykolab[dot]com>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>

### BUILD OPTIONS

# Set these variables to ANYTHING that is not null to enable them

# Set to force building with a particular commit ~ takes precedence over _bcachefs_branch
_bcachefs_commit=be3ef67f38e1e6a6bdbe2253b6bf4c19be05dcb9 # prandom: Remove unused include

# Set to force building with a particular branch
_bcachefs_branch=

# Tweak kernel options prior to a build via nconfig
_makenconfig=

# Optionally select a sub architecture by number if building in a clean chroot
# Leaving this entry blank will require user interaction during the build
# which will cause a failure to build if using makechrootpkg. Note that the
# generic (default) option is 40.
#
# Note - the march=native option is unavailable by this method, use the nconfig
# and manually select it.
#
# 1. AMD Opteron/Athlon64/Hammer/K8 (MK8)
# 2. AMD Opteron/Athlon64/Hammer/K8 with SSE3 (MK8SSE3)
# 3. AMD 61xx/7x50/PhenomX3/X4/II/K10 (MK10)
# 4. AMD Barcelona (MBARCELONA)
# 5. AMD Bobcat (MBOBCAT)
# 6. AMD Jaguar (MJAGUAR)
# 7. AMD Bulldozer (MBULLDOZER)
# 8. AMD Piledriver (MPILEDRIVER)
# 9. AMD Steamroller (MSTEAMROLLER)
# 10. AMD Excavator (MEXCAVATOR)
# 11. AMD Zen (MZEN)
# 12. AMD Zen 2 (MZEN2)
# 13. AMD Zen 3 (MZEN3)
# 14. AMD Zen 4 (MZEN4)
# 15. Intel P4 / older Netburst based Xeon (MPSC)
# 16. Intel Core 2 (MCORE2)
# 17. Intel Atom (MATOM)
# 18. Intel Nehalem (MNEHALEM)
# 19. Intel Westmere (MWESTMERE)
# 20. Intel Silvermont (MSILVERMONT)
# 21. Intel Goldmont (MGOLDMONT)
# 22. Intel Goldmont Plus (MGOLDMONTPLUS)
# 23. Intel Sandy Bridge (MSANDYBRIDGE)
# 24. Intel Ivy Bridge (MIVYBRIDGE)
# 25. Intel Haswell (MHASWELL)
# 26. Intel Broadwell (MBROADWELL)
# 27. Intel Skylake (MSKYLAKE)
# 28. Intel Skylake X (MSKYLAKEX)
# 29. Intel Cannon Lake (MCANNONLAKE)
# 30. Intel Ice Lake (MICELAKE)
# 31. Intel Cascade Lake (MCASCADELAKE)
# 32. Intel Cooper Lake (MCOOPERLAKE)
# 33. Intel Tiger Lake (MTIGERLAKE)
# 34. Intel Sapphire Rapids (MSAPPHIRERAPIDS)
# 35. Intel Rocket Lake (MROCKETLAKE)
# 36. Intel Alder Lake (MALDERLAKE)
# 37. Intel Raptor Lake (MRAPTORLAKE)
# 38. Intel Meteor Lake (MMETEORLAKE)
# 39. Intel Emerald Rapids (MEMERALDRAPIDS)
# 40. Generic-x86-64 (GENERIC_CPU)
# 41. Generic-x86-64-v2 (GENERIC_CPU2)
# 42. Generic-x86-64-v3 (GENERIC_CPU3)
# 43. Generic-x86-64-v4 (GENERIC_CPU4)
# 44. Intel-Native optimizations autodetected by the compiler (MNATIVE_INTEL)
# 45. AMD-Native optimizations autodetected by the compiler (MNATIVE_AMD)
_subarch=

# Compile ONLY used modules to VASTLY reduce the number of modules built
# and the build time.
#
# To keep track of which modules are needed for your specific system/hardware,
# give module_db script a try: https://aur.archlinux.org/packages/modprobed-db
# This PKGBUILD read the database kept if it exists
#
# More at this wiki page ---> https://wiki.archlinux.org/index.php/Modprobed-db
_localmodcfg=

pkgbase=linux-bcachefs-git
pkgver=6.4.3.arch1.r1189903.be3ef67f38e1
pkgrel=1
pkgdesc="Linux"
_srcver_tag=6.4.3.arch1
url="https://github.com/koverstreet/bcachefs"
arch=(x86_64)
license=(GPL2)
makedepends=(
    bc
    cpio
    gettext
    git
    libelf
    pahole
    perl
    tar
    xz

    # htmldocs
    graphviz
    imagemagick
    python-sphinx
    texlive-latexextra
)
options=('!strip')

_reponame="linux-bcachefs"
_repo_url="https://github.com/koverstreet/bcachefs.git"

_repo_url_arch="https://github.com/archlinux/linux.git"

_reponame_upstream="linux"
_repo_url_upstream="https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git"

_reponame_kernel_patch="kernel_compiler_patch"
_repo_url_kernel_patch="https://github.com/graysky2/${_reponame_kernel_patch}.git"
_kernel_patch_name="more-uarches-for-kernel-5.17+.patch"

_pkgdesc_extra="~ featuring Kent Overstreet's bcachefs filesystem"

_kernel_base_string="${_reponame}::git+${_repo_url}"
if [ -n "${_bcachefs_commit}" ]; then
    kernel_source_string="${_kernel_base_string}#commit=${_bcachefs_commit}"
elif [ -n "${_bcachefs_branch}" ]; then
    kernel_source_string="${_kernel_base_string}#branch=${_bcachefs_branch}"
else
    kernel_source_string="${_kernel_base_string}#branch=master"
fi

source=(
    ${kernel_source_string}
    #"${_reponame_upstream}::git+${_repo_url_upstream}"
    "git+${_repo_url_kernel_patch}"
    config # kernel config file
)
validpgpkeys=(
    ABAF11C65A2970B130ABE3C479BE3E4300411886  # Linus Torvalds
    647F28654894E3BD457199BE38DBBDC86092693E  # Greg Kroah-Hartman
    A2FF3A36AAA56654109064AB19802F8B0D70FC30  # Jan Alexander Steffens (heftig)
    C7E7849466FE2358343588377258734B41C31549  # David Runge <dvzrv@archlinux.org>
)
b2sums=('SKIP'
        'SKIP'
        '1886ac1f57ec860ce5ad00cd0ecf011de302879ca0ac597e5d7bd0a2a1da481c56e245393974d644ea5c9bc219152f3600a07dbf9bfa9b9b03259e4f4e8fea36')

export KBUILD_BUILD_HOST=archlinux
export KBUILD_BUILD_USER=$pkgbase
export KBUILD_BUILD_TIMESTAMP="$(date -Ru${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH})"

_make() {
    test -s version
    make KERNELRELEASE="$(<version)" "$@"
}

prepare() {
    cd "$srcdir/$_reponame"

    msg2 "Fetch and merge stable tag from ${_repo_url_arch} ..."
    git remote add arch_stable "${_repo_url_arch}" || true
    git fetch arch_stable "v${_srcver_tag%.*}-${_srcver_tag##*.}"
    git merge --no-edit --no-commit FETCH_HEAD

    #msg2 "Fetch and merge tag ${_srcver_tag//.arch*/} from Linux stable upstream repository..."
    #git remote add upstream_stable "${srcdir}/${_reponame_upstream}" || true
    #git fetch upstream_stable $v{_srcver_tag//.arch*/}
    #git merge --no-edit --no-commit FETCH_HEAD

    msg2 "Setting version..."
    echo "-$pkgrel" > localversion.10-pkgrel
    echo "${pkgbase#linux}" > localversion.20-pkgname
    pkgver > version
    make defconfig
    make -s kernelrelease
    make mrproper

    FullPatchesArray=(
        $_reponame_kernel_patch/$_kernel_patch_name
    )
    for MyPatch in "${FullPatchesArray[@]}"
    do
        msg2 "Applying patch $MyPatch..."
        patch -Np1 -i "$srcdir/$MyPatch"
    done

    msg2 "Setting config..."
    cp ../config .config

    if [ -n "$_subarch" ]; then
        yes "$_subarch" | _make oldconfig
    else
        _make prepare
    fi

    ### Optionally load needed modules for the make localmodconfig
    # See https://aur.archlinux.org/packages/modprobed-db
    if [ -n "$_localmodcfg" ]; then
        if [ -f $HOME/.config/modprobed.db ]; then
            msg2 "Running Steven Rostedt's make localmodconfig now"
            _make LSMOD=$HOME/.config/modprobed.db localmodconfig
        else
            msg2 "No modprobed.db data found"
            exit
        fi
    fi

    # do not run 'make olddefconfig' as it sets default options
    yes "" | _make config >/dev/null

    msg2 "Showing config diff"
    diff -u ../config .config || :

    msg2 "Prepared $pkgbase version $(<version)"

    [[ -z "$_makenconfig" ]] || _make nconfig

    # save configuration for later reuse
    cat .config > "$startdir/config.last"
}

pkgver() {
    cd "${srcdir}/${_reponame}"
    printf "%s.r%s.%s" "${_srcver_tag//-/.}" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd $_reponame
    _make all
    _make htmldocs
}

_package() {
    pkgdesc="The $pkgdesc kernel and modules $_pkgdesc_extra"
    depends=(
        coreutils
        initramfs
        kmod
        bcachefs-tools-git
    )
    optdepends=(
        'wireless-regdb: to set the correct wireless channels of your country'
        'linux-firmware: firmware images needed for some devices'
    )
    provides=(
        KSMBD-MODULE
        VIRTUALBOX-GUEST-MODULES
        WIREGUARD-MODULE
    )
    replaces=(
        virtualbox-guest-modules-arch
        wireguard-arch
    )

    cd $_reponame
    local modulesdir="$pkgdir/usr/lib/modules/$(<version)"

    msg2 "Installing boot image..."
    # systemd expects to find the kernel here to allow hibernation
    # https://github.com/systemd/systemd/commit/edda44605f06a41fb86b7ab8128dcf99161d2344
    install -Dm644 "$(_make -s image_name)" "$modulesdir/vmlinuz"

    # Used by mkinitcpio to name the kernel
    echo "$pkgbase" | install -Dm644 /dev/stdin "$modulesdir/pkgbase"

    msg2 "Installing modules..."
    ZSTD_CLEVEL=19 _make INSTALL_MOD_PATH="$pkgdir/usr" INSTALL_MOD_STRIP=1 \
        DEPMOD=/doesnt/exist modules_install  # Suppress depmod

    # remove build and source links
    rm "$modulesdir"/{source,build}
}

_package-headers() {
    pkgdesc="Headers and scripts for building modules for the $pkgdesc kernel $_pkgdesc_extra"
    depends=(pahole)

    cd $_reponame
    local builddir="$pkgdir/usr/lib/modules/$(<version)/build"

    msg2 "Installing build files..."
    install -Dt "$builddir" -m644 .config Makefile Module.symvers System.map \
        localversion.* version vmlinux
    install -Dt "$builddir/kernel" -m644 kernel/Makefile
    install -Dt "$builddir/arch/x86" -m644 arch/x86/Makefile
    cp -t "$builddir" -a scripts

    # required when STACK_VALIDATION is enabled
    install -Dt "$builddir/tools/objtool" tools/objtool/objtool

    # required when DEBUG_INFO_BTF_MODULES is enabled
    install -Dt "$builddir/tools/bpf/resolve_btfids" tools/bpf/resolve_btfids/resolve_btfids

    msg2 "Installing headers..."
    cp -t "$builddir" -a include
    cp -t "$builddir/arch/x86" -a arch/x86/include
    install -Dt "$builddir/arch/x86/kernel" -m644 arch/x86/kernel/asm-offsets.s

    install -Dt "$builddir/drivers/md" -m644 drivers/md/*.h
    install -Dt "$builddir/net/mac80211" -m644 net/mac80211/*.h

    # https://bugs.archlinux.org/task/13146
    install -Dt "$builddir/drivers/media/i2c" -m644 drivers/media/i2c/msp3400-driver.h

    # https://bugs.archlinux.org/task/20402
    install -Dt "$builddir/drivers/media/usb/dvb-usb" -m644 drivers/media/usb/dvb-usb/*.h
    install -Dt "$builddir/drivers/media/dvb-frontends" -m644 drivers/media/dvb-frontends/*.h
    install -Dt "$builddir/drivers/media/tuners" -m644 drivers/media/tuners/*.h

    # https://bugs.archlinux.org/task/71392
    install -Dt "$builddir/drivers/iio/common/hid-sensors" -m644 drivers/iio/common/hid-sensors/*.h

    msg2 "Installing KConfig files..."
    find . -name 'Kconfig*' -exec install -Dm644 {} "$builddir/{}" \;

    msg2 "Removing unneeded architectures..."
    local arch
    for arch in "$builddir"/arch/*/; do
        [[ $arch = */x86/ ]] && continue
        echo "Removing $(basename "$arch")"
        rm -r "$arch"
    done

    msg2 "Removing documentation..."
    rm -r "$builddir/Documentation"

    msg2 "Removing broken symlinks..."
    find -L "$builddir" -type l -printf 'Removing %P\n' -delete

    msg2 "Removing loose objects..."
    find "$builddir" -type f -name '*.o' -printf 'Removing %P\n' -delete

    msg2 "Stripping build tools..."
    local file
    while read -rd '' file; do
        case "$(file -Sib "$file")" in
            application/x-sharedlib\;*)      # Libraries (.so)
                strip -v $STRIP_SHARED "$file" ;;
            application/x-archive\;*)        # Libraries (.a)
                strip -v $STRIP_STATIC "$file" ;;
            application/x-executable\;*)     # Binaries
                strip -v $STRIP_BINARIES "$file" ;;
            application/x-pie-executable\;*) # Relocatable binaries
                strip -v $STRIP_SHARED "$file" ;;
        esac
    done < <(find "$builddir" -type f -perm -u+x ! -name vmlinux -print0)

    echo "Stripping vmlinux..."
    strip -v $STRIP_STATIC "$builddir/vmlinux"

    msg2 "Adding symlink..."
    mkdir -p "$pkgdir/usr/src"
    ln -sr "$builddir" "$pkgdir/usr/src/$pkgbase"
}

_package-docs() {
    pkgdesc="Documentation for the $pkgdesc kernel $_pkgdesc_extra"

    cd $_srcname
    local builddir="$pkgdir/usr/lib/modules/$(<version)/build"

    msg2 "Installing documentation..."
    local src dst
    while read -rd '' src; do
        dst="${src#Documentation/}"
        dst="$builddir/Documentation/${dst#output/}"
        install -Dm644 "$src" "$dst"
    done < <(find Documentation -name '.*' -prune -o ! -type d -print0)

    msg2 "Adding symlink..."
    mkdir -p "$pkgdir/usr/share/doc"
    ln -sr "$builddir/Documentation" "$pkgdir/usr/share/doc/$pkgbase"
}

pkgname=(
    "$pkgbase"
    "$pkgbase-headers"
    "$pkgbase-docs"
)
for _p in "${pkgname[@]}"; do
    eval "package_$_p() {
        $(declare -f "_package${_p#$pkgbase}")
        _package${_p#$pkgbase}
    }"
done

# vim:set ts=8 sts=2 sw=2 et:
