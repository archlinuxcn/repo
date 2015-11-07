# Maintainer: Joel Teichroeb <joel@teichroeb.net>
# Contributor: Matthias Maennich < arch .at. maennich.net >
# Contributor: bruce < b_a_g99 .at. hotmail.com >
# Contributor: carstene1ns <arch carsten-teibes de>

pkgname=dropbox-cli
pkgver=2015.10.28
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
sha1sums=('32eb8cf7dc3b37440ef6553c332712b7f326f2f6'
          '9e595a8ba7e6d5f83f46a8e0be1fca02e6570d7e')

build(){
    mkdir -p "$srcdir/build"
    cp -L "$srcdir/dropbox.py" "$srcdir/build/"
    cd "$srcdir/build"
    patch -i "$srcdir/$pkgname-arch.patch"
}

package() {
    install -D -m 755 "$srcdir/build/dropbox.py" "$pkgdir/usr/bin/dropbox-cli"
}
