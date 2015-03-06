#Maintainer: xgdgsc<xgdgsc@gmail.com>
pkgname=lindict-git
pkgver=20150305
pkgrel=1
pkgdesc="Opensource youdao dictionary client"
arch=('any')
url="https://gitcafe.com/Jactry/LinDict"
license=('GPL3')
depends=('python2-pyqt')
source=('https://gitcafe.com/Jactry/LinDict/archiveball/master/tar.gz' 'lindict.desktop')
md5sums=('49e927734a6e4a6c118bb4fa67c22bc4' 'e4fd210491586dc040881aea7db0610d')

package() {
    mkdir -p $pkgdir/opt/lindict
    mkdir -p $pkgdir/usr/share/applications
    cp -R $srcdir/LinDict/src/* $pkgdir/opt/lindict
    install -Dm644 "$srcdir/lindict.desktop" "$pkgdir/usr/share/applications/lindict.desktop"
}
