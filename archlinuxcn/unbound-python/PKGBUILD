# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Bruno Pagani <archange@archlinux.org>
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor: Hisato Tatekura <hisato_tatekura@excentrics.net>
# Contributor: Massimiliano Torromeo <massimiliano DOT torromeo AT google mail service>

_pkgname=unbound
pkgname=unbound-python
pkgver=1.13.2
pkgrel=1
pkgdesc="Validating, recursive, and caching DNS resolver, with Python bindings"
arch=(x86_64)
url="https://unbound.net/"
license=(BSD)
depends=("dnssec-anchors" "fstrm" "hiredis" "ldns" "libevent" "libnghttp2" "libsodium" "openssl" "python")
makedepends=(expat protobuf-c systemd python swig)
optdepends=(
  'expat: for unbound-anchor'
  'sh: for unbound-control-setup'
  'python: python-bindings'
)
provides=("libunbound.so" "unbound=$pkgver")
backup=(etc/${_pkgname}/${_pkgname}.conf)
source=("https://unbound.net/downloads/${_pkgname}-${pkgver}.tar.gz"{,.asc}
        "${_pkgname}-1.13.2-fix_libpython_linking.patch"
        ${_pkgname}-sysusers.conf
        ${_pkgname}-tmpfiles.conf
        ${_pkgname}-trusted-key.hook)
sha512sums=('1e89441446e7a25c6a49bded645f8b348c1758c3be54e3a986041cb1f00c45d152fd469dc52666fb820574db9d51b16f1627dc8afcb9519508d4833ca358191a'
            'SKIP'
            '836ec61c79f91e429feed7fca7b8df64c0233aa621b3c49011ad39854b231bbc7ab73408785278b0b8b7d1038bd2c9c57548d973ce796cccdb575307ff5318c6'
            'ef71d4e9b0eb0cc602d66bd0573d9424578fe33ef28a852c582d56f0fd34fdd63046c365ef7aed8b84a461b81254240af7ad3fd539da72f9587817d21bd6c585'
            '6b1849ae9d7cf427f6fa6cd0590e8f8c3f06210d2d6795e543b0f325a9e866db0f5db2275a29fa90f688783c0dd16f19c8a49a9817d5f5444e13f8f2df3ff712'
            '613826cdf5ab6e77f2805fa2aa65272508dcd11090add1961b3df6dfac3b67db016bc9f45fbcf0ef0de82b2d602c153d5263a488027a6cf13a72680b581b266d')
b2sums=('71806edc86b323ff1f9f2d7bd3f699b15da2cd1cfefe9ca6008d74915dd6c7b45690026fb0244531ae563a3ca1b142f21fc8aed97ba4bb0015d8ab9196ff045a'
        'SKIP'
        'b2b7f27f1d339ea8ded8733cb71cbdb0d4b11c925a412fe78a0848c80fa401fc381a1c041b85879999a2c3f273021e6ff0bd748af479d914df2eb4b94614b821'
        '292a3c2e5fde292a03b6c9b2ddabd5089f52e73b50a404c3d9f54c1a43184924b661a21eea61cc521c594c1005a3b40b630fa585a38195c61298f9b24b248b92'
        'd3951006b43068be904c6b91a9e0563d56228225854e12b40abbdd4ba9b47338e97265837297a6de879acbc8051bb749163f9457683f5e12fc29ac2e7b687fd3'
        'd28785390eb6c125bd26ca11f097fe8864b080482157deeb7c70e9bee47ff2844abaed574db59a7c152ed3ec0acba05cfee4c3751f7a9f553320b064578f86c7')
validpgpkeys=(EDFAA3F2CA4E6EB05681AF8E9F6F1C2D7E045F8D) # W.C.A. Wijngaards <wouter@nlnetlabs.nl>

prepare() {
  cd ${_pkgname}-${pkgver}
  # set default location of trusted-key.key
  sed '/# trust-anchor-file:/c\\ttrust-anchor-file: /etc/unbound/trusted-key.key' \
    -i doc/example.conf.in
  # backport https://github.com/NLnetLabs/unbound/pull/511
  patch -Np1 -i ../"${_pkgname}-1.13.2-fix_libpython_linking.patch"

  autoreconf -vfi
}

build() {
  cd ${_pkgname}-${pkgver}
  ./configure --prefix=/usr \
              --sysconfdir=/etc \
              --localstatedir=/var \
              --sbindir=/usr/bin \
              --disable-rpath \
              --enable-dnscrypt \
              --enable-dnstap \
              --enable-pie \
              --enable-relro-now \
              --enable-subnet \
              --enable-systemd \
              --enable-tfo-client \
              --enable-tfo-server \
              --enable-cachedb \
              --with-libhiredis \
              --with-conf-file=/etc/unbound/unbound.conf \
              --with-pidfile=/run/unbound.pid \
              --with-rootkey-file=/etc/trusted-key.key \
              --with-libevent \
              --with-libnghttp2 \
              --with-pyunbound --with-pythonmodule
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

check() {
  cd ${_pkgname}-${pkgver}
  make -k check
}

package() {
  depends+=(libprotobuf-c.so libsystemd.so)
  cd ${_pkgname}-${pkgver}
  make DESTDIR="${pkgdir}" install
  install -vDm 644 contrib/${_pkgname}.service -t "${pkgdir}"/usr/lib/systemd/system/
  install -vDm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/${_pkgname}/
  cd ..
  install -vDm 644 ${_pkgname}-sysusers.conf "${pkgdir}"/usr/lib/sysusers.d/${_pkgname}.conf
  install -vDm 644 ${_pkgname}-tmpfiles.conf "${pkgdir}"/usr/lib/tmpfiles.d/${_pkgname}.conf
  # libalpm hook to copy the dnssec-anchors provided key to /etc/unbound
  install -vDm 644 unbound-trusted-key.hook -t "${pkgdir}"/usr/share/libalpm/hooks/
}
conflicts=("unbound")
