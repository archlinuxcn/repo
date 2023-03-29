# Maintainer:   Corey Berla <corey@berla.me>
# Contributor:  M.Reynolds <blackboxnetworkproject@gmail.com>
# Contributor:  Vlad M. <vlad@archlinux.net>
# Contributor:  Christophe Gueret <christophe.gueret@gmail.com>
# Contributor:  josephgbr <rafael.f.f1@gmail.com>
# Contributor:  cmorlok <christianmorlok@web.de>
# Contributor:  fazibear <fazibear@gmail.com>
# Contributor:  neuromante <lorenzo.nizzi.grifi@gmail.com>
# Contributor:  Gordin <9ordin @t gmail.com>

pkgname=nautilus-dropbox
pkgdesc="Dropbox Nautilus Extension"
pkgver=2022.12.05
pkgrel=1
arch=(x86_64)
url="https://www.dropbox.com/"
license=('custom:CC-BY-ND-3' 'GPL')
depends=(nautilus libnautilus-extension dropbox)
makedepends=(python python-docutils python-gobject gnome-common)
options=('!libtool' '!emptydirs')
_commit=8cc1635a0e0e6edf90beb4b6f9c9ecb2b39e41f3
source=("git+https://github.com/dropbox/nautilus-dropbox.git#commit=$_commit")
sha256sums=('SKIP')

build() {
    cd nautilus-dropbox
    ./autogen.sh
    make
}

package() {
    cd nautilus-dropbox
    make DESTDIR="$pkgdir" install

    # install the common license
    install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/COPYING"

    # remove executables and depend on 'dropbox' package
    rm "$pkgdir/usr/bin/dropbox"
    rm "$pkgdir/usr/share/applications/dropbox.desktop"
    rm "$pkgdir/usr/share/man/man1/dropbox.1"
}

