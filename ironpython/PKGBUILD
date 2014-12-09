# Maintainer: Michael Schubert <mschu.dev at gmail>
# Contributor: Di "thc_flow" Abel <nospam@weedsmoker.im>

pkgname=ironpython
pkgver=2.7.5
pkgrel=1
pkgdesc="Python implementation for the .NET framework"
arch=("any")
url="http://ironpython.net"
license=("Apache")
depends=('mono>=2.10.0')
makedepends=('xz')
options=('!strip' 'emptydirs' 'libtool')
source=("https://github.com/IronLanguages/main/archive/ipy-$pkgver.zip"
        site.patch)
md5sums=('25c3b8047702f923eaf47a1ebe9ea829'
         'dd484ca6dfe03277d8a13e7b1cfe6662')

prepare() {
    cd "$srcdir/main-ipy-$pkgver"
    sed -i "/TreatWarningsAsErrors/s|true|false|" Solutions/Common.proj
}

build() {
    cd "$srcdir/main-ipy-$pkgver"
    xbuild Solutions/IronPython.sln /p:Mono=true /p:Configuration="Release"
}

package() {
    mkdir -p "$pkgdir/"{opt/ipy,usr/bin}
    cp -r $srcdir/main-ipy-$pkgver/bin/Release/* "$pkgdir/opt/ipy"
    for bin in ipy ipy64 ipyw ipyw64; do
      echo -e "#!/bin/sh\nmono /opt/ipy/$bin.exe \$*" > "$pkgdir/usr/bin/$bin"
      chmod +x "$pkgdir/usr/bin/$bin"
    done
}
