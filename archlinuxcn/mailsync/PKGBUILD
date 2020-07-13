# Maintainer: Adrián Pérez de Castro <aperez@igalia.com>
_imapver='2007f'
pkgname=mailsync
pkgdesc='Synchronizes a collection of mailboxes using a 3-way diff'
url=http://mailsync.sourceforge.net/
pkgver=5.2.1
pkgrel=2
license=(GPL)
arch=(x86_64 i686)
depends=(pam)
options=(zipman)
source=("http://downloads.sourceforge.net/project/${pkgname}/${pkgname}/${pkgver}/${pkgname}_${pkgver}.orig.tar.gz"
        "http://ftp.ntua.gr/pub/net/mail/imap/imap-${_imapver}.tar.gz"
        1006_openssl1.1_autoverify.patch
        c-client-2006k_GENTOO_amd64-so-fix.patch)
sha512sums=('9282cbb6a4ed70ac003ceeace933fda92da3fd6f5bf1058016c138cd81f29918c59ceed615a8f05761f3fd1b32c5b04a0087116cbb75ecf56b8d66ab2c47d14b'
            '7c3e1d9927872001e768ff2ddbcf3af74078243efe58dd70e01d966856b7611134e4b579818691a954bade9acaeeda6f2f30f40d812b8aa20990de5cb90d5d35'
            '7ecbe52adc6e3d1deee05790745642f794150ffaebf51c0cf689dc036eea9c7d80e643648aac37bf0aa83ac138b8bb63abfad3b540bc9440de3456162dfabae5'
            '213f06e133704ed2bb9fc6900edb7a4505bf6965409ecf76502bf9cafdf7c981bca552479f8ffaa1a355d2f1c1c08dbe0453fa5bce06590f6627d0e622c70879')

prepare () {
  cd "${srcdir}/imap-${_imapver}"

  # Straight out of the "imap" PKGBUILD.
  sed \
    -e "s:-g -fno-omit-frame-pointer -O6:\${CFLAGS}:" \
    -e "s:SSLDIR=/usr/local/ssl:SSLDIR=/usr:" \
    -e "s:SSLCERTS=\$(SSLDIR)/certs:SSLCERTS=/etc/ssl/certs:" \
    -i src/osdep/unix/Makefile

  patch -p1 -i "${srcdir}/c-client-2006k_GENTOO_amd64-so-fix.patch"
  patch -p1 -i "${srcdir}/1006_openssl1.1_autoverify.patch"
}

build () {
  # Ditto, from the "imap" PKGBUILD.
  cd "${srcdir}/imap-${_imapver}"
  yes "y" | make lnp EXTRAAUTHENTICATORS=gss PASSWDTYPE=pam SPECIALAUTHENTICATORS=ssl SSLTYPE=unix EXTRACFLAGS="${CFLAGS} -fPIC -lgssapi_krb5 -lkrb5 -lk5crypto -lcom_err -lpam" EXTRALDFLAGS="${LDFLAGS}"

  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --with-c-client="${srcdir}/imap-${_imapver}" \
  	--prefix=/usr --sysconfdir=/etc --with-openssl
  make
}

package () {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make install DESTDIR="${pkgdir}"

  # Move manual page to a proper location
  install -m755 -d "${pkgdir}/usr/share/man/man1"
  mv "${pkgdir}/usr/share/doc/mailsync/mailsync.1" \
     "${pkgdir}/usr/share/man/man1"
}
