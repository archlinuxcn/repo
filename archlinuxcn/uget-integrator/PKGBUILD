#Maintainer : Sasasu <lizhaolong0123@gmail.com>
pkgname=uget-integrator
pkgdesc="Integrate uGet Download Manager"
arch=('any')
url="https://github.com/ugetdm/uget-integrator"
license=('GPL3')
depends=('python3' 'uget')
makedepends=()
pkgver=1.0.0
pkgrel=2
source=("uget-integrator-$pkgver::https://raw.githubusercontent.com/ugetdm/uget-integrator/v$pkgver/bin/uget-integrator")
replaces=('uget-chrome-wrapper')
conflicts=('uget-chrome-wrapper')
pkgdesc="Integrate uGet Download Manager with Google Chrome, Chromium, Vivaldi, Opera and Firefox"
md5sums=('3f30519362f94598ccf8085be9f9da3d')
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
