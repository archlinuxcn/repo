# Contributor: Valentin-Costel Haloiu <vially.ichb@gmail.com>
# Contributor: Eugene Yunak <e.yunak@gmail.com>

pkgname=kindlegen
pkgver=2.9
pkgrel=4
pkgdesc="A command line tool used to build eBooks that can be sold through Amazon's Kindle platform."
arch=('i686' 'x86_64')
url="https://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000765211"
license=(custom)
source=("https://s3.amazonaws.com/${pkgname}/${pkgname}_linux_2.6_i386_v${pkgver/\./_}.tar.gz")
md5sums=('21aef3c8846946203e178c83a37beba1')

package() {
    install -D -m755 $srcdir/kindlegen $pkgdir/usr/bin/kindlegen

    # install license files
    mkdir -p $pkgdir/usr/share/licenses/$pkgname/
    install -m644 "$srcdir/KindleGen Legal Notices 2013-02-19 Linux.txt" $pkgdir/usr/share/licenses/$pkgname/
    install -m644 $srcdir/EULA.txt $pkgdir/usr/share/licenses/$pkgname/
}
