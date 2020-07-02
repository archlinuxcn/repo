# Maintainer: Xuanwo <xuanwo@archlinuxcn.org>
# Maintainer: Allen Zhong <zhongbenli@pingcap.com>
pkgname=tikv-pd
pkgver=4.0.2
pkgrel=2
pkgdesc='Manage and schedule the TiKV cluster.'
makedepends=('go' 'make' 'git' 'unzip')
arch=('x86_64')
url='https://github.com/pingcap/pd'
license=('Apache')
provides=('pd-server')
backup=(etc/pd/pd.toml)
install=pd.install
source=(pd-${pkgver}.tar.gz::https://github.com/pingcap/pd/archive/v${pkgver}.tar.gz
        pd.service
        pd-sysusers.conf
        pd-tmpfiles.conf
        pd.toml)
sha256sums=('5b08661eafabe27671760de44f898625eebfdc4a5052fe1615e02ad78c67b18f'
            'b03d12f2f8d6eb2e9d654d6258ca39000225cdf1418840f7e35081631bc4d924'
            '5edd250ba9e70a4f8d27581ed658f0fbfeca58ca62429dec12bb5fffc0919b67'
            '15633aaa2d7726375112a1b5af88105878f09c176a542cde6d0e5f0c4eee4495'
            'dd3097d7f72da151d792894d2f3bb4188bfe9d445df8955d0f6f9b5c36980249')

_gopkgname='github.com/pingcap/pd'

prepare() {
  export GOPATH="$srcdir/build"
  rm -rf "$GOPATH/src/$_gopkgname"
  mkdir -p `dirname "$GOPATH/src/$_gopkgname"`
  mv -Tv "$srcdir/pd-${pkgver}" "$GOPATH/src/$_gopkgname"

  # patch Makefile
  sed -i 's/go build/go build $(GOFLAGS)/g' "$GOPATH/src/$_gopkgname/Makefile"
  sed -i 's/CGO_ENABLED=0/CGO_ENABLED=1/g' "$GOPATH/src/$_gopkgname/Makefile"
  sed -i 's/BUILD_CGO_ENABLED := 0/BUILD_CGO_ENABLED := 1/g' "$GOPATH/src/$_gopkgname/Makefile"
  sed -i '/shell git /d' "$GOPATH/src/$_gopkgname/Makefile"
}

build() {
  export GOPATH="$srcdir/build"
  export PATH=$GOPATH/bin:$PATH
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

  cd $GOPATH/src/$_gopkgname

  _LDFLAGS="-X $_gopkgname/v4/server.PDReleaseVersion=$pkgver -X $_gopkgname/v4/server.PDGitBranch=release -X $_gopkgname/v4/server.PDGitHash=v$pkgver"

  LDFLAGS=$_LDFLAGS make build tools
}

package() {
  # Install binary
  install -Dm755 "$srcdir/build/src/$_gopkgname/bin/pd-server" "$pkgdir/usr/bin/pd-server"
  install -Dm755 "$srcdir/build/src/$_gopkgname/bin/pd-ctl" "$pkgdir/usr/bin/pd-ctl"
  install -Dm755 "$srcdir/build/src/$_gopkgname/bin/pd-tso-bench" "$pkgdir/usr/bin/pd-tso-bench"
  install -Dm755 "$srcdir/build/src/$_gopkgname/bin/pd-recover" "$pkgdir/usr/bin/pd-recover"
  install -Dm755 "$srcdir/build/src/$_gopkgname/bin/pd-analysis" "$pkgdir/usr/bin/pd-analysis"
  install -Dm755 "$srcdir/build/src/$_gopkgname/bin/pd-heartbeat-bench" "$pkgdir/usr/bin/pd-heartbeat-bench"

  # Install systemd service
  install -Dm644 "$srcdir/pd.service" "$pkgdir/usr/lib/systemd/system/pd.service"
  # Install sysusers
  install -Dm644 "$srcdir/pd-sysusers.conf" "$pkgdir/usr/lib/sysusers.d/pd.conf"
  # Install tmpfiles
  install -Dm644 "$srcdir/pd-tmpfiles.conf" "$pkgdir/usr/lib/tmpfiles.d/pd.conf"
  # Install default pd config
  install -Dm644 pd.toml "$pkgdir/etc/pd/pd.toml"
}

# vim: ft=sh syn=sh et
