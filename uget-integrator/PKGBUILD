#Maintainer : Sasasu <lizhaolong0123@gmail.com>
pkgname=uget-integrator
pkgdesc="Integrate uGet Download Manager"
arch=('any')
url="https://github.com/ugetdm/uget-integrator"
license=('GPL3')
depends=('python3' 'uget')
makedepends=()
pkgver=0.0.1
pkgrel=1
source=("uget-integrator-$pkgver::https://raw.githubusercontent.com/ugetdm/uget-integrator/v$pkgver/bin/uget-integrator")
conflicts=('uget-chrome-wrapper')
pkgdesc="Integrate uGet Download Manager with Google Chrome, Chromium, Vivaldi, Opera and Firefox"
md5sums=('83b3c8c2cacdd352d3625f6e3a8e8dd3')
optdepends=(
    'uget-integrator-chrome: native messaging hosts for Google Chrome'
    'uget-integrator-chromium: native messaging hosts for Chromium and Vivaldi'
    'uget-integrator-opera: native messaging hosts for Opera'
    'uget-integrator-firefox: native messaging hosts for Firefox'
)

build() {
    cd "$srcdir"
}

package(){
    cd "$srcdir"
    mkdir -p "$pkgdir/usr/bin"
    install -m755 "uget-integrator-$pkgver" "$pkgdir"/usr/bin/uget-integrator
}
