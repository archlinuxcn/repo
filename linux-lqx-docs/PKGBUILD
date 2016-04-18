# Maintainer: Piotr Gorski <lucjan.lucjanov@gmail.com> PGP-Key: 78695CFD
# Contributor: shivik <> PGP-Key: 761E423C
# Contributor: Michael Duell <mail@akurei.me> PGP-Key: 6EE23EBE

###########################################################################################################
#                                          Patch and Build Options
###########################################################################################################
_custom="no"		# "m":	custom config via menuconfig
			# "n":	custom config via nconfig
			# "x":	custom config via xconfig
			# "no":	nothing

_config="pkg"		# "local":	compile only probed modules(https://aur.archlinux.org/packages/modprobed-db/)
			# "nomod":	don't use modules(make localyesconfig)
			# "old":	make with old config (/proc/config.gz)
			# "pkg":	use this package's config

_akcs=""		# Append Kernel Custom String.Not working on some systems.
			# Use if you wnat to append a custom string to kernel version.
			# No risc if you have a backup kernel in case of boot failure.

_use_BFS="no"		# "yes":	Use BFS cpu scheduler.
			# "no":		Use CFS cpu scheduler.

_use_KSM="no"		# "yes":	Enable Kernel SamePage Merging (KSM).
			# "no":		Don't use Kernel SamePage Merging (KSM).

_use_32bit_pae="no"	# "yes": Use the PAE config for 32-bit
			# "no": Use normal 32-bit config
###########################################################################################################

pkgdesc='A desktop oriented kernel and modules with Liquorix patches'
__basekernel=4.5
_minor=1
pkgver=${__basekernel}.${_minor}
pkgrel=2
lqxrel=2
_kernelname=-lqx
pkgbase=linux-lqx
pkgname=('linux-lqx' 'linux-lqx-headers' 'linux-lqx-docs')
_lqxpatchname="${pkgver}-${lqxrel}.patch"
arch=('i686' 'x86_64')
license=('GPL2')
url="http://liquorix.net/"
if [ "$_custom" = "x" ]; then
   makedepends=('qt5-base' 'kmod' 'inetutils' 'bc')
else
   makedepends=('kmod' 'inetutils' 'bc')
fi
options=(!strip)
install='linux-lqx.install'
source=("http://www.kernel.org/pub/linux/kernel/v4.x/linux-${__basekernel}.tar.xz"
        "http://www.kernel.org/pub/linux/kernel/v4.x/linux-${__basekernel}.tar.sign"
        "http://liquorix.net/sources/${_lqxpatchname}.gz"
        "http://liquorix.net/sources/${__basekernel}/config.i386"
        "http://liquorix.net/sources/${__basekernel}/config.i386-pae"
        "http://liquorix.net/sources/${__basekernel}/config.amd64"
        "linux-lqx.preset")

sha512sums=('cb0d5f30baff37dfea40fbc1119a1482182f95858c883e019ee3f81055c8efbdb9dba7dfc02ebcc4216db38f03ece58688e69efc0fce1dade359af30bd5426de'
            'SKIP'
            '8953fcfea491bb98b53d6504b9f90a8c289f621ae7a701cb837195b41e18a97522fbd15df9b474b594d124c221aa4448aa4e780115bac9ebe776231c49c064ec'
            '72e503fb2ef8526e0f01c72c410438a75f0af1e5b15e136ad4ec88e57ac191df3bfcad6c424af390fb92a4ed9d1dfd59f076283929e88f343684f9efdc24e070'
            'f8183466ace0b0a82419139b53703e0a85fa6469fbd8df4ac397db046cb9f643f7104e1089166378d260e0baa3a5f33db858abe5262c9fa277899a1a2715dfd6'
            'f9c3a09519d3873535ffa1afc84c63c39dccfc4d9dfebc18746a82264a5fcfcc509c63257231ac145fbccfff422bc62a7ce2d2da36c763f4e5262990c08cbcf7'
            'fe4dcd7b5ec06ec3ec4aa631531469f58f6a7111e2d33affa98a1b8a8d230c5fa7e25ffdf770fe5ce61f249b0ec0ecd69df2858c4029acee0efaadff957858fe')
            
validpgpkeys=(
              'ABAF11C65A2970B130ABE3C479BE3E4300411886' # Linus Torvalds
             )



