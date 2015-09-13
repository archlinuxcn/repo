# Maintainer: Joel Teichroeb <joel@teichroeb.net>
# Contributor: Matthias Maennich < arch .at. maennich.net >
# Contributor: bruce < b_a_g99 .at. hotmail.com >
# Contributor: carstene1ns <arch carsten-teibes de>

pkgname=dropbox-cli
pkgver=2015.02.12
pkgrel=1
pkgdesc='Command line interface for dropbox'
arch=('any')
url='http://www.dropbox.com'
license=('GPL')
install='dropbox-cli.install'
depends=('python2' 'dropbox')
makedepends=("patch")
source=("https://linux.dropbox.com/packages/dropbox.py"
        "$pkgname-arch.patch")
md5sums=('69420e8cd30592d7b832e1e6f23f7fa1'
         '0cb7114774490c31e7cc10f86692ac70')

build(){
    mkdir -p "$srcdir/build"
    cp -L "$srcdir/dropbox.py" "$srcdir/build/"
    cd "$srcdir/build"
    patch -i "$srcdir/$pkgname-arch.patch"
}

package() {
    install -D -m 755 "$srcdir/build/dropbox.py" "$pkgdir/usr/bin/dropbox-cli"
}
