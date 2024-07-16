# Maintainer: Toolybird <toolybird at tuta dot io>
#
# WORK IN PROGRESS
#
# <rant>This thing is a packaging nightmare!! The upstream build system is
# *especially* distro unfriendly (build on Centos 7...WTF?). Building from
# source to proper Arch standards is "interesting" to say the least.</rant>
#
# NOTE: upstream uses losetup (root) for disk image preparation and GRUB
# installation. Solved by utilizing libguestfs/QEMU.
#
# NOT INCLUDED (compared to upstream): ARM64, MIPS64, LiveCD.
#
# PROBLEMS: FIXME
#
# - ancient pkg versions used in the build
# - includes bundled / vendored sources
# - some third party / pre-compiled / downloaded binaries are used
#
# This PKGBUILD is based on "INSTALL/all_in_one.sh". The upstream build
# environment is Centos 7 (as root!). See "DOC/BuildVentoyFromSource.txt" and
# GitHub CI/docker files. The Ventoy code is unfortunately built upon very old
# and outdated pkgs. In order to achieve an initial working build, I've simply
# tried to replicate upstream procedures as much as possible. Some patches are
# required to successfully build on a modern Arch system. The main components of
# Ventoy are heavily modified versions of:
#
# - grub (Jul 2019) (2.04)
# - ipxe (Sep 2019) (3fe683e)
# - edk2 (Dec 2019) (201911)
#
# Please see the "License" folder for full details of various other bits that
# have been modified.

pkgname=ventoy
pkgver=1.0.99
_grub_ver=2.04                  # (Jul 2019)
#_unifont_ver=15.0.01            # FIXME see NOTE below
_ipxe_ver=3fe683e               # (Sep 29 2019)
_edk2_ver=stable201911          # (Dec 2019)
_diet_ver=0.34                  # FIXME AUR pkg needs a patch, see below, build our own (64/32)
_musl_ver=1.2.5                 # upstream uses 1.2.1, use repo for 64-bit, build our own 32-bit
_kern_hdrs_musl_ver=4.19.88     # for busybox 32-bit
_fuse_ver=2.9.9                 # need a static lib built against musl, build our own (64/32)
_exfat_ver=1.3.0                # (Sep 2018) old! FIXME see comments below for why we build our own
_lz4_ver=1.8.1.2                # (Jan 2018) old! FIXME statically linked into unsquashfs
_xz_ver=5.0.4                   # (Jun 2012) old! FIXME statically linked into unsquashfs
_lzo_ver=2.08                   # (Jun 2014) old! FIXME statically linked into unsquashfs
_zstd_ver=1.4.4                 # (Nov 2019) old! FIXME statically linked into unsquashfs
_zlib_ver=1.3.1                 # need a static 32-bit lib for unsquashfs, build our own
_squash_ver=4.4                 # (Aug 2019) old! FIXME for unsquashfs
_dm_ver=1.02.28                 # (Sep 2008) old! FIXME for dmsetup
_zstd1_ver=1.0.0                # (Sep 2016) old! FIXME for standalone zstdcat
_xz_embed_ver=20130513          # (May 2013) old! FIXME for xzminidec
_busybox_ver=1.32.0             # (Jun 2020) old! FIXME
_crypt_ver=1.7.5                # (Apr 2017) old! FIXME for veritysetup
_lunzip_ver=1.11                # (Jan 2019) old! FIXME
_wimboot_ver=2.7.3              # (Apr 2021) old! FIXME
pkgrel=2
pkgdesc="A new bootable USB solution"
arch=(x86_64)
url="https://www.ventoy.net/"
license=(GPL-3.0-or-later)
depends=(bash dosfstools)
makedepends=(
  acpica                # edk2
  cdrtools              # EfiISO
  cpio                  # IMG/USB prep
  device-mapper         # grub2
  freetype2             # grub2
  fuse2                 # grub2 exfat
  git                   # ipxe
  gtk3                  # GUI
  kernel-headers-musl   # busybox
  lib32-gcc-libs        # 32-bit squashfs-tools lz4 xz lzo zstd vblade
  lib32-glibc           # 32-bit dietlibc vtoytool dmsetup zstdcat xzminidec busybox lunzip
  libguestfs            # IMG/USB prep
  linux                 # libguestfs
  musl                  # vtoycli fuse fuseiso xzminidec busybox
  nasm                  # edk2
  python                # grub2 edk2
  python-setuptools     # edk2 (python-3.12+)
  qt5-base              # GUI
  ttf-dejavu            # grub2
)
optdepends=(
  'gtk3: for GTK GUI'
  'parted: for preferred CLI partitioner'
  'polkit: for GUI privilege escalation'
  'qt5-base: for Qt GUI'
)
conflicts=(ventoy-bin)
# A regression in latest pacman unsets MAKEFLAGS when using !buildflags.
# https://gitlab.archlinux.org/archlinux/packaging/packages/pacman/-/issues/25
# Workaround it for now by manually unsetting VARS. See (way down) below in build() function.
#options=(!buildflags)
source=(
  "$pkgname-$pkgver.tar.gz::https://github.com/ventoy/Ventoy/archive/refs/tags/v$pkgver.tar.gz"
  https://ftp.gnu.org/gnu/grub/grub-"$_grub_ver".tar.xz
  ventoy-grub-fix-build-with-binutils-2.36.patch::https://git.savannah.gnu.org/cgit/grub.git/patch/configure.ac?id=b9827513
  # https://ftp.gnu.org/gnu/unifont/unifont-"$_unifont_ver/unifont-$_unifont_ver".bdf.gz
  git+https://github.com/ipxe/ipxe.git#commit="$_ipxe_ver"
  https://github.com/tianocore/edk2/archive/refs/tags/edk2-"$_edk2_ver".zip
  ventoy-fix-ucs-2-lookup-on-python-3.9.patch::https://github.com/tianocore/edk2/commit/5d864834.patch
  ventoy-fix-array.array.tostring-removal-in-python-3.9.patch::https://github.com/tianocore/edk2/commit/43bec9ea.patch
  https://www.fefe.de/dietlibc/dietlibc-"$_diet_ver".tar.xz
  dietlibc-headers-fix.patch::https://salsa.debian.org/debian/dietlibc/-/raw/master/debian/patches/bugfixes/newer-linux-headers.diff
  https://musl.libc.org/releases/musl-"$_musl_ver".tar.gz
  kernel-headers-musl-"$_kern_hdrs_musl_ver".tar.gz::https://github.com/sabotage-linux/kernel-headers/archive/v"$_kern_hdrs_musl_ver".tar.gz
  https://github.com/libfuse/libfuse/releases/download/fuse-"$_fuse_ver/fuse-$_fuse_ver".tar.gz
  exfat-"$_exfat_ver".tar.gz::https://github.com/relan/exfat/archive/refs/tags/v"$_exfat_ver".tar.gz
  https://github.com/madler/zlib/releases/download/v"$_zlib_ver/zlib-$_zlib_ver".tar.xz
  squashfs-tools-"$_squash_ver".tar.gz::https://github.com/plougher/squashfs-tools/archive/refs/tags/"$_squash_ver".tar.gz
  http://vault.centos.org/5.3/os/SRPMS/device-mapper-"$_dm_ver"-2.el5.src.rpm
  zstd-"$_zstd1_ver".tar.gz::https://github.com/facebook/zstd/archive/refs/tags/v"$_zstd1_ver".tar.gz
  https://tukaani.org/xz/xz-embedded-"$_xz_embed_ver".tar.gz
  https://busybox.net/downloads/busybox-"$_busybox_ver".tar.bz2
  https://mirrors.edge.kernel.org/pub/linux/utils/cryptsetup/v"${_crypt_ver%.*}"/cryptsetup-"$_crypt_ver".tar.xz
  wimboot-"$_wimboot_ver".tar.gz::https://github.com/ipxe/wimboot/archive/v"$_wimboot_ver".tar.gz
  wimboot-binutils-2.42-fix.patch
)
noextract=(
  grub-"$_grub_ver".tar.xz
  edk2-"$_edk2_ver".zip
  fuse-"$_fuse_ver".tar.gz
  exfat-"$_exfat_ver".tar.gz
  zlib-"$_zlib_ver".tar.xz
  squashfs-tools-"$_squash_ver".tar.gz
  device-mapper-"$_dm_ver"-2.el5.src.rpm
  zstd-"$_zstd1_ver".tar.gz
  xz-embedded-"$_xz_embed_ver".tar.gz
  busybox-"$_busybox_ver".tar.bz2
  cryptsetup-"$_crypt_ver".tar.xz
  wimboot-"$_wimboot_ver".tar.gz
)
sha256sums=('2557ccdeaf8b0e517087afb63f65c4e2a32ef3f15bd196b7f828d93d586ca7b9'
            'e5292496995ad42dabe843a0192cf2a2c502e7ffcc7479398232b10a472df77d'
            'db2a9018392a3984d1e1e649bde0ffc19c90fa4d96b9fd2d4caaf9c1ca2af68b'
            '5ee49d23d376aeea24269f7605fcaa7fbd326c04cda4e31b8eb7fa15a540ef44'
            'c6f691aa91afbaab811a369fe729f61d8e5b58bb5ad79a45446c9ee849c1a60b'
            'SKIP' # Cannot rely on GitHub to maintain a stable patch checksum
            'SKIP' # Cannot rely on GitHub to maintain a stable patch checksum
            '7994ad5a63d00446da2e95da1f3f03355b272f096d7eb9830417ab14393b3ace'
            '313aa962c7f80a02f41758d90d6f67687c77c74a6126b060337f248bc1b637f6'
            'a9a118bbe84d8764da0ea0d28b3ab3fae8477fc7e4085d90102b8596fc7c75e4'
            'd104397fc657ffb0f0bda46f54fd182b76a9ebc324149c183a4ff8c86a8db53d'
            'd0e69d5d608cc22ff4843791ad097f554dd32540ddc9bed7638cc6fea7c1b4b5'
            '689bcb4a639acd2d45e6fa0ff455f7f18edb2421d4f4f42909943775adc0e375'
            '38ef96b8dfe510d42707d9c781877914792541133e1870841463bfa73f883e32'
            'a7fa4845e9908523c38d4acf92f8a41fdfcd19def41bd5090d7ad767a6dc75c3'
            '599a630fdf020282e27c66aa2b4f3d624d731bd150749a8d7b74f544be03b2bb'
            '197e6ef74da878cbf72844f38461bb18129d144fd5221b3598e973ecda6f5963'
            '19577e9f68a2d4e08bb5564e3946e35c6323276cb6749c101c86e26505e3bf0e'
            'c35d87f1d04b2b153d33c275c2632e40d388a88f19a9e71727e0bbbff51fe689'
            '2b30cd1d0dd606a53ac77b406e1d37798d4b0762fa89de6ea546201906a251bd'
            '3cf04ca4a5b4466e624570d980638f8ab72feaed9b94106dd6ed2bed674a4cdf'
            '8121a64145ff317693de80148fbdca6cb73d3f2ed92f66b946949750ab71afe9')

# Some components below are notated as follows:
#
# 'HOST' -> a tool that runs on Arch itself. e.g. it might be part of the
# install routine to set up (install) a Ventoy USB drive. Usually a "normal"
# x86_64 binary.
#
# 'IMG/USB' -> a tool that is "embedded" into a Ventoy USB drive. The tool is
# stored inside a cpio archive on the ESP and is typically involved in the
# process of booting ISO's. There will usually be an additional 32-bit binary.
# These tools are meant to be small and self-contained and are often statically
# linked against dietlibc or musl.

prepare() {
  cd Ventoy-$pkgver
  : "${_DIFF:=0}" # "1" to generate diffs for easier inspection of Ventoy mod's.

  # Create our own INSTALL trees
  mv -v INSTALL{,.upstream}
  mv -v IMG/cpio_x86{,.upstream}

  (
    # Refer "GRUB2/buildgrub.sh"
    cd GRUB2
    mkdir -v SRC NBP PXE
    tar -xf "$srcdir"/grub-$_grub_ver.tar.xz -C SRC
    cp -av MOD_SRC/grub-$_grub_ver SRC

    if ((_DIFF)); then
      tar -xf "$srcdir"/grub-$_grub_ver.tar.xz -C SRC --xform "s|\(grub-$_grub_ver\)|\1.orig|"
      diff -urN SRC/grub-$_grub_ver{.orig,} > ventoy-$pkgver-grub-$_grub_ver.patch || :
    fi

    # Fix build for newer toolchain.
    patch -d SRC/grub-$_grub_ver -Np1 -i "$srcdir"/ventoy-grub-fix-build-with-binutils-2.36.patch

    # Tweak font path.
    sed -i 's|\(/usr/share/fonts/dejavu\)|\1 /usr/share/fonts/TTF|g' SRC/grub-$_grub_ver/configure.ac

    # NOTE: Upstream builds don't include this. Yet they ship their own
    # {ascii,unicode}.pf2 font files...how are they derived? FIXME
    # gzip -cd "$srcdir"/unifont-$_unifont_ver.bdf.gz > SRC/grub-$_grub_ver/unifont.bdf
  )

  (
    # Refer "IPXE/buildipxe.sh"
    cd IPXE
    tar -xf ipxe_org_code/ipxe-$_ipxe_ver.tar.bz2
    cp -av ipxe_mod_code/ipxe-$_ipxe_ver .

    if ((_DIFF)); then
      # The bundled tarball has been independently verified as being identical
      # to a git checkout. But might as well use the git version for comparison.
      diff -urN -x .git "$srcdir"/ipxe ipxe-$_ipxe_ver > ventoy-$pkgver-ipxe-$_ipxe_ver.patch || :
    fi

    rm -rfv ipxe-$_ipxe_ver/src/{bin,drivers}
  )

  (
    # Refer "EDK2/buildedk.sh"
    cd EDK2
    bsdtar -xf "$srcdir"/edk2-$_edk2_ver.zip
    cp -av edk2_mod/edk2-edk2-$_edk2_ver .

    if ((_DIFF)); then
      bsdtar -xf "$srcdir"/edk2-$_edk2_ver.zip -s "|edk2-edk2-$_edk2_ver|~.orig|"
      diff -urN edk2-edk2-$_edk2_ver{.orig,} > ventoy-$pkgver-edk2-$_edk2_ver.patch || :
    fi

    cd edk2-edk2-$_edk2_ver

    # Remove -Werror for successful build (as per main Arch repo).
    sed -i 's/ -Werror//g' BaseTools/Conf/*.template BaseTools/Source/C/Makefiles/*.makefile

    # Fix build with newer toolchain.
    sed -i 's/GCC48/GCC5/' ../build.sh

    # Fix build against recent python.
    patch -Np1 -i "$srcdir"/ventoy-fix-ucs-2-lookup-on-python-3.9.patch
    patch -Np1 -i "$srcdir"/ventoy-fix-array.array.tostring-removal-in-python-3.9.patch
  )

  (
    cd "$srcdir"/dietlibc-$_diet_ver

    # Fix from Debian. Avoid errors when compiling apps against recent kernel headers. FIXME
    patch -Np1 -i "$srcdir"/dietlibc-headers-fix.patch

    # <cpuid.h> compile fix
    sed -i 's/__leaf/__LEAF/' include/sys/cdefs.h
  )

  (
    cd SQUASHFS
    if ((_DIFF)); then
      tar -xf "$srcdir"/squashfs-tools-$_squash_ver.tar.gz --xform "s|\(squashfs-tools-$_squash_ver\)|\1.orig|"
      diff -urN squashfs-tools-$_squash_ver{.orig,} > ventoy-$pkgver-squashfs-tools-$_squash_ver.patch || :
    fi
  )

  (
    cd Ventoy2Disk
    if ((_DIFF)); then
      tar -xf "$srcdir"/xz-embedded-$_xz_embed_ver.tar.gz -C Ventoy2Disk --xform "s|\(xz-embedded-$_xz_embed_ver\)|\1.orig|"
      diff -urN Ventoy2Disk/xz-embedded-$_xz_embed_ver{.orig,} > ventoy-$pkgver-xz-embedded-$_xz_embed_ver.patch || :
    fi
  )

  (
    cd wimboot
    # Some *.S files are missing from the bundled source. We will grab them from the tarball.
    tar -xf "$srcdir"/wimboot-$_wimboot_ver.tar.gz --xform "s|\(wimboot-$_wimboot_ver\)|\1.orig|"

    if ((_DIFF)); then
      diff -ur wimboot-$_wimboot_ver{.orig,}/src > ventoy-$pkgver-wimboot-$_wimboot_ver.patch || :
    fi

    # Fix build with recent binutils.
    cd wimboot-$_wimboot_ver.orig
    patch -Np1 -i "$srcdir"/wimboot-binutils-2.42-fix.patch
  )
}

_build_grub() (
  echo ":: grub"
  # Refer "GRUB2/buildgrub.sh"
  cd Ventoy-$pkgver/GRUB2
  local _VT_GRUB_DIR=$PWD

  (
    cd SRC/grub-$_grub_ver
    ./autogen.sh
  )

  cp -a SRC/grub-$_grub_ver SRC/grub-x86_64-efi
  cp -a SRC/grub-$_grub_ver SRC/grub-i386-efi
  cp -a SRC/grub-$_grub_ver SRC/grub-i386-pc

  mkdir -pv ../INSTALL/{EFI/BOOT,grub/i386-pc}
  local _conf_args=(--prefix="$_VT_GRUB_DIR"/INSTALL --disable-werror)

  _build_grub-x86_64-efi() (
    cd SRC/grub-x86_64-efi
    ./configure --with-platform=efi "${_conf_args[@]}"
    make
    sh install.sh uefi
  )

  _build_grub-i386-efi() (
    cd SRC/grub-i386-efi
    ./configure --target=i386 --with-platform=efi "${_conf_args[@]}"
    make
    sh install.sh i386efi
  )

  _build_grub-i386-pc() (
    cd SRC/grub-i386-pc
    ./configure --target=i386 --with-platform=pc "${_conf_args[@]}"
    make
    sh install.sh
  )

  _build_grub-x86_64-efi
  _build_grub-i386-efi
  _build_grub-i386-pc

  # Copy over the ancillary stuff.
  local _d
  for _d in distro fonts help menu themes; do
    cp -av ../INSTALL.upstream/grub/$_d ../INSTALL/grub
  done
  cp -av ../INSTALL.upstream/grub/*.cfg ../INSTALL/grub
)

_build_ipxe() (
  echo ":: ipxe"
  # Refer "IPXE/buildipxe.sh"
  cd Ventoy-$pkgver/IPXE/ipxe-$_ipxe_ver/src

  make bin/ipxe.lkrn NO_WERROR=1 V=1
  install -Dv bin/ipxe.lkrn "$srcdir"/Ventoy-$pkgver/INSTALL/ventoy/ipxe.krn
)

_build_edk2() (
  echo ":: edk2"
  # Refer "EDK2/buildedk.sh"
  cd Ventoy-$pkgver/EDK2

  (
    cd edk2-edk2-$_edk2_ver
    make -C BaseTools
  )

  mkdir -pv ../INSTALL/ventoy
  sh ./build.sh ia32
  sh ./build.sh
)

_build_dietlibc() (
  echo ":: dietlibc"
  # Refer "DOC/installdietlibc.sh"
  cd dietlibc-$_diet_ver
  make
  make i386
)

_build_musl32() (
  echo ":: musl32"
  # Refer "DOC/BuildVentoyFromSource.txt" Section 2.3
  (
    cd musl-$_musl_ver

    CFLAGS=-m32 \
      ./configure --prefix="$srcdir"/musl32 --syslibdir="$srcdir"/musl32/lib \
      --target=i386 --build=i386
    make
    make install
  )

  cd kernel-headers-$_kern_hdrs_musl_ver
  make ARCH=x86 prefix="$srcdir"/musl32 install
)

# IMG/USB
_build_vtoytool() (
  echo ":: vtoytool"
  # Refer "VtoyTool/build.sh"
  cd Ventoy-$pkgver/VtoyTool

  "$srcdir"/dietlibc-$_diet_ver/bin-x86_64/diet -Os gcc -DVTOY_X86_64 -D_FILE_OFFSET_BITS=64 ./*.c BabyISO/*.c \
    -IBabyISO -Wall -DBUILD_VTOY_TOOL -DUSE_DIET_C -o vtoytool_64

  "$srcdir"/dietlibc-$_diet_ver/bin-i386/diet -Os gcc -DVTOY_I386 -D_FILE_OFFSET_BITS=64 -m32 ./*.c BabyISO/*.c \
    -IBabyISO -Wall -DBUILD_VTOY_TOOL -DUSE_DIET_C -o vtoytool_32

  strip --strip-all vtoytool_{64,32}
  rm -rfv vtoytool
  install -Dvt vtoytool/00 vtoytool_{64,32}
)

# HOST
_build_vtoycli() (
  echo ":: vtoycli"
  # Refer "vtoycli/fat_io_lib/buildlib.sh" and "vtoycli/build.sh"
  #
  # Upstream builds small and static here, but this is a "host" binary so we
  # don't really need that, nor do we need a 32-bit binary. A "normal" GCC
  # binary would do. FIXME

  cd Ventoy-$pkgver/vtoycli

  (
    cd fat_io_lib/release
    rm -rfv ../{include,lib}

    # GCC-14 build fix
    sed -i '/fat_cache.h/a #include "fat_format.h"' fat_filelib.c

    musl-gcc -O2 -D_FILE_OFFSET_BITS=64 fat*.c -c
    ar -rc libfat_io_64.a ./*.o
    rm -fv ./*.o

    # gcc -m32 -O2 -D_FILE_OFFSET_BITS=64 fat*.c -c
    # ar -rc libfat_io_32.a ./*.o
    # rm -fv ./*.o

    mkdir -v ../{include,lib}
    mv -v ./*.a ../lib/
    cp -av ./*.h ../include/
  )

  local _SRCS=(vtoycli.c vtoyfat.c vtoygpt.c crc32.c partresize.c)

  musl-gcc -Os -static -D_FILE_OFFSET_BITS=64 \
    "${_SRCS[@]}" -Ifat_io_lib/include fat_io_lib/lib/libfat_io_64.a -o vtoycli_64

  # "$srcdir"/dietlibc-$_diet_ver/bin-i386/diet -Os gcc -D_FILE_OFFSET_BITS=64 -m32 \
  #   "${_SRCS[@]}" -Ifat_io_lib/include fat_io_lib/lib/libfat_io_32.a -o vtoycli_32

  strip --strip-all vtoycli_64
  # strip --strip-all vtoycli_32
  install -Dv vtoycli_64 ../INSTALL/tool/x86_64/vtoycli
  # install -Dv vtoycli_32 ../INSTALL/tool/i386/vtoycli
)

# IMG/USB
_build_fuseiso() (
  echo ":: fuseiso"
  # Refer "FUSEISO/build.sh"
  cd Ventoy-$pkgver/FUSEISO

  __build_libfuse_static() (
    # Refer "FUSEISO/build_libfuse.sh"
    tar -xf "$srcdir"/fuse-$_fuse_ver.tar.gz
    cd fuse-$_fuse_ver
    mkdir -v build{64,32}

    local _conf_args=(
      --disable-shared
      --disable-util
      --disable-example
      CFLAGS=-Os
    )

    (
      cd build64
      CC=musl-gcc \
        ../configure "${_conf_args[@]}"
      make V=1
    )

    (
      cd build32
      CC="$srcdir/musl32/bin/musl-gcc -m32" \
        LDFLAGS="-Wl,-melf_i386" \
        ../configure "${_conf_args[@]}"
      make V=1
    )
  )

  __build_libfuse_static

  rm -fv vtoy_fuse_iso_*

  musl-gcc -static -O2 -D_FILE_OFFSET_BITS=64 vtoy_fuse_iso.c -Ifuse-$_fuse_ver/include \
    fuse-$_fuse_ver/build64/lib/.libs/libfuse.a -o vtoy_fuse_iso_64

  "$srcdir"/musl32/bin/musl-gcc -m32 -static -O2 -D_FILE_OFFSET_BITS=64 \
    vtoy_fuse_iso.c -Ifuse-$_fuse_ver/include -Wl,-melf_i386 \
    fuse-$_fuse_ver/build32/lib/.libs/libfuse.a -o vtoy_fuse_iso_32

  strip --strip-all vtoy_fuse_iso_{64,32}
)

# HOST
_build_exfat() (
  echo ":: exfat"
  # Refer "ExFAT/buidexfat.sh"
  #
  # This is the FUSE based pkg. The version in the repo "exfat-utils" is going
  # away in favor of the kernel based "exfatprogs" [1]. Ventoy is apparently not
  # yet ready for the newer "exfatprogs" tools. Upstream builds want to link
  # "libfuse.a" statically, however this is a "host" binary so there's no need.
  # Additionally, Ventoy modifies it slightly with the sed below. Although, it
  # appears the mod is only applicable to "mount.exfat-fuse" which we don't need
  # (see below). FIXME
  #
  # [1] https://bugs.archlinux.org/task/72629

  cd Ventoy-$pkgver/ExFAT

  tar -xf "$srcdir"/exfat-$_exfat_ver.tar.gz
  cd exfat-$_exfat_ver

  sed "/printf.*VERSION/a\\\tif (access(\"/etc/initrd-release\", F_OK) >= 0) argv[0][0] = '@';" \
    -i fuse/main.c
  autoreconf -i
  ./configure
  make

  # NOTE: AFAICT "mount.exfat-fuse" is used only in the LiveCD which is of no use to us.
  # If it turns out that it is required, a runtime dep on "fuse2" will be needed.

  # strip --strip-all fuse/mount.exfat-fuse
  strip --strip-all mkfs/mkexfatfs

  # install -Dvt ../../INSTALL/tool/x86_64 fuse/mount.exfat-fuse
  install -Dvt ../../INSTALL/tool/x86_64 mkfs/mkexfatfs
)

# IMG/USB
_build_unsquashfs() (
  echo ":: unsquashfs"
  # Refer "SQUASHFS/build.txt"
  cd Ventoy-$pkgver/SQUASHFS/SRC
  CFLAGS=-Os
  local _libdir="$srcdir"/Ventoy-$pkgver/SQUASHFS/LIB

  __build_lz4_static() (
    # Refer "SQUASHFS/SRC/build_lz4.sh"
    # The bundled lz4 tarball (ver 1.8.1.2 Jan 2018) has been independently
    # verified as being identical to the one available on GitHub.

    tar -xf lz4-$_lz4_ver.tar.gz
    sed -i "s/@\$(CC)/\$(CC)/" lz4-$_lz4_ver/lib/Makefile
    cp -a lz4-$_lz4_ver{,-32}

    (
      cd lz4-$_lz4_ver
      make -C lib
      make -C lib install PREFIX="$_libdir"/LZ4
    )

    (
      cd lz4-$_lz4_ver-32
      CC="gcc -m32" \
        make -C lib
      make -C lib install PREFIX="$_libdir"32/LZ4
    )
  )

  __build_xz_static() (
    # Refer "SQUASHFS/SRC/build_lzma.sh"
    # The bundled liblzma/xz zip file contents have been independently verified
    # as being identical to (ver 5.0.4 Jun 2012) available on [1], apart from
    # the addition of a single file "liblzma-builder.sh".
    #
    # [1] https://tukaani.org/xz/old.html

    bsdtar -xf liblzma-master.zip
    cp -a liblzma-master{,-32}

    local _conf_args=(
      --disable-shared
      --disable-xz
      --disable-xzdec
      --disable-lzmadec
      --disable-lzmainfo
      --enable-small
    )

    (
      cd liblzma-master
      ./configure --prefix="$_libdir"/LZMA "${_conf_args[@]}"
      make
      make install
    )

    (
      cd liblzma-master-32
      CC="gcc -m32" \
        ./configure --prefix="$_libdir"32/LZMA "${_conf_args[@]}"
      make
      make install
    )
  )

  __build_lzo_static() (
    # Refer "SQUASHFS/SRC/build_lzo.sh"
    # The bundled lzo tarball (ver 2.08 Jun 2014) contents have been
    # independently verified as being identical to the 2.08 tarball available
    # on [1], apart from a 1 line change in "configure{,.ac}" and a minor change
    # in "include/lzo/lzodefs.h" but these appear to be tweaks by lzo upstream.
    #
    # [1] https://www.oberhumer.com/opensource/lzo/download/lzo-2.08.tar.gz

    tar -xf lzo-$_lzo_ver.tar.gz
    cp -a lzo-$_lzo_ver{,-32}

    (
      cd lzo-$_lzo_ver
      ./configure --prefix="$_libdir"/LZO
      make V=1
      make install
    )

    (
      cd lzo-$_lzo_ver-32
      CC="gcc -m32" \
        ./configure --prefix="$_libdir"32/LZO
      make V=1
      make install
    )
  )

  __build_zstd_static() (
    # Refer "SQUASHFS/SRC/build_zstd.sh"
    # The bundled zstd tarball (ver 1.4.4 Nov 2019) has been independently
    # verified as being identical to the one available on GitHub.

    tar -xf zstd-$_zstd_ver.tar.gz
    cp -a zstd-$_zstd_ver{,-32}

    (
      cd zstd-$_zstd_ver
      ZSTD_LIB_COMPRESSION=0 make -C lib
      make -C lib install PREFIX="$_libdir"/ZSTD
    )

    (
      cd zstd-$_zstd_ver-32
      export CC="gcc -m32"
      ZSTD_LIB_COMPRESSION=0 make -C lib
      make -C lib install PREFIX="$_libdir"32/ZSTD
    )
  )

  __build_zlib_static-32() (
    tar -xf "$srcdir"/zlib-$_zlib_ver.tar.xz
    cd zlib-$_zlib_ver

    CC="gcc -m32" \
      ./configure --static
    make
  )

  __build_lz4_static
  __build_xz_static
  __build_lzo_static
  __build_zstd_static
  __build_zlib_static-32

  cd "$srcdir"/Ventoy-$pkgver/SQUASHFS
  unset CFLAGS
  cp -a squashfs-tools-4.4/squashfs-tools{,-32}
  rm -fv unsquashfs_*

  (
    cd squashfs-tools-4.4/squashfs-tools
    sed -i 's|LIBS) -o|LIBS) /usr/lib/libz.a -o|' Makefile
    make unsquashfs LZ4_LIBDIR="$_libdir"/LZ4 LZMA_LIBDIR="$_libdir"/LZMA \
      LZO_LIBDIR="$_libdir"/LZO ZSTD_LIBDIR="$_libdir"/ZSTD

    strip --strip-all unsquashfs
    cp -av unsquashfs ../../unsquashfs_64
  )

  (
    cd squashfs-tools-4.4/squashfs-tools-32
    sed -i "s|LIBS) -o|LIBS) ../../SRC/zlib-$_zlib_ver/libz.a -o|" Makefile
    CC="gcc -m32" \
      make unsquashfs LZ4_LIBDIR="$_libdir"32/LZ4 LZMA_LIBDIR="$_libdir"32/LZMA \
      LZO_LIBDIR="$_libdir"32/LZO ZSTD_LIBDIR="$_libdir"32/ZSTD

    strip --strip-all unsquashfs
    cp -av unsquashfs ../../unsquashfs_32
  )
)

# IMG/USB
_build_vblade() (
  echo ":: vblade"
  # Refer "VBLADE/vblade-master/build.sh"
  cd Ventoy-$pkgver/VBLADE/vblade-master
  rm -fv vblade_*

  # Need -fcommon for build to succeed FIXME
  gcc linux.c aoe.c ata.c bpf.c -Os -o vblade_64 -fcommon
  gcc linux.c aoe.c ata.c bpf.c -Os -m32 -o vblade_32 -fcommon

  strip --strip-all vblade_{64,32}
)

# IMG/USB
_build_dmsetup() (
  echo ":: dmsetup"
  # Refer "DMSETUP/build.txt"
  cd Ventoy-$pkgver/DMSETUP
  rm -fv dmsetup*
  bsdtar -O -xvf "$srcdir"/device-mapper*.rpm device-mapper*.tgz | tar -xzf -

  tee -a device-mapper.$_dm_ver/include/configure.h.in > /dev/null << _EOF_
#ifndef UINT32_MAX
#define UINT32_MAX (4294967295U)
#endif

#ifndef UINT64_C
#define UINT64_C(c) c ## ULL
#endif
_EOF_

  # GCC-14 build fixes
  sed -i '/ctype.h/a #include <strings.h>' device-mapper.$_dm_ver/lib/libdm-report.c
  sed -i '/langinfo.h/a #include <strings.h>' device-mapper.$_dm_ver/dmsetup/dmsetup.c

  cp -a device-mapper.$_dm_ver{,-32}

  (
    cd device-mapper.$_dm_ver
    CC="$srcdir/dietlibc-$_diet_ver/bin-x86_64/diet gcc" \
      ./configure
    sed -i '/rpl_malloc/d' include/configure.h
    make
    strip --strip-all dmsetup/dmsetup
    cp -av dmsetup/dmsetup ../dmsetup64
  )

  (
    cd device-mapper.$_dm_ver-32
    CC="$srcdir/dietlibc-$_diet_ver/bin-i386/diet gcc -m32" \
      ./configure
    sed -i '/rpl_malloc/d' include/configure.h
    make
    strip --strip-all dmsetup/dmsetup
    cp -av dmsetup/dmsetup ../dmsetup32
  )
)

# IMG/USB
_build_zstdcat() (
  echo ":: zstdcat"
  # Refer "ZSTD/build.txt"
  cd Ventoy-$pkgver/ZSTD
  rm -fv zstdcat*
  tar -xf "$srcdir"/zstd-$_zstd1_ver.tar.gz
  cp -a zstd-$_zstd1_ver{,-32}

  local _compile_opts1=(
    -I../lib -I../lib/common -I../lib/dictBuilder -I../lib/legacy -Wall -DZSTD_LEGACY_SUPPORT=1
    ../lib/decompress/zstd_decompress.c -c -o ../lib/decompress/zstd_decompress.o
  )

  local _compile_opts2=(
      -I../lib -I../lib/common -I../lib/dictBuilder -I../lib/legacy -Wall -DZSTD_LEGACY_SUPPORT=1
      ../lib/decompress/zstd_decompress.o ../lib/decompress/huf_decompress.c ../lib/common/entropy_common.c
      ../lib/common/fse_decompress.c ../lib/common/xxhash.c ../lib/common/zstd_common.c
      ../lib/compress/zstd_compress.c ../lib/compress/fse_compress.c ../lib/compress/huf_compress.c
      ../lib/legacy/zstd_v01.c ../lib/legacy/zstd_v02.c ../lib/legacy/zstd_v03.c ../lib/legacy/zstd_v04.c
      ../lib/legacy/zstd_v05.c ../lib/legacy/zstd_v06.c ../lib/legacy/zstd_v07.c ../lib/dictBuilder/divsufsort.c
      ../lib/dictBuilder/zdict.c zstdcli.c fileio.c bench.c datagen.c dibio.c -o zstd
  )

  (
    cd zstd-$_zstd1_ver/programs
    "$srcdir"/dietlibc-$_diet_ver/bin-x86_64/diet -Os gcc -pipe -nostdinc -falign-loops=32 "${_compile_opts1[@]}"
    "$srcdir"/dietlibc-$_diet_ver/bin-x86_64/diet -Os gcc -pipe -nostdinc "${_compile_opts2[@]}"
    strip --strip-all zstd
    cp -av zstd ../../zstdcat64
  )

  (
    cd zstd-$_zstd1_ver-32/programs
    "$srcdir"/dietlibc-$_diet_ver/bin-i386/diet -Os gcc -m32 -pipe -nostdinc -falign-loops=32 "${_compile_opts1[@]}"
    "$srcdir"/dietlibc-$_diet_ver/bin-i386/diet -Os gcc -m32 -pipe -nostdinc "${_compile_opts2[@]}"
    strip --strip-all zstd
    cp -av zstd ../../zstdcat
  )

  install -Dvt ../IMG/cpio_x86/ventoy/tool zstdcat{,64}
)

# IMG/USB
_build_xzminidec() (
  echo ":: xzminidec"
  # Refer "DOC/BuildVentoyFromSource.txt" Section(s) 4.15 and 4.16
  cd Ventoy-$pkgver/Ventoy2Disk/Ventoy2Disk/xz-embedded-20130513/userspace

  make -f ventoy_makefile CC="$srcdir/dietlibc-$_diet_ver/bin-i386/diet gcc -Os -m32 -std=gnu89"
  mv -v xzminidec{,32}
  make clean
  rm -v bytetest.o

  make -f ventoy_makefile CC="$srcdir/dietlibc-$_diet_ver/bin-x86_64/diet gcc -Os -std=gnu89"
  mv -v xzminidec{,64}
  make clean
  rm -v bytetest.o

  make -f ventoy_makefile CC="musl-gcc -Os -static -std=gnu89"
  mv -v xzminidec{,64_musl}
  make clean
  rm -v bytetest.o

  strip --strip-all xzminidec{32,64}*
  install -Dvt ../../../../IMG/cpio_x86/ventoy/busybox xzminidec{32,64}*
)

# IMG/USB
_build_busybox() (
  echo ":: busybox"
  # Refer "BUSYBOX/build.txt"
  cd Ventoy-$pkgver/BUSYBOX
  mkdir -pv ../IMG/cpio_x86/ventoy/busybox

  (
    # Refer "BUSYBOX/chmod/build.sh"
    cd chmod
    rm -vf vtchmod*{32,64}*

    "$srcdir"/dietlibc-$_diet_ver/bin-x86_64/diet gcc -Os vtchmod.c -o vtchmod64
    "$srcdir"/dietlibc-$_diet_ver/bin-i386/diet gcc -Os -m32 vtchmod.c -o vtchmod32
    musl-gcc -Os -static vtchmod.c -o vtchmod64_musl
    strip --strip-all vtchmod{64,32} vtchmod64_musl
    cp -avt ../../IMG/cpio_x86/ventoy/busybox vtchmod{64,32} vtchmod64_musl
  )

  tar -xf "$srcdir"/busybox-$_busybox_ver.tar.bz2

  cp -a busybox-$_busybox_ver{,-xzcat64}
  cp -a busybox-$_busybox_ver{,-xzcat32}
  cp -a busybox-$_busybox_ver{,-32}

  (
    cd busybox-$_busybox_ver-xzcat64
    cp -av ../x86_64_xzcat.config .config
    make CC=musl-gcc V=1
    mv -v busybox xzcat64_musl
    xz xzcat64_musl
    cp -avt ../../IMG/cpio_x86/ventoy/busybox xzcat64_musl.xz
  )

  (
    cd busybox-$_busybox_ver-xzcat32
    sed 's/# CONFIG_LFS is not set/CONFIG_LFS=y/' ../x86_64_xzcat.config > .config
    make CC="$srcdir/musl32/bin/musl-gcc -m32 -Wl,-melf_i386" V=1
    mv -v busybox xzcat32_musl
    xz xzcat32_musl
    cp -avt ../../IMG/cpio_x86/ventoy/busybox xzcat32_musl.xz
  )

  (
    cd busybox-$_busybox_ver
    make defconfig
    sed -i 's/# CONFIG_STATIC is not set/CONFIG_STATIC=y/' .config
    make CC=musl-gcc V=1
    mv -v busybox busybox64
    xz busybox64
    cp -avt ../../IMG/cpio_x86/ventoy/busybox busybox64.xz
  )

  (
    cd busybox-$_busybox_ver-32
    make defconfig
    sed -i 's/# CONFIG_STATIC is not set/CONFIG_STATIC=y/' .config
    make CC="$srcdir/musl32/bin/musl-gcc -m32 -Wl,-melf_i386" V=1
    mv -v busybox busybox32
    xz busybox32
    cp -avt ../../IMG/cpio_x86/ventoy/busybox busybox32.xz
  )
)

# IMG/USB
_build_lunzip() (
  echo ":: lunzip"
  # Refer "DOC/BuildVentoyFromSource.txt" Section 4.19
  # The bundled lunzip tarball (ver 1.11 Jan 2019) has been independently
  # verified as being identical to the one available on [1].
  #
  # [1] http://download.savannah.gnu.org/releases/lzip/lunzip/

  cd Ventoy-$pkgver/LZIP
  rm -fv lunzip*{32,64}
  tar -xf lunzip-$_lunzip_ver.tar.gz
  cp -a lunzip-$_lunzip_ver{,-32}

  (
    cd lunzip-$_lunzip_ver
    ./configure CC="$srcdir/dietlibc-$_diet_ver/bin-x86_64/diet gcc" CFLAGS=-Os
    make
    strip --strip-all lunzip
    cp -av lunzip ../lunzip64
  )

  (
    cd lunzip-$_lunzip_ver-32
    ./configure CC="$srcdir/dietlibc-$_diet_ver/bin-i386/diet gcc -m32" CFLAGS=-Os
    make
    strip --strip-all lunzip
    cp -av lunzip ../lunzip32
  )

  # Undocumented!
  rm -fv lz4cat*
  "$srcdir"/dietlibc-$_diet_ver/bin-x86_64/diet -Os gcc -D_FILE_OFFSET_BITS=64 smallz4cat.c -o lz4cat64
  strip --strip-all lz4cat64
  install -Dvt ../IMG/cpio_x86/ventoy/tool lz4cat64
)

# IMG/USB
_build_verity() (
  echo ":: verity"
  # Refer "cryptsetup/cryptsetup-build.txt"
  # Needed for *experimental* FydeOS/CloudReady (ChromeOS) support.

  cd Ventoy-$pkgver/cryptsetup
  tar -xf "$srcdir"/cryptsetup-$_crypt_ver.tar.xz
  cp -a cryptsetup-$_crypt_ver{,-32}

  # 30 Jun 2024. Ugh, this now fails to build because latest libgcrypt-1.11.0
  # has removed libgcrypt-config. Just use the upstream provided 64-bit binary
  # for now. The ChromeOS support is experimental anyway. FIXME

  # (
  #   rm -v veritysetup64
  #   cd cryptsetup-$_crypt_ver
  #   ./configure --enable-static --host=x86_64-pc-linux-gnu
  #   make
  #   cd src
  #   gcc -Wall -O2 -o veritysetup veritysetup-utils_crypt.o veritysetup-utils_loop.o veritysetup-utils_tools.o \
  #     veritysetup-veritysetup.o -lpopt -ldevmapper -lgcrypt -luuid .././lib/.libs/libcryptsetup.a
  #   strip --strip-all veritysetup
  #   cp -av veritysetup ../../veritysetup64
  # )

  # Ugh, this needs multilib (lib32-e2fsprogs lib32-popt lib32-libgcrypt) and
  # a 32-bit libdevmapper which doesn't actually exist in the repo. Just use the
  # upstream provided 32-bit binary for now. FIXME

  # rm -v veritysetup32
  # cd cryptsetup-$_crypt_ver-32
  # CC="gcc -m32" \
  # ./configure --enable-static --host=x86_64-pc-linux-gnu
  # make
  # cd src
  # gcc -m32 -Wall -O2 -o veritysetup veritysetup-utils_crypt.o veritysetup-utils_loop.o veritysetup-utils_tools.o \
  #   veritysetup-veritysetup.o -lpopt -ldevmapper -lgcrypt -luuid .././lib/.libs/libcryptsetup.a
  # strip --strip-all veritysetup
  # cp -av veritysetup ../../veritysetup32
)

# IMG/USB
_build_wimboot() (
  echo ":: wimboot"
  # Refer "wimboot/build.sh"
  cd Ventoy-$pkgver/wimboot/wimboot-$_wimboot_ver/src

  # Grab the missing *.S files
  cp -av ../../wimboot-$_wimboot_ver.orig/src/*.S .
  sed -i '/^CFLAGS/s/ -Werror//' Makefile

  # pesign (if installed) appears to make no difference, ignore.
  make wimboot.x86_64 wimboot.i386.efi
  xz wimboot.{x86_64,i386.efi}
  install -Dvt "$srcdir"/Ventoy-$pkgver/INSTALL/ventoy wimboot.{x86_64,i386.efi}.xz
)

_pack_ventoy() (
  echo ":: pack"
  # Refer "INSTALL/ventoy_pack.sh"
  # 3RD PARTY BINARIES ALERT! FIXME

  cd Ventoy-$pkgver
  local _LDFLAGS="-Wl,-O1,--sort-common,--as-needed,-z,relro,-z,now,-z,pack-relative-relocs"

  (
    cd IMG
    sed -i '/arm64 #/i exit 0' mkcpio.sh
    install -dv cpio_x86/ventoy/{busybox,tool}
    cp -avt cpio_x86/ventoy/tool cpio_x86.upstream/ventoy/tool/*.sh

    # 32-bit tiny lz4cat binary FIXME
    # Refer "DOC/BuildVentoyFromSource.txt" Section 5.1
    cp -avt cpio_x86/ventoy/tool cpio_x86.upstream/ventoy/tool/lz4cat

    # 32-bit busybox ar binary FIXME
    # Refer "DOC/BuildVentoyFromSource.txt" Section 5.2
    cp -avt cpio_x86/ventoy/tool cpio_x86.upstream/ventoy/tool/ar

    # 32-bit busybox inotifyd binary FIXME
    # Refer "DOC/BuildVentoyFromSource.txt" Section 5.3
    cp -avt cpio_x86/ventoy/tool cpio_x86.upstream/ventoy/tool/inotifyd

    # 32-bit busybox ash binary FIXME
    # Refer "DOC/BuildVentoyFromSource.txt" Section 5.4
    cp -avt cpio_x86/ventoy/busybox cpio_x86.upstream/ventoy/busybox/ash

    # 64-bit busybox ash binary FIXME
    # Refer "DOC/BuildVentoyFromSource.txt" Section 4.18
    # For some unknown reason this is the only binary built with uclibc.
    # Please see: https://github.com/ventoy/Ventoy/issues/2183
    cp -avt cpio_x86/ventoy/busybox cpio_x86.upstream/ventoy/busybox/64h

    # patch for device-mapper kernel modules FIXME
    # Refer "DMPATCH/readme.txt"
    cp -avt cpio_x86/ventoy/tool cpio_x86.upstream/ventoy/tool/dm_patch_*

    sh mkcpio.sh
    install -Dvm 644 -t ../INSTALL/ventoy ventoy.cpio ventoy_x86.cpio

    # "IMG/vtloopex" contains pre-compiled binary kernel modules (dm-mod) for
    # stuff like LibreELEC, openwrt, etc. FIXME
    sh mkloopex.sh
  )

  (
    # "IMG/Unix" contains pre-compiled binary kernel modules (geom_ventoy) for
    # various BSD's, FreeBSD, etc. FIXME
    cd Unix
    sh pack_unix.sh
  )

  (
    # HOST
    cd LinuxGUI
    sed -i '/dos2unix/d' language.sh
    sh language.sh

    mkdir -pv ../INSTALL/tool/x86_64

    sed -e '/^build.*i386/d;/^build.*aarch64/d;/^build.*mips/d;/^build.*gtk2/d;/^export/d' \
        -e "/\$XXLIB/a \        $_LDFLAGS \\\\" \
        -e "/VTOY_GUI/s/$/ $_LDFLAGS/" -i.bak build.sh build_gtk.sh
    sh build.sh
    sh build_gtk.sh

    sed -e '/^if.*CentOS8/,+6d;/^build.*aarch64$/d;/^build.*mips64el$/d' \
        -e '/QT_INC.*gcc_64/a \    QT_INC_PATH="/usr/include/qt"' \
        -e '/QT_LIB.*gcc_64/a \    QT_LIB_PATH="/usr/lib"' \
        -e "/LFLAGS.*PATH\"/a \    LFLAGS+=\" $_LDFLAGS\"" -i.bak build_qt.sh
    sh build_qt.sh
  )

  (
    # HOST
    cd Plugson
    sed -e '/^build.*i386/d;/^build.*aarch64/d;/^build.*mips/d' \
        -e "/\$XXLIB/a \        $_LDFLAGS \\\\" -i.bak build.sh
    sh build.sh
    sh pack.sh
  )

  (
    # HOST
    # Upstream builds small and static here, but this is a "host" binary so we
    # don't really need that. A "normal" GCC binary would do. FIXME
    cd Vlnk
    local _SRCS=(src/crc32.c src/main_linux.c src/vlnk.c)

    musl-gcc -Os -static -D_FILE_OFFSET_BITS=64 "${_SRCS[@]}" -Isrc -o vlnk
    strip --strip-all vlnk
    install -Dvt ../INSTALL/tool/x86_64 vlnk

    sh pack.sh
  )

  (
    cd EfiISO
    sed -i 's/-P/-publisher/' mkefiiso.sh
    sh mkefiiso.sh
  )

  # Binary EFI Secure Boot stuff FIXME
  # These files are taken from various projects. "?" denotes unverified/unknown origin

  local _efi_files=(
    BOOTIA32.EFI        # shim 32-bit  ver 15.6         # SUISBD [1] based on Fedora
    BOOTX64.EFI         # shim 64-bit  ver 15.7         # ? SUSE Linux Enterprise ?
    grub.efi            # preloader 64-bit              # SUISBD [1]
    grubia32.efi        # preloader 32-bit              # SUISBD [2]
    mmia32.efi          # MokManager 32-bit  ver 15.6   # same length as SUISBD [1] (but 261 bytes differ) based on Fedora
    MokManager.efi      # MokManager 64-bit  ver 15.7   # ? SUSE Linux Enterprise ?
  )

  # This file is also from SUISBD
  install -vm 644 INSTALL.upstream/tool/ENROLL_THIS_KEY_IN_MOKMANAGER.cer INSTALL/tool
  (
    cd INSTALL.upstream/EFI/BOOT
    install -Dvt "$srcdir"/Ventoy-$pkgver/INSTALL/EFI/BOOT "${_efi_files[@]}"
  )
  # [1] https://github.com/ValdikSS/Super-UEFIinSecureBoot-Disk/releases/download/3-4/Super-UEFIinSecureBoot-Disk_minimal_v3-4.zip
  # [2] https://github.com/ValdikSS/Super-UEFIinSecureBoot-Disk/releases/download/3-3/Super-UEFIinSecureBoot-Disk_minimal_v3-3.zip

  # More EFI stuff. Should be buildable with EDK2 FIXME
  # Refer "DOC/BuildVentoyFromSource.txt" Section 4.17
  cp -avt INSTALL/ventoy INSTALL.upstream/ventoy/iso9660_{x64,ia32}.efi
  cp -avt INSTALL/ventoy INSTALL.upstream/ventoy/udf_{x64,ia32}.efi

  # Windows stuff. Apparently buildable with Microsoft Visual Studio FIXME
  # Refer "DOC/BuildVentoyFromSource.txt" Section 4.4
  cp -avt INSTALL/ventoy INSTALL.upstream/ventoy/vtoyjump{64,32}.exe

  # 3rd party Windows stuff FIXME
  # Refer "DOC/BuildVentoyFromSource.txt" Section(s) 5.12 and 5.8
  cp -avt INSTALL/ventoy INSTALL.upstream/ventoy/7z
  cp -avt INSTALL/ventoy INSTALL.upstream/ventoy/imdisk

  # Unknown Windows crap. Config data for Windows Boot Manager? Where from? FIXME
  cp -avt INSTALL/ventoy INSTALL.upstream/ventoy/common_{bcd,bootmgr}.xz

  # From syslinux. Could we use our own repo version? FIXME
  # Refer "DOC/BuildVentoyFromSource.txt" Section 5.9
  cp -avt INSTALL/ventoy INSTALL.upstream/ventoy/memdisk

  # DragonFly BSD stuff FIXME
  # Refer "Unix/ventoy_unix/DragonFly/mkinitrd.sh"
  cp -avt INSTALL/ventoy INSTALL.upstream/ventoy/dragonfly.mfs.xz
)

_create_img() (
  echo ":: image"
  # Refer "INSTALL/ventoy_pack.sh"
  mkdir -pv Ventoy-$pkgver/INSTALL
  cd Ventoy-$pkgver/INSTALL

  # Create a 256M Ventoy disk image, partition/format a 32M ESP
  dd if=/dev/zero of=img.bin bs=1M count=256 status=none
  echo -e 'size=223M, type=7, bootable\n size=32M, type=U\n' | sfdisk img.bin
  guestfish add img.bin : run : mkfs vfat /dev/sda2 label:VTOYEFI

  # Create a 64M "scratch" disk image / ext4 partition
  dd if=/dev/zero of=scratch.bin bs=1M count=64 status=none
  echo -e 'size=+\n' | sfdisk scratch.bin
  guestfish add scratch.bin : run : mkfs ext4 /dev/sda1 label:SCRATCH

  # Copy our GRUB stuff into the scratch disk
  tar -czvf - -C "$srcdir"/Ventoy-$pkgver/INSTALL grub/i386-pc |
    guestfish add scratch.bin : run : mount /dev/sda1 / : tar-in - / compress:gzip
  tar -czvf - -C "$srcdir"/Ventoy-$pkgver/GRUB2 INSTALL |
    guestfish add scratch.bin : run : mount /dev/sda1 / : tar-in - / compress:gzip

  # Do the GRUB install business
  #
  # XXX (ab)using `guestfish debug sh "args ..."' like this is a dirty hack. FIXME. Pls see:
  # https://www.libguestfs.org/guestfs-faq.1.html#whats-the-difference-between-guestfish-and-virt-rescue
  #
  # We should be using `guestfish sh command' or maybe `guestfish command "args ..."' but we
  # cannot do so because we don't have a proper guest filesystem.
  # https://www.libguestfs.org/guestfish.1.html#sh
  # https://www.libguestfs.org/guestfish.1.html#command
  #
  # Possible alternative for a guest image -> Arch Boxes basic qcow2...or maybe we just don't
  # use guestfish here at all and instead use something like [1] with an Arch ISO.
  #
  # [1] https://gitlab.archlinux.org/archlinux/ci-scripts/-/blob/master/scripts/build_in_archiso_vm.sh

  guestfish add img.bin : add scratch.bin : run : mount /dev/sdb1 / : debug sh \
    "/sysroot/INSTALL/sbin/grub-bios-setup --skip-fs-probe --directory=/sysroot/grub/i386-pc /dev/sda"

  (
    cd grub
    tar -czf help.tar.gz help
    rm -rf help

    vtlangtitle=$(grep VTLANG_LANGUAGE_NAME menu/zh_CN.json | awk -F\" '{print $4}')
    {
      echo "menuentry \"zh_CN  -  $vtlangtitle\" --class=menu_lang_item --class=debug_menu_lang --class=F5tool {"
      echo "    vt_load_menu_lang zh_CN"
      echo "}"
    } >> menulang.cfg

    # shellcheck disable=SC2010 # FIXME
    ls -1 menu | grep -v 'zh_CN' | sort | while read -r vtlang; do
      vtlangname=${vtlang%.*}
      vtlangtitle=$(grep VTLANG_LANGUAGE_NAME menu/"$vtlang" | awk -F\" '{print $4}')
      {
        echo "menuentry \"$vtlangname  -  $vtlangtitle\" --class=menu_lang_item --class=debug_menu_lang --class=F5tool {"
        echo "    vt_load_menu_lang $vtlangname"
        echo "}"
      } >> menulang.cfg
    done

    {
      echo "menuentry \"\$VTLANG_RETURN_PREVIOUS\" --class=vtoyret VTOY_RET {"
      echo "        echo \"Return ...\""
      echo "}"
    } >> menulang.cfg

    tar -czf menu.tar.gz menu
    rm -rf menu

    rm -fv i386-pc/*.img
  )

  # Apparently grub.cfg needs to be located at the front of the partition, copy it first..
  guestfish add img.bin : run : mount /dev/sda2 / : mkdir /grub : copy-in grub/grub.cfg /grub

  # ..and now the rest
  tar -czvf - --exclude=grub.cfg -C grub . |
    guestfish add img.bin : run : mount /dev/sda2 / : tar-in - /grub compress:gzip
  tar -czvf - ventoy EFI |
    guestfish add img.bin : run : mount /dev/sda2 / : tar-in - / compress:gzip
  guestfish add img.bin : run : mount /dev/sda2 / : copy-in tool/ENROLL_THIS_KEY_IN_MOKMANAGER.cer /

  # Just *WTF* is going on here? FIXME
  dd status=none bs=1024 count=16 if=/dev/zero of=/tmp/mount.exfat-fuse_aarch64
  guestfish add img.bin : run : mount /dev/sda2 / : mkdir /tool : copy-in /tmp/mount.exfat-fuse_aarch64 /tool

  # Prepare the final "payload" dir
  curver=$(grep 'set.*VENTOY_VERSION=' ./grub/grub.cfg | awk -F'"' '{print $2}')
  tmpdir=ventoy-$curver

  mkdir -pv "$tmpdir"/{boot,ventoy}
  echo "$curver" > "$tmpdir"/ventoy/version
  dd if=img.bin of="$tmpdir"/boot/boot.img bs=1 count=512 status=none
  dd if=img.bin of="$tmpdir"/boot/core.img bs=512 count=2047 skip=1 status=none
  xz --check=crc32 "$tmpdir"/boot/core.img

  cp -avt "$tmpdir" tool ../INSTALL.upstream/plugin ../LinuxGUI/WebUI
  sed -i 's/.*SCRIPT_DEL_THIS \(.*\)/\1/g' "$tmpdir"/WebUI/index.html

  cp -avt "$tmpdir"/tool \
    ../INSTALL.upstream/tool/{distro_gui_type.json,VentoyGTK.glade,ventoy_lib.sh,VentoyWorker.sh}

  cp -avt "$tmpdir" VentoyGUI.x86_64 VentoyVlnk.sh \
    ../INSTALL.upstream/{Ventoy2Disk,VentoyWeb,VentoyPlugson,CreatePersistentImg,ExtendPersistentImg}.sh

  # 32MB ESP image
  dd status=none if=img.bin of="$tmpdir"/ventoy/ventoy.disk.img bs=512 count=65536 skip=458752
  xz --check=crc32 "$tmpdir"/ventoy/ventoy.disk.img

  chmod -v +x "$tmpdir"{,/tool}/*.sh
  cp -avt "$tmpdir"/tool ../LANGUAGES/languages.json

  # Fix ups
  sed -e 's|./log.txt|/var/log/ventoy.log|' \
      -e "/^vtdebug()/a \    test -w /var/log && \\\\" -i "$tmpdir"/{Ventoy2Disk,tool/ventoy_lib}.sh

  sed -i 's|log.txt|/var/log/ventoy.log|' "$tmpdir/"WebUI/static/js/languages.js \
    "$tmpdir"/tool/{languages.json,VentoyWorker.sh} "$tmpdir"/VentoyWeb.sh

  sed -e '/^chmod/d' -e '/^echo.*decompress/d' \
      -e '/^echo.*2D/s|^|test -w /var/log \&\& |' \
      -e '/^date/s|^|test -w /var/log \&\& |' -i "$tmpdir"/Ventoy2Disk.sh

  sed -e 's|#!/bin/sh|#!/usr/bin/env bash|' -i "$tmpdir"/tool/{VentoyWorker.sh,ventoy_lib.sh}
)

build() {
  # Workaround for abovementioned pacman regression.
  unset CPPFLAGS CFLAGS DEBUG_CFLAGS CXXFLAGS DEBUG_CXXFLAGS LDFLAGS LTOFLAGS RUSTFLAGS DEBUG_RUSTFLAGS

  _build_grub
  _build_ipxe
  _build_edk2
  _build_dietlibc
  _build_musl32
  _build_vtoytool
  _build_vtoycli
  _build_fuseiso
  _build_exfat
  _build_unsquashfs
  _build_vblade
  _build_dmsetup
  _build_zstdcat
  _build_xzminidec
  _build_busybox
  _build_lunzip
  _build_verity
  _build_wimboot
  _pack_ventoy
  _create_img
}

package() {
  mkdir -pv "$pkgdir"/{opt,usr/{bin,share/{applications,pixmaps}}}

  cp -arv Ventoy-$pkgver/INSTALL/ventoy-$pkgver "$pkgdir"/opt/ventoy

  # Everything below this line -> Credits: https://aur.archlinux.org/packages/ventoy-bin
  tee "$pkgdir"/usr/bin/ventoy > /dev/null << _EOF_
#!/bin/sh

cd /opt/ventoy || exit 1
exec ./Ventoy2Disk.sh "\$@"
_EOF_

  tee "$pkgdir"/usr/bin/ventoygui > /dev/null << _EOF_
#!/bin/sh

cd /opt/ventoy || exit 1
./VentoyGUI.x86_64 "\$@"
_EOF_

  tee "$pkgdir"/usr/bin/ventoyplugson > /dev/null << _EOF_
#!/bin/sh

cd /opt/ventoy || exit 1
exec ./VentoyPlugson.sh "\$@"
_EOF_

  tee "$pkgdir"/usr/bin/ventoyweb > /dev/null << _EOF_
#!/bin/sh

cd /opt/ventoy || exit 1
exec ./VentoyWeb.sh "\$@"
_EOF_

  tee "$pkgdir"/usr/bin/ventoy-persistent > /dev/null << _EOF_
#!/bin/sh

exec /opt/ventoy/CreatePersistentImg.sh "\$@"
_EOF_

  tee "$pkgdir"/usr/bin/ventoy-extend-persistent > /dev/null << _EOF_
#!/bin/sh

exec /opt/ventoy/ExtendPersistentImg.sh "\$@"
_EOF_

  tee "$pkgdir"/usr/share/applications/ventoy.desktop > /dev/null << _EOF_
[Desktop Entry]
Type=Application
Icon=ventoy
Name=Ventoy
Exec=ventoygui --xdg
Terminal=false
Hidden=false
Categories=Utility
Comment=Ventoy2Disk GUI
_EOF_

  chmod -v 755 "$pkgdir"/usr/bin/*
  cp -av Ventoy-$pkgver/LinuxGUI/WebUI/static/img/VentoyLogo.png "$pkgdir"/usr/share/pixmaps/ventoy.png
}
