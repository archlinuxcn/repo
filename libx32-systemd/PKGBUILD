# $Id: PKGBUILD 153155 2015-12-13 09:59:26Z lcarlier $
# Maintainer: Dave Reisner <dreisner@archlinux.org>
# Maintainer: Tom Gundersen <teg@jklm.no>
# x32 Maintainer: Fantix King <fantix.king at gmail.com> 

pkgname=libx32-systemd
_pkgbasename=systemd
pkgver=228
pkgrel=1.1
pkgdesc="system and service manager (x32 ABI)"
arch=('x86_64')
url="http://www.freedesktop.org/wiki/Software/systemd"
license=('GPL2' 'LGPL2.1' 'MIT')
depends=('libx32-libgcrypt' 'libx32-xz' 'libx32-libcap' 'libx32-acl' 'libx32-libidn' 'libx32-gcc-libs' 'systemd')
makedepends=('libx32-gcc-libs' 'gcc-multilib-x32' 'libx32-libidn' 'libx32-glib2' 'intltool' 'gperf'
             'libx32-curl' 'libx32-bzip2' 'git')
source=("git://github.com/systemd/systemd.git#tag=v$pkgver")
md5sums=('SKIP')

prepare() {
  cd systemd
  git cherry-pick --no-commit -m1 0d8fdbb53ee68396617e0751c3d9cc44487077ec

  ./autogen.sh
}

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd systemd

  local timeservers=({0..3}.arch.pool.ntp.org)

  ./configure \
    --libexecdir=/usr/libx32 \
    --libdir=/usr/libx32 \
    --localstatedir=/var \
    --sysconfdir=/etc \
    --enable-compat-libs \
    --disable-audit \
    --disable-tests \
    --disable-ima \
    --disable-seccomp \
    --disable-pam \
    --disable-kmod \
    --disable-networkd \
    --disable-blkid \
    --disable-libiptc \
    --disable-lz4 \
    --disable-manpages \
    --without-python \
    --disable-libcryptsetup \
    --with-sysvinit-path= \
    --with-sysvrcnd-path= \
    --with-ntp-servers="${timeservers[*]}"

  make
}

package() {
  cd systemd
    
  make DESTDIR="$pkgdir" install
    
  rm -rf "${pkgdir}"/{etc,var}
  rm -rf "${pkgdir}"/usr/{bin,include,lib,share}

  install -m755 -d "${pkgdir}/usr/share/licenses"
  ln -s systemd "$pkgdir/usr/share/licenses/libx32-systemd"
}
