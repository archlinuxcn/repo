# Maintainer: DoTheEvolution <DoTheEvo@gmail.com>
pkgname="angrysearch"
pkgver=1.0.0
pkgrel=1
pkgdesc="Instant file search"
arch=("any")
url="https://github.com/dotheevo/angrysearch/"
license=("GPL")
depends=("python-pyqt5" "libxkbcommon-x11" "xdg-utils")
optdepends=("python-gobject: desktop notifications support"
            "xdotool: Thunar & PCmanFM to select file on path open")
source=("https://github.com/DoTheEvo/ANGRYsearch/archive/v$pkgver.tar.gz")
sha256sums=("6dd2b97da63ab98f08d412bd31a0cd0413ac542d80cc7603e08b94ca13133fbe")

package() {
 cd "ANGRYsearch-$pkgver"
 install -Dm755 angrysearch.py "$pkgdir/usr/share/angrysearch/angrysearch.py"
 install -Dm755 angrysearch_update_database.py "$pkgdir/usr/share/angrysearch/angrysearch_update_database.py"
 install -Dm644 angrysearch.desktop "$pkgdir/usr/share/angrysearch/angrysearch.desktop"
 install -Dm644 angrysearch.svg "$pkgdir/usr/share/angrysearch/angrysearch.svg"
 install -Dm644 scandir.py "$pkgdir/usr/share/angrysearch/scandir.py"
 install -Dm644 resource_file.py "$pkgdir/usr/share/angrysearch/resource_file.py"
 install -Dm644 qdarkstylesheet.qss "$pkgdir/usr/share/angrysearch/qdarkstylesheet.qss"

 install -d "$pkgdir/usr/bin"
 install -d "$pkgdir/usr/share/pixmaps"
 install -d "$pkgdir/usr/share/applications"

 ln -s "/usr/share/angrysearch/angrysearch.py" "$pkgdir/usr/bin/angrysearch"
 ln -s "/usr/share/angrysearch/angrysearch.svg" "$pkgdir/usr/share/pixmaps"
 ln -s "/usr/share/angrysearch/angrysearch.desktop" "$pkgdir/usr/share/applications"
}
