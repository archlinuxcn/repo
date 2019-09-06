# Maintainer: Maikel Wever <maikelwever@gmail.com>
# based on lxd-git package https://aur.archlinux.org/packages/lxd-git/
# which in turn is based based on old version of this very package
# Contributor: Asterios Dimitriou <asterios@pci.gr>
# Contributor: Benjamin Asbach <archlinux-aur.lxd@impl.it>
# Contributer: nightuser <nightuser.android at gmail.com>

pkgname=lxd
_pkgname=lxd
pkgver=3.17
pkgrel=1
pkgdesc="REST API, command line tool and OpenStack integration plugin for LXC."
arch=('x86_64')
url="https://github.com/lxc/lxd"
license=('APACHE')
conflicts=('lxd-git' 'lxd-lts')
provides=('lxd')
depends=('lxc' 'squashfs-tools' 'dnsmasq' 'libuv')
makedepends=('go' 'git' 'tcl' 'patchelf')
optdepends=(
    'lvm2: for lvm2 support'
    'thin-provisioning-tools: for thin provisioning support'
    'btrfs-progs: for btrfs storage driver support'
    'ceph: for ceph storage driver support'
    'lxcfs: for lxcfs support'
)
options=('!strip' '!emptydirs')

_lxd=github.com/lxc/lxd

source=(
    "https://${_lxd}/releases/download/${pkgname}-${pkgver}/${pkgname}-${pkgver}.tar.gz"
    "lxd.service"
    "lxd.socket"
    "dnsmasq-lxd.conf"
    "dnsmasq@lxd.service"
    "lxd.netctl"
    "dbus-dnsmasq-lxd.conf"
    "networkmanager-dnsmasq-lxd.conf"
)

md5sums=('fb2bd541ece52f06a22e6486b5a2dc4b'
         '6462095d5892d15c4f14310aa263a2a9'
         '1fb28d8dfe82af71d0675c8e9a0a7293'
         'b1fd16933c1b24aaa9ccc8f5a0e6478c'
         '15ae1bc51684d611bded2839ca55a37b'
         '52c641ea0ba5477f5c1a1b857c03dda9'
         'c86b8c441ab014340186acc7799096f2'
         '427926fddb1537f7a65d0a7274106df5')

build() {
  export GOPATH="${srcdir}/${pkgname}-${pkgver}/_dist"
  cd "${GOPATH}/src/${_lxd}"
  make deps
  export CGO_CFLAGS="-I${GOPATH}/deps/sqlite/ -I${GOPATH}/deps/libco/ -I${GOPATH}/deps/raft/include/ -I${GOPATH}/deps/dqlite/include/"
  export CGO_LDFLAGS="-L${GOPATH}/deps/sqlite/.libs/ -L${GOPATH}/deps/libco/ -L${GOPATH}/deps/raft/.libs -L${GOPATH}/deps/dqlite/.libs/"
  export LD_LIBRARY_PATH="${GOPATH}/deps/sqlite/.libs/:${GOPATH}/deps/libco/:${GOPATH}/deps/raft/.libs/:${GOPATH}/deps/dqlite/.libs/"
  make
}

package() {
  go_path="${srcdir}/${pkgname}-${pkgver}/_dist"
  go_bin_dir="${go_path}/bin"
  go_deps_dir="${go_path}/deps"
  install=lxd.install
  mkdir -p "${pkgdir}/usr/bin"
  mkdir -p "${pkgdir}/usr/lib/lxd"
  mkdir -p "${pkgdir}/usr/share/doc/lxd"
  mkdir -p "${pkgdir}/usr/share/bash-completion/completions"
  install -p -m755 "${go_bin_dir}/"* "${pkgdir}/usr/bin"
  patchelf --set-rpath "/usr/lib/lxd" "${pkgdir}/usr/bin/lxd"
  cp --no-dereference --preserve=timestamps \
    "${go_deps_dir}/sqlite/.libs/"libsqlite3.so* \
    "${go_deps_dir}/libco/"libco.so* \
    "${go_deps_dir}/raft/.libs/"libraft.so* \
    "${go_deps_dir}/dqlite/.libs/"libdqlite.so* \
    "${pkgdir}/usr/lib/lxd"
  patchelf --set-rpath "/usr/lib/lxd" "${pkgdir}/usr/lib/lxd/libdqlite.so"

  # Package license
  install -Dm644 "${go_path}/src/${_lxd}/COPYING"  "${pkgdir}/usr/share/licenses/${_pkgname}/LICENCE"

  # systemd files
  install -D -m644 "${srcdir}/lxd.service" \
    "${pkgdir}/usr/lib/systemd/system/lxd.service"
  install -D -m644 "${srcdir}/lxd.socket" \
    "${pkgdir}/usr/lib/systemd/system/lxd.socket"

  # documentation
  install -D -m644 "${go_path}/src/${_lxd}/doc/"* \
    "${pkgdir}/usr/share/doc/lxd/"

  # Bash completions
  install -p -m644 "${go_path}/src/${_lxd}/scripts/bash/lxd-client" \
    "${pkgdir}/usr/share/bash-completion/completions/lxd"

  # Example configuration files
  mkdir -p "${pkgdir}/usr/share/lxd/"
  mkdir -p "${pkgdir}/usr/share/lxd/systemd/system/"
  mkdir -p "${pkgdir}/usr/share/lxd/netctl/"
  mkdir -p "${pkgdir}/usr/share/lxd/dbus-1/system.d/"
  mkdir -p "${pkgdir}/usr/share/lxd/NetworkManager/dnsmasq.d/"

  install -Dm644 "${srcdir}/dnsmasq-lxd.conf" \
    "${pkgdir}/usr/share/lxd/dnsmasq-lxd.conf"
  install -Dm644 "${srcdir}/dnsmasq@lxd.service" \
    "${pkgdir}/usr/share/lxd/systemd/system/dnsmasq@lxd.service"
  install -Dm644 "${srcdir}/lxd.netctl" \
    "${pkgdir}/usr/share/lxd/netctl/lxd"
  install -Dm644 "${srcdir}/dbus-dnsmasq-lxd.conf" \
    "${pkgdir}/usr/share/lxd/dbus-1/system.d/dnsmasq-lxd.conf"
  install -Dm644 "${srcdir}/networkmanager-dnsmasq-lxd.conf" \
    "${pkgdir}/usr/share/lxd/NetworkManager/dnsmasq.d/lxd.conf"
}

# vim:set ts=2 sw=2 et:
