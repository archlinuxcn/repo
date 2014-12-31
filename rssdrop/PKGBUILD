pkgname=rssdrop
pkgver=22.b9a43ee
pkgrel=1
pkgdesc="A Perl script to deliver rss feeds to Maildirs."
arch=('any')
url="https://github.com/petronny/rssdrop"
license=('GPL3')
depends=('perl-xml-simple' 'perl-date-manip' 'perl-lwp-protocol-https')
makedepends=('git')
source=("git+https://github.com/petronny/rssdrop"
        "rssdrop.install")
sha256sums=('SKIP'
            '4a733fc69835eac68f5cc381a96158311e0fcb1b1fc8aa8ec35bd2b7aa584a09')
install='rssdrop.install'

pkgver() {
    cd $pkgname
    echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

package() {
    cd $pkgname

    mkdir -p "$pkgdir/usr/bin/"
    cp rssdrop "$pkgdir/usr/bin/"
}
