# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Bruno Pagani <archange@archlinux.org>
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor: Hisato Tatekura <hisato_tatekura@excentrics.net>
# Contributor: Massimiliano Torromeo <massimiliano DOT torromeo AT google mail service>

_pkgname=unbound
pkgname=unbound-python
pkgver=1.17.0
pkgrel=1
pkgdesc="Validating, recursive, and caching DNS resolver, with Python bindings"
arch=(x86_64)
url="https://unbound.net/"
license=(BSD)
depends=(dnssec-anchors fstrm hiredis ldns libevent libnghttp2 libsodium openssl python)
makedepends=(expat protobuf-c swig systemd)
optdepends=(
  'expat: for unbound-anchor'
  'sh: for unbound-control-setup'
)
provides=("libunbound.so" "unbound=$pkgver")
conflicts=("unbound")
backup=(etc/${_pkgname}/${_pkgname}.conf)
source=(
  "https://unbound.net/downloads/${_pkgname}-${pkgver}.tar.gz"{,.asc}
  "${_pkgname}-1.14.0-trust_anchor_file.patch"
  ${_pkgname}-sysusers.conf
  ${_pkgname}-tmpfiles.conf
  ${_pkgname}-trusted-key.hook
)
sha512sums=('f6b9f279330fb19b5feca09524959940aad8c4e064528aa82b369c726d77e9e8e5ca23f366f6e9edcf2c061b96f482ed7a2c26ac70fc15ae5762b3d7e36a5284'
            'SKIP'
            '9590d3d459d96f99cbc7482fae0f5318dd22a034e45cff18079e4f3c9f9c3c1d7af90cdd5353fb469eac08c535555fd164097b496286b807b2117e8a3a6cd304'
            'ef71d4e9b0eb0cc602d66bd0573d9424578fe33ef28a852c582d56f0fd34fdd63046c365ef7aed8b84a461b81254240af7ad3fd539da72f9587817d21bd6c585'
            '6b1849ae9d7cf427f6fa6cd0590e8f8c3f06210d2d6795e543b0f325a9e866db0f5db2275a29fa90f688783c0dd16f19c8a49a9817d5f5444e13f8f2df3ff712'
            '613826cdf5ab6e77f2805fa2aa65272508dcd11090add1961b3df6dfac3b67db016bc9f45fbcf0ef0de82b2d602c153d5263a488027a6cf13a72680b581b266d')
b2sums=('611c1b96ff84e6dd8f7a592135cc17f416cd810d0f35d27c8cedd56af069badd8dca112cc5927a1fe50ec3335c377b6bd6fc4e1a6d63a332a90d676e3c23dcef'
        'SKIP'
        '0978ab5c0474ed29de9c0904a46d114413e094dafeadaac4f10cdbc19e4152fcc064d7cdb8c331da7c2531075aa699326b84e21da1a8218a6f00a10f0e107b3d'
        '292a3c2e5fde292a03b6c9b2ddabd5089f52e73b50a404c3d9f54c1a43184924b661a21eea61cc521c594c1005a3b40b630fa585a38195c61298f9b24b248b92'
        'd3951006b43068be904c6b91a9e0563d56228225854e12b40abbdd4ba9b47338e97265837297a6de879acbc8051bb749163f9457683f5e12fc29ac2e7b687fd3'
        'd28785390eb6c125bd26ca11f097fe8864b080482157deeb7c70e9bee47ff2844abaed574db59a7c152ed3ec0acba05cfee4c3751f7a9f553320b064578f86c7')
validpgpkeys=(EDFAA3F2CA4E6EB05681AF8E9F6F1C2D7E045F8D) # W.C.A. Wijngaards <wouter@nlnetlabs.nl>

prepare() {
  # borrowed from community/hyperkitty
  local python_stdlib_basepath="$(python -c "from sysconfig import get_path; print(get_path('stdlib'))")"

  cd ${_pkgname}-${pkgver}
  # enable trusted-anchor-file and set it to an unbound specific location
  patch -Np1 -i ../"${_pkgname}-1.14.0-trust_anchor_file.patch"
  # Not sure if there is a way to patch autoconf - this line should exist only when --with-pythonmodule
  echo BindReadOnlyPaths=$python_stdlib_basepath:/etc/unbound$python_stdlib_basepath >> contrib/${_pkgname}.service.in
  autoreconf -fiv
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
              --with-pyunbound \
              --with-pythonmodule
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
  install -vDm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}/
  install -vDm 644 ../${_pkgname}-sysusers.conf "${pkgdir}"/usr/lib/sysusers.d/${_pkgname}.conf
  install -vDm 644 ../${_pkgname}-tmpfiles.conf "${pkgdir}"/usr/lib/tmpfiles.d/${_pkgname}.conf
  # libalpm hook to copy the dnssec-anchors provided key to /etc/unbound
  install -vDm 644 ../unbound-trusted-key.hook -t "${pkgdir}"/usr/share/libalpm/hooks/

  python -m compileall -s "$pkgdir" -p / "$pkgdir"/usr/lib
}