prepare() {
  KARCH=x86

  cd ${srcdir}/linux-${__basekernel}

  # Add Liquorix patches
  patch -Np1 -i ${srcdir}/$_lqxpatchname
  
    # Trying oldcfg if possible and if selected
  if [ "$_config" = "old" ]; then
    if [ -e /proc/config.gz ]; then
      zcat /proc/config.gz > ./.config
    else
      echo "WARNING: There's no /proc/config.gz... You cannot use the old config. Aborting..."
      exit 1
    fi         
  else
    if [ "$CARCH" = "x86_64" ]; then
      cat ../config.amd64 >./.config
    elif [ "${_use_32bit_pae}" = "yes" ]; then
      cat ../config.i386-pae >./.config
    else
      cat ../config.i386 >./.config
    fi
  fi

  if [ "${_kernelname}" != "" ]; then
    sed -i "s|CONFIG_LOCALVERSION=.*|CONFIG_LOCALVERSION=\"${_kernelname}\"|g" ./.config
    sed -i "s|CONFIG_LOCALVERSION_AUTO=.*|CONFIG_LOCALVERSION_AUTO=n|" ./.config
  fi

  #Enable BFS cpu scheduler in config
  if [ "${_use_BFS}" = "yes" ]; then
    sed -i -e 's/# CONFIG_SCHED_BFS is not set/CONFIG_SCHED_BFS=y/' ./.config
    sed -i '/CONFIG_SCHED_BFS=y/a \CONFIG_SCHED_BFS_AUTOISO=n' ./.config
  fi

  #Enable KSM (Kernel SamePage Merging)
  if [ "${_use_KSM}" = "yes" ]; then
    sed -i -e 's/# CONFIG_KSM is not set/CONFIG_KSM=y/' ./.config
    sed -i '/CONFIG_KSM=y/a \CONFIG_UKSM=y/n' ./.config
    sed -i '/CONFIG_UKSM=y/a \# CONFIG_KSM_LEGACY is not set' ./.config
  fi

  # set extraversion to pkgrel
  sed -ri "s|^(EXTRAVERSION =).*|\1 -${pkgrel}|" Makefile

  # don't run depmod on 'make install'. We'll do this ourselves in packaging
  sed -i '2iexit 0' scripts/depmod.sh

  # set sublevel to kernel minor version
  sed -ri "s|^(SUBLEVEL =).*|\1 ${_minor}|" Makefile

  msg "Running make prepare"
  make prepare

### Optionally load needed modules for the make localmodconfig
 # See https://aur.archlinux.org/packages/modprobed-db/
 if [ $_config = "local" ]; then
  msg "If you have modprobe_db installed, running it in recall mode now"
  if [ -e /usr/bin/modprobed_db ]; then
    [[ ! -x /usr/bin/sudo ]] && echo "Cannot call modprobe with sudo. Install via pacman -S sudo and configure to work with this user." && exit 1
    sudo /usr/bin/modprobed_db recall
 fi
  msg "Running Steven Rostedt's make localmodconfig now"
  make localmodconfig
 else
  yes "" | make config
 fi

 if [ $_config = "nomod" ]; then
  msg "Running localYESconfig now"
  make localyesconfig
 else
  yes "" | make config
 fi

  if [ $_custom = "m" ]; then
    msg "Running make menuconfig"
    make menuconfig
  fi

  if [ $_custom = "n" ]; then
    msg "Running make nconfig"
    make nconfig
  fi

  if [ $_custom = "x" ]; then
    msg "Running make xconfig"
    make xconfig
  fi
}

build() {
  cd ${srcdir}/linux-${__basekernel}
  msg "Starting build."
  make ${MAKEFLAGS} LOCALVERSION=${_append_kernel_custom_string} bzImage modules
}

