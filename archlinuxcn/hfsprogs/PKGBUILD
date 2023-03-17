# $Id: PKGBUILD 214848 2017-03-04 09:22:15Z arojas $
# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: Rustam Tsurik <rustam.tsurik@gmail.com>
# Contributor: Prashant Vaibhav <mercurysquad+arch@gmail.com>
# Contributor: Alessio 'mOLOk' Bolognino <themolok@gmail.com>
# Contributor: Rubin Simons <rubin@xs4all.nl>
# Fedora Team: https://src.fedoraproject.org/rpms/hfsplus-tools

pkgname=hfsprogs
pkgver=540.1.linux3
pkgrel=4
pkgdesc="User space utils for create and check Apple HFS/HFS+ filesystem"
arch=('x86_64')
depends=('openssl')
makedepends=('libbsd')
license=('custom:APSL')
url="http://www.opensource.apple.com/"
_checksum='0435afc389b919027b69616ad1b05709'
source=("https://src.fedoraproject.org/repo/pkgs/hfsplus-tools/diskdev_cmds-${pkgver}.tar.gz/${_checksum}/diskdev_cmds-${pkgver}.tar.gz"
        "https://src.fedoraproject.org/rpms/hfsplus-tools/raw/rawhide/f/hfsplus-tools-no-blocks.patch"
        "https://src.fedoraproject.org/rpms/hfsplus-tools/raw/rawhide/f/hfsplus-tools-learn-to-stdarg.patch"
        "https://src.fedoraproject.org/rpms/hfsplus-tools/raw/rawhide/f/apsl-2.0.txt"
        "https://src.fedoraproject.org/rpms/hfsplus-tools/raw/rawhide/f/hfsplus-tools-sysctl.patch"
        "ldflags_relro.patch")
sha256sums=('b01b203a97f9a3bf36a027c13ddfc59292730552e62722d690d33bd5c24f5497'
            'd78d883f9b485e58d40820595000a8c20ec12f4aff6ca424368b5d1c04b2fe5e'
            'fb6556be9af656f7a83841db6de92482c697a9d706145d4c6041b5e284bd2820'
            'e5881019d8766c1e88a5fe1dbca4ba40c78011d41fcb18f6e9f50df60182685b'
            '2ab3de8bb2d4e18dbda89590e32f0fbdbeb4541875ff5726d68cdc5ba25235b6'
            '1bc2a40c66c244f6273b3d102d00bbcf16bbbfc1c6dc4e33f3cc890349bb20f4')

prepare() {
  # Apply patches
  cd "diskdev_cmds-${pkgver}"
  patch -p1 -i "${srcdir}/hfsplus-tools-no-blocks.patch"
  patch -p1 -i "${srcdir}/hfsplus-tools-learn-to-stdarg.patch"
  patch -p0 -i "${srcdir}/ldflags_relro.patch"
  patch -p1 -i "${srcdir}/hfsplus-tools-sysctl.patch"
}

build() {
  cd "diskdev_cmds-${pkgver}"
  make -f Makefile
}

package() {
  cd "diskdev_cmds-${pkgver}"
  # Copy license file
  install -m 755 -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m 644 "${srcdir}/apsl-2.0.txt" "${pkgdir}/usr/share/licenses/${pkgname}/APSL"
  # Copy executable files
  install -m 755 -d "${pkgdir}/usr/bin"
  install -m 755 "newfs_hfs.tproj/newfs_hfs" "${pkgdir}/usr/bin/mkfs.hfsplus"
  install -m 755 "fsck_hfs.tproj/fsck_hfs" "${pkgdir}/usr/bin/fsck.hfsplus"
  # Copy man pages
  install -m 755 -d "${pkgdir}/usr/share/man/man8/"
  install -m 644 "newfs_hfs.tproj/newfs_hfs.8" "${pkgdir}/usr/share/man/man8/mkfs.hfsplus.8"
  install -m 644 "fsck_hfs.tproj/fsck_hfs.8" "${pkgdir}/usr/share/man/man8/fsck.hfsplus.8"
}
