# Maintainer: Xuanwo <xuanwo@archlinuxcn.org>
pkgname=tidb
pkgver=2.1.2
pkgrel=1
pkgdesc='A distributed HTAP database compatible with the MySQL protocol'
makedepends=('go' 'make' 'git')
arch=('x86_64')
url='https://github.com/pingcap/tidb'
license=('Apache')
provides=('tidb-server')
backup=(etc/tidb/tidb.toml)
depends=('tikv')
source=(tidb-${pkgver}.tar.gz::https://github.com/pingcap/tidb/archive/v${pkgver}.tar.gz
        tidb.service
        tidb-sysusers.conf
        tidb-tmpfiles.conf
        tidb.toml)
sha256sums=('414a3fda48e082405cf41bb5978451d0826125ab6e94642c9243657195b0c4e9'
            '22318c19bb89ff5a0852df5186cc1496214cd49f2264192413a326d1e8c93dc9'
            '2b147d80985e714d5f861baf76591104c07058b9b6fa573bf0676d675cf8fc20'
            '30ce83fbec8f102c30e438282bb5b18c026d08480f2386d68f1116c12481bf66'
            'a34a8ca1f13c965cc0e872fc671f377b64a80cc11225cd6359bf7415b4c86a06')

_gopkgname='github.com/pingcap/tidb'

prepare() {
  export GOPATH="$srcdir/build"
  rm -rf "$GOPATH/src/$_gopkgname"
  mkdir -p `dirname "$GOPATH/src/$_gopkgname"`
  mv -Tv "$srcdir/tidb-${pkgver}" "$GOPATH/src/$_gopkgname"
}

build() {
  export GOPATH="$srcdir/build"
  export PATH=$GOPATH/bin:$PATH
  export CGO_ENABLED=0

  cd $GOPATH/src/$_gopkgname

  # A workaround for https://github.com/pingcap/tidb/issues/8827
  rm go.sum

  GO111MODULE=on go build -o bin/tidb-server tidb-server/main.go
}

package() {
  # Install binary
  install -Dm755 "$srcdir/build/src/$_gopkgname/bin/tidb-server" "$pkgdir/usr/bin/tidb-server"
  # Install systemd service
  install -Dm644 "$srcdir/tidb.service" "$pkgdir/usr/lib/systemd/system/tidb.service"
  # Install sysusers
  install -Dm644 "$srcdir/tidb-sysusers.conf" "$pkgdir/usr/lib/sysusers.d/tidb.conf"
  # Install tmpfiles
  install -Dm644 "$srcdir/tidb-tmpfiles.conf" "$pkgdir/usr/lib/tmpfiles.d/tidb.conf"
  # Install default config
  install -Dm644 tidb.toml "$pkgdir/etc/tidb/tidb.toml"
}

# vim: ft=sh syn=sh et