package_linux-lqx() {
pkgdesc="A desktop oriented kernel and modules with Liquorix patches"
depends=('coreutils' 'linux-firmware' 'mkinitcpio>=0.8')
optdepends=('crda: to set the correct wireless channels of your country' 'nvidia-lqx: nVidia drivers for linux-lqx' 'linux-firmware: Firmware files for Linux')
backup=("etc/mkinitcpio.d/linux-lqx.preset")
install=linux-lqx.install

cd "${srcdir}/linux-${__basekernel}"

KARCH=x86

# get kernel version
_kernver="$(make LOCALVERSION=${_append_kernel_custom_string} kernelrelease)"
_basekernel=${_kernver%%-*}
_basekernel=${_basekernel%.*}

mkdir -p "${pkgdir}"/{lib/modules,lib/firmware,boot}
make LOCALVERSION=${_append_kernel_custom_string} INSTALL_MOD_PATH="${pkgdir}" modules_install
cp arch/$KARCH/boot/bzImage "${pkgdir}/boot/vmlinuz-linux-lqx"

############## add vmlinux
##############install -D -m644 vmlinux "${pkgdir}/usr/src/linux-${_kernver}/vmlinux"

# set correct depmod command for install
cp -f "${startdir}/${install}" "${startdir}/${install}.pkg"
true && install=${install}.pkg
sed \
	-e  "s/KERNEL_NAME=.*/KERNEL_NAME=-lqx/g" \
	-e  "s/KERNEL_VERSION=.*/KERNEL_VERSION=${_kernver}/g" \
	-i "${startdir}/linux-lqx.install"

# install fallback mkinitcpio.conf file and preset file for kernel
install -D -m644 "${srcdir}/linux-lqx.preset" "${pkgdir}/etc/mkinitcpio.d/linux-lqx.preset"

sed \
	-e "1s|'linux.*'|'linux-lqx'|" \
	-e "s|ALL_kver=.*|ALL_kver=\"/boot/vmlinuz-linux-lqx\"|g" \
	-e "s|default_image=.*|default_image=\"/boot/initramfs-linux-lqx.img\"|g" \
	-e "s|fallback_image=.*|fallback_image=\"/boot/initramfs-linux-lqx-fallback.img\"|g" \
	-i "${pkgdir}/etc/mkinitcpio.d/linux-lqx.preset"

# remove build and source links
rm -f "${pkgdir}"/lib/modules/${_kernver}/{source,build}
# remove the firmware
rm -rf "${pkgdir}/lib/firmware"
# gzip -9 all modules to save 100MB of space
find "${pkgdir}" -name '*.ko' -exec gzip -9 {} \;
# make room for external modules
ln -s "../extramodules-${_basekernel}${_kernelname:lqx}" "${pkgdir}/lib/modules/${_kernver}/extramodules"
# add real version for building modules and running depmod from post_install/upgrade
mkdir -p "${pkgdir}/lib/modules/extramodules-${_basekernel}${_kernelname:lqx}"
echo "${_kernver}" > "${pkgdir}/lib/modules/extramodules-${_basekernel}${_kernelname:lqx}/version"

# Now we call depmod...
depmod -b "$pkgdir" -F System.map "$_kernver"

# move module tree /lib -> /usr/lib
mkdir -p "${pkgdir}/usr"
mv "$pkgdir/lib" "$pkgdir/usr"

install -D -m644 vmlinux "${pkgdir}/usr/lib/modules/${_kernver}/build/vmlinux"
}

