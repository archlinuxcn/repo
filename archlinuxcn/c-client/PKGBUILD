_pkgbase=imap
pkgname=c-client
pkgver=2007f
pkgrel=20
arch=('x86_64')
license=('APACHE')
url="https://github.com/uw-imap/imap"
makedepends=('pam' 'git')
source=("imap-src::git+https://github.com/uw-imap/imap.git#tag=patches-FD29-RPM"
        'c-client-2006k_GENTOO_amd64-so-fix.patch')
options=('staticlibs')
sha256sums=('SKIP'
            '77de7621946c69638295ac11275124d0c405a4c6ba284a068f9a96c4994f3184')

prepare() {
  cd "$srcdir/$_pkgbase-src"

  sed \
    -e "s:-g -fno-omit-frame-pointer -O6:\${CFLAGS}:" \
    -e "s:SSLDIR=/usr/local/ssl:SSLDIR=/usr:" \
    -e "s:SSLCERTS=\$(SSLDIR)/certs:SSLCERTS=/etc/ssl/certs:" \
    -i src/osdep/unix/Makefile

  patch -p1 -i "$srcdir/c-client-2006k_GENTOO_amd64-so-fix.patch"
}

build() {
  cd "$srcdir/$_pkgbase-src"
  CFLAGS+=" -ffat-lto-objects"
  # NOTE: if you wish to enforce SSL, use SSLTYPE=unix.nopwd

  yes "y" | make -j1 lnp EXTRAAUTHENTICATORS=gss PASSWDTYPE=pam SPECIALAUTHENTICATORS=ssl SSLTYPE=unix EXTRACFLAGS="${CFLAGS} -fPIC -lgssapi_krb5 -lkrb5 -lk5crypto -lcom_err -lpam" EXTRALDFLAGS="${LDFLAGS}"

}

package_imap() {
  pkgdesc="An IMAP/POP server"
  depends=('c-client')
  provides=('imap-server' 'pop3-server')
  conflicts=('courier-mta' 'courier-imap')
  backup=(etc/xinetd.d/{imap,ipop2,ipop3})
  install=imap.install

  cd "$srcdir/$_pkgbase-src"
  install -d "$pkgdir/usr/bin"
  install -D -m755 imapd/imapd "$pkgdir/usr/bin/imapd"
  install -D -m755 ipopd/ipop2d "$pkgdir/usr/bin/ipop2d"
  install -D -m755 ipopd/ipop3d "$pkgdir/usr/bin/ipop3d"

  # install xinetd.d configs
  install -D -m644 ../imap "$pkgdir/etc/xinetd.d/imap"
  install -D -m644 ../ipop2 "$pkgdir/etc/xinetd.d/ipop2"
  install -D -m644 ../ipop3 "$pkgdir/etc/xinetd.d/ipop3"
}

package_c-client() {
  pkgdesc="Imap client library"
  depends=('pam')

  cd "$srcdir/$_pkgbase-src"

  for i in c-client mail imap4r1 rfc822 linkage misc smtp nntp \
    osdep env_unix env fs ftl nl tcp sslio utf8 utf8aux; do
    install -D -m644 c-client/${i}.h "$pkgdir/usr/include/imap/${i}.h"
  done
  install -m644 c-client/linkage.c "$pkgdir/usr/include/imap/linkage.c"
  install -D -m644 c-client/c-client.a "$pkgdir/usr/lib/c-client.a"
  ln -sf c-client.a "$pkgdir/usr/lib/libc-client.a"

  install -D -m755 c-client/libc-client.so.1.0.0 "$pkgdir/usr/lib/libc-client.so.1.0.0"
  ln -sf /usr/lib/libc-client.so.1.0.0 "$pkgdir/usr/lib/libc-client.so.1"
  ln -sf /usr/lib/libc-client.so.1.0.0 "$pkgdir/usr/lib/libc-client.so"
}
