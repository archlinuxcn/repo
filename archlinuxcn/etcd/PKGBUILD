# Maintainer: Andrew Crerar <crerar@archlinux.org>
# Contributor: guillaume alaux <guillaume at alaux dot net>
# Contributor: korjjj <korjjj+aur[at]gmail[dot]com>
# Contributor: xeross <contact at xeross dot me>
# Contributor: codekoala <codekoala at gmail dot com>

pkgname=etcd
pkgver=3.4.13
pkgrel=1
pkgdesc='A highly-available key value store for shared configuration and service discovery.'
arch=('x86_64' 'armv6h' 'armv7h')
url='https://github.com/etcd-io/etcd'
license=('Apache')
makedepends=('go')
backup=('etc/conf.d/etcd')
install="${pkgname}".install
source=("${pkgname}"-"${pkgver}".tar.gz::https://github.com/etcd-io/"${pkgname}"/archive/v"${pkgver}".tar.gz
         10-EnvironmentFile.conf
         etcd.env)
sha512sums=('a348e46f8f543bb43691cea20a7bfa0b1ef8b642dacc1dd26ee6f999cd5dc4aced19bb1606ba447293056674dbec7f043cbf959188a8b5cdf1f0de3d0938e08d'
            'fa85d772929ea7e0a18bddd4b9c41d043a7f75e560eacfab67b979985e510dea694c332b5130570e47101c1ec5c25925872c6a581568390e7b141d9c6c26aae2'
            '040cee3c04dd5bb253415169d1f6f50bbccac10b687706c1b168184985c0c6c6cc67858f0c71d2ebb475891e54b370fa39b20ead5155658d01fac31d7d388324')

build() {
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

  cd "${srcdir}"/"${pkgname}"-"${pkgver}"

  # https://github.com/etcd-io/etcd/issues/12109
  go mod tidy

  ./build
}

package() {
  # binaries
  install -Dm755 "${srcdir}"/"${pkgname}"-"${pkgver}"/bin/etcd "${pkgdir}"/usr/bin/etcd
  install -Dm755 "${srcdir}"/"${pkgname}"-"${pkgver}"/bin/etcdctl "${pkgdir}"/usr/bin/etcdctl

  # Upstream systemd unit
  install -Dm644 "${srcdir}"/"${pkgname}"-"${pkgver}"/contrib/systemd/etcd.service "${pkgdir}"/usr/lib/systemd/system/"${pkgname}".service

  # Adding 'EnvironmentFile=-/etc/conf.d/etcd' option to the unit
  install -Dm644 "${srcdir}"/10-EnvironmentFile.conf "${pkgdir}"/usr/lib/systemd/system/"${pkgname}".service.d/10-EnvironmentFile.conf

  # env file itself
  install -Dm644 "${srcdir}"/etcd.env "${pkgdir}"/etc/conf.d/"${pkgname}"

  # License
  install -Dm644 "${srcdir}"/"${pkgname}"-"${pkgver}"/LICENSE "${pkgdir}"/usr/share/licenses/"${pkgname}"/LICENSE

  # Docs
  install -dm755 "${pkgdir}"/usr/share/doc/"${pkgname}"
  cp -r "${srcdir}"/"${pkgname}"-"${pkgver}"/Documentation/* "${pkgdir}"/usr/share/doc/"${pkgname}"/
  install -m644 "${srcdir}"/"${pkgname}"-"${pkgver}"/"${pkgname}".conf.yml.sample "${pkgdir}"/usr/share/doc/"${pkgname}"
}