package_linux-lqx-headers() {
pkgdesc="Header files and scripts to build modules for linux-lqx."
depends=('linux-lqx')

install -dm755 "${pkgdir}/usr/lib/modules/${_kernver}"



cd "${srcdir}/linux-${__basekernel}"

KARCH=x86

# get kernel version
_kernver="$(make LOCALVERSION=${_append_kernel_custom_string} kernelrelease)"
_basekernel=${_kernver%%-*}
_basekernel=${_basekernel%.*}

install -D -m644 Makefile \
	"${pkgdir}/usr/lib/modules/${_kernver}/build/Makefile"
install -D -m644 kernel/Makefile \
	"${pkgdir}/usr/lib/modules/${_kernver}/build/kernel/Makefile"
install -D -m644 .config \
	"${pkgdir}/usr/lib/modules/${_kernver}/build/.config"

mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/include"

for i in acpi asm-generic config crypto drm generated keys linux math-emu \
	media net pcmcia scsi sound trace uapi video xen; do
	cp -a include/${i} "${pkgdir}/usr/lib/modules/${_kernver}/build/include/"
done

	# copy arch includes for external modules
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/x86"
	cp -a arch/x86/include "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/x86/"

	# copy files necessary for later builds, like nvidia and vmware
	cp Module.symvers "${pkgdir}/usr/lib/modules/${_kernver}/build"
	cp -a scripts "${pkgdir}/usr/lib/modules/${_kernver}/build"

	# fix permissions on scripts dir
	chmod og-w -R "${pkgdir}/usr/lib/modules/${_kernver}/build/scripts"
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/.tmp_versions"

	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/${KARCH}/kernel"

	cp arch/${KARCH}/Makefile "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/${KARCH}/"

	if [ "${CARCH}" = "i686" ]; then
		cp arch/${KARCH}/Makefile_32.cpu "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/${KARCH}/"
	fi

	cp arch/${KARCH}/kernel/asm-offsets.s "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/${KARCH}/kernel/"

	# add docbook makefile
	install -D -m644 Documentation/DocBook/Makefile \
	"${pkgdir}/usr/lib/modules/${_kernver}/build/Documentation/DocBook/Makefile"

	# add dm headers
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/md"
	cp drivers/md/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/md"

	# add inotify.h
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/include/linux"
	cp include/linux/inotify.h "${pkgdir}/usr/lib/modules/${_kernver}/build/include/linux/"

	# add wireless headers
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/net/mac80211/"
	cp net/mac80211/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/net/mac80211/"

	# add dvb headers for external modules
	# in reference to:
	# http://bugs.archlinux.org/task/9912
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/dvb-core"
	cp drivers/media/dvb-core/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/dvb-core/"
	# and...
	# http://bugs.archlinux.org/task/11194
	###
	### DO NOT MERGE OUT THIS IF STATEMENT
	### IT AFFECTS USERS WHO STRIP OUT THE DVB STUFF SO THE OFFICIAL ARCH CODE HAS A CP
	### LINE THAT CAUSES MAKEPKG TO END IN AN ERROR
	###
	if [ -d include/config/dvb/ ]; then
		mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/include/config/dvb/"
		cp include/config/dvb/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/include/config/dvb/"
	fi

	# add dvb headers for http://mcentral.de/hg/~mrec/em28xx-new
	# in reference to:
	# http://bugs.archlinux.org/task/13146
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/dvb-frontends/"
	cp drivers/media/dvb-frontends/lgdt330x.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/dvb-frontends/"
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/i2c/"
	cp drivers/media/i2c/msp3400-driver.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/i2c/"

	# add dvb headers
	# in reference to:
	# http://bugs.archlinux.org/task/20402
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/usb/dvb-usb"
	cp drivers/media/usb/dvb-usb/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/usb/dvb-usb/"
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/dvb-frontends"
	cp drivers/media/dvb-frontends/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/dvb-frontends/"
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/tuners"
	cp drivers/media/tuners/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/tuners/"

	# add xfs and shmem for aufs building
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/fs/xfs"
	mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/mm"

	# copy in Kconfig files
	for i in $(find . -name "Kconfig*"); do
		mkdir -p "${pkgdir}"/usr/lib/modules/${_kernver}/build/`echo ${i} | sed 's|/Kconfig.*||'`
		cp ${i} "${pkgdir}/usr/lib/modules/${_kernver}/build/${i}"
	done

	chown -R root.root "${pkgdir}/usr/lib/modules/${_kernver}/build"
	find "${pkgdir}/usr/lib/modules/${_kernver}/build" -type d -exec chmod 755 {} \;

	# strip scripts directory
	find "${pkgdir}/usr/lib/modules/${_kernver}/build/scripts" -type f -perm -u+w 2>/dev/null | while read binary ; do
	case "$(file -bi "${binary}")" in
	*application/x-sharedlib*) # Libraries (.so)
		/usr/bin/strip ${STRIP_SHARED} "${binary}";;
	*application/x-archive*) # Libraries (.a)
		/usr/bin/strip ${STRIP_STATIC} "${binary}";;
	*application/x-executable*) # Binaries
		/usr/bin/strip ${STRIP_BINARIES} "${binary}";;
	esac
	done
	
	# remove a files already in linux-lqx-docs package
        rm -f "${pkgdir}/usr/lib/modules/${_kernver}/build/Documentation/kbuild/Kconfig.recursion-issue-01"
        rm -f "${pkgdir}/usr/lib/modules/${_kernver}/build/Documentation/kbuild/Kconfig.recursion-issue-02"
        rm -f "${pkgdir}/usr/lib/modules/${_kernver}/build/Documentation/kbuild/Kconfig.select-break"


	 # remove unneeded architectures
	 rm -rf "${pkgdir}"/usr/lib/modules/${_kernver}/build/arch/{alpha,arc,arm,arm26,arm64,avr32,blackfin,c6x,cris,frv,h8300,hexagon,ia64,m32r,m68k,m68knommu,metag,mips,microblaze,mn10300,openrisc,parisc,powerpc,ppc,s390,score,sh,sh64,sparc,sparc64,tile,unicore32,um,v850,xtensa}
}


package_linux-lqx-docs() {
pkgdesc="Kernel hackers manual - HTML documentation that comes with the linux-lqx kernel"
depends=('linux-lqx' )



cd "${srcdir}/linux-${__basekernel}"

    KARCH=x86
    
    # get kernel version
_kernver="$(make LOCALVERSION=${_append_kernel_custom_string} kernelrelease)"
_basekernel=${_kernver%%-*}
_basekernel=${_basekernel%.*}

  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build"
  cp -al Documentation "${pkgdir}/usr/lib/modules/${_kernver}/build"
  find "${pkgdir}" -type f -exec chmod 4.5 {} \;
  find "${pkgdir}" -type d -exec chmod 755 {} \;

  # remove a file already in linux package
  rm -f "${pkgdir}/usr/lib/modules/${_kernver}/build/Documentation/DocBook/Makefile"
}

