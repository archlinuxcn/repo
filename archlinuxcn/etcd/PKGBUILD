# Maintainer: Andrew Crerar <crerar@archlinux.org>
# Contributor: guillaume alaux <guillaume at alaux dot net>
# Contributor: korjjj <korjjj+aur[at]gmail[dot]com>
# Contributor: xeross <contact at xeross dot me>
# Contributor: codekoala <codekoala at gmail dot com>

pkgname=etcd
pkgver=3.6.6
pkgrel=1
pkgdesc="A distributed, reliable key-value store for the most critical data of a distributed system."
url="https://github.com/etcd-io/etcd"
license=(Apache-2.0)
arch=(
  x86_64
  armv6h
  armv7h
  aarch64
)
makedepends=(
  git
  go
)
install="${pkgname}".install
backup=('etc/conf.d/etcd')
options=(!lto)
source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/etcd-io/${pkgname}/archive/v${pkgver}.tar.gz"
  10-EnvironmentFile.conf
  etcd.env
  etcd.sysusers
  etcd.tmpfiles
)
b2sums=('9b3e1e59ba21e27a8cb942781164a9f3bd40c53a9a5904faa971f921e901606138ff28aeac9f59ec864e3e9a32f14469aa2b8d6169381404ce7c19df53931f72'
        '754d5e84506b9aff7629b9b08743e609d8e9db5926d5dd1ef22366a2eeffd4b9e56903284c3b6081bc2a3035e75922a009174aa612517d93e0f6a48fd6345729'
        '71f207c4ef1643dc70eecea6bdba4dcd7226626813d2a9f3330059f1b9f78ea2d3607b8b15b67b1afec0d201b01c10f6db3267695118732621a05f967a56a65a'
        'd59f33f6f6d84ade2c5053fe920b6185e5ab39ba9a6fed36d5d6bbad6a03f2950ed19c41856d343f969c1046e8abd9497c12f028482d705a65e0439675408776'
        '7c9f2c672450bfc86b94c3aa2177e1a799c2e01ac9a42e11c0e52e9feecdbc1918e9fcfc1d7683912dcd86ee785132e8a54cb83fdcf3d0060d2ee243dc13fbff')

build() {
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

  cd "${pkgname}-${pkgver}"

  ./scripts/build.sh
}

package() {
  cd "${pkgname}-${pkgver}"

  install -Dvm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}"/LICENSE

  install -Dvm755 bin/etcd "${pkgdir}"/usr/bin/etcd
  install -Dvm755 bin/etcdctl "${pkgdir}"/usr/bin/etcdctl
  install -Dvm755 bin/etcdutl "${pkgdir}"/usr/bin/etcdutl

  install -Dvm644 "${srcdir}"/etcd.sysusers \
    "${pkgdir}/usr/lib/sysusers.d/${pkgname}".conf

  install -Dvm644 "${srcdir}"/etcd.tmpfiles \
    "${pkgdir}/usr/lib/tmpfiles.d/${pkgname}".conf

  install -Dvm644 "${srcdir}"/etcd.env "${pkgdir}/etc/conf.d/${pkgname}"

  install -Dvm644 contrib/systemd/"${pkgname}".service \
    "${pkgdir}/usr/lib/systemd/system/${pkgname}".service

  install -Dvm644 "${srcdir}"/10-EnvironmentFile.conf \
    "${pkgdir}/usr/lib/systemd/system/${pkgname}".service.d/10-EnvironmentFile.conf

  install -dvm755 "${pkgdir}/usr/share/doc/${pkgname}"
  cp -r Documentation/* "${pkgdir}/usr/share/doc/${pkgname}"/  

  install -m644 "${pkgname}".conf.yml.sample \
    "${pkgdir}/usr/share/doc/${pkgname}"/
}
