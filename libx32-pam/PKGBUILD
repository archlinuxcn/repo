# Upstream Maintainer: jtts
# Contributor: josephgbr <rafael.f.f1 at gmail.com> 
# Contributor: Janax <janax99@yahoo.com>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>
# Contributor: judd <jvinet@zeroflux.org>
# Maintainer: Fantix King <fantix.king at gmail.com> 

_pkgbasename=pam
pkgname=libx32-${_pkgbasename}
pkgver=1.1.8
pkgrel=5
pkgdesc="PAM (Pluggable Authentication Modules) library (x32 ABI)"
arch=('x86_64')
license=('GPL2')
url="http://linux-pam.org"
depends=(libx32-cracklib libx32-libtirpc $_pkgbasename) # pambase libx32-glibc
makedepends=('libx32-flex' 'gcc-multilib-x32') # w3m docbook-xml>=4.4 docbook-xsl
#backup=(etc/security/{access.conf,group.conf,limits.conf,namespace.conf,namespace.init,pam_env.conf,time.conf} etc/default/passwd etc/environment)
source=(https://fedorahosted.org/releases/l/i/linux-pam/Linux-PAM-$pkgver.tar.bz2
        ftp://ftp.archlinux.org/other/pam_unix2/pam_unix2-2.9.1.tar.bz2
        pam_unix2-glibc216.patch
        pam-1.1.8-cve-2013-7041.patch
        pam-1.1.8-cve-2014-2583.patch)
sha256sums=('c4b1f23a236d169e2496fea20721578d864ba00f7242d2b41d81050ac87a1e55'
            '3315747699fece4e1cc5771885d243b3e017c4c4ca1326e86228d590a840e955'
            '6644c5cff46878c65bdc77977becbeda392675702264bfcc7c610a45a9982574'
            '18034730d74f67c79feb2c6abc796442c0c548ce221b8e9d633e98a7bd3cce2c'
            'b10255f690f9f4a8cec044383d9cd03031b9a7be9892d824b2adc451d6d06f65')
options=('!emptydirs')

prepare () {
  cd $srcdir/Linux-PAM-$pkgver
  # fix CVEs in pam
  patch -Np1 -i  "${srcdir}/pam-1.1.8-cve-2013-7041.patch"
  patch -Np1 -i  "${srcdir}/pam-1.1.8-cve-2014-2583.patch"

  # fix pam_unix2 building
  cd $srcdir/pam_unix2-2.9.1
  patch -Np1 -i "${srcdir}/pam_unix2-glibc216.patch"
}

build() {
  export CC='gcc -mx32'
  export CXX='g++ -mx32'
  export PKG_CONFIG_PATH='/usr/libx32/pkgconfig'
  
  cd $srcdir/Linux-PAM-$pkgver
  ./configure --libdir=/usr/libx32 --sbindir=/usr/bin --with-xml-catalog=no --disable-db
  make

  cd $srcdir/pam_unix2-2.9.1
  # modify flags to build against the pam compiled here, not a system lib.
  ./configure \
      CFLAGS="$CFLAGS -I$srcdir/Linux-PAM-$pkgver/libpam/include/" \
      LDFLAGS="$LDFLAGS -L$srcdir/Linux-PAM-$pkgver/libpam/.libs/" \
      --libdir=/usr/libx32 \
      --sbindir=/usr/bin
  make
}

package() {
  cd $srcdir/Linux-PAM-$pkgver
  make DESTDIR=$pkgdir SCONFIGDIR=/etc/security install

  # build pam_unix2 module
  # source ftp://ftp.suse.com/pub/people/kukuk/pam/pam_unix2
  cd $srcdir/pam_unix2-2.9.1
  #make DESTDIR=$pkgdir install
  install src/pam_unix2.so $pkgdir/usr/libx32/security/pam_unix2.so

  # add the realtime permissions for audio users
  #sed -i 's|# End of file||' $pkgdir/etc/security/limits.conf
  #cat >>$pkgdir/etc/security/limits.conf <<_EOT
#*               -       rtprio          0
#*               -       nice            0
#@audio          -       rtprio          65
#@audio          -       nice           -10
#@audio          -       memlock         40000
#_EOT

  # fix some missing symlinks from old pam for compatibility
  cd $pkgdir/usr/libx32/security
  ln -s pam_unix.so pam_unix_acct.so
  ln -s pam_unix.so pam_unix_auth.so
  ln -s pam_unix.so pam_unix_passwd.so
  ln -s pam_unix.so pam_unix_session.so

  # set unix_chkpwd uid
  #chmod +s $pkgdir/usr/bin/unix_chkpwd

  # cleanup for libx32 package
  rm -rf "${pkgdir}"/{etc,usr/{include,share,bin}}
}
