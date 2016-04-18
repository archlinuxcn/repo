# Maintainer: Maikel Wever <maikelwever@gmail.com>

pkgname=lxd
pkgver=2.0.0
pkgrel=1
pkgdesc="REST API, command line tool and OpenStack integration plugin for LXC."
arch=('x86_64')
url="https://github.com/lxc/lxd"
license=('APACHE')
depends=('go' 'lxc')
makedepends=('git')
options=('!strip' '!emptydirs')
optdepends=(
    'lvm2: for lvm2 support'
    'thin-provisioning-tools: for thin provisioning support'
    'btrfs-progs: for btrfs support'
    'linux-user-ns-enabled: kernel with CONFIG_USER_NS enabled'
)
source=(
    "https://github.com/lxc/$pkgname/archive/$pkgname-$pkgver.tar.gz"
    "lxd.service"
)
md5sums=('2a6bcb8e01bc21d1a376d2059eadf572'
         'b1780c0e01e404895e35ac277aa597c4')

_gourl=github.com/lxc/lxd


build() {
  mkdir -p $srcdir/src/${_gourl}
  cp -r --preserve=timestamps $srcdir/$pkgname-$pkgname-$pkgver/* $srcdir/src/${_gourl}/
  cd $srcdir/src/${_gourl}
  GOPATH="$srcdir" go get
  GOPATH="$srcdir" go build
  GOPATH="$srcdir" make
}

package() {
  install=lxd.install

  mkdir -p "$pkgdir/usr/bin"
  mkdir -p "$pkgdir/usr/lib/lxd/"
  mkdir -p "$pkgdir/usr/share/lxd/"

  install -p -m755 "$srcdir/bin/"* "$pkgdir/usr/bin"
  mv "$pkgdir/usr/bin/lxd-bridge-proxy" "$pkgdir/usr/lib/lxd/"

  install -p -m755 "$srcdir/src/$_gourl/lxd-bridge/lxd-bridge" "$pkgdir/usr/lib/lxd/"

  # Package license (if available)
  for f in LICENSE COPYING LICENSE.* COPYING.*; do
    if [ -e "$srcdir/src/$_gourl/$f" ]; then
      install -Dm644 "$srcdir/src/$_gourl/$f" \
        "$pkgdir/usr/share/licenses/$pkgname/$f"
    fi
  done

  install -D -m644 "${srcdir}/lxd.service" \
      "${pkgdir}/usr/lib/systemd/system/lxd.service"
}

# vim:set ts=2 sw=2 et:
