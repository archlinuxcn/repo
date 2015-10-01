# Maintainer: XavierCLL <xavier.corredor.llano (a) gmail.com>

pkgname=pycharm-professional
pkgver=4.5.4
_pkgver=4.5.4
pkgrel=2
pkgdesc="Powerful Python and Django IDE. Professional version."
arch=('any')
options=('!strip')
url="http://www.jetbrains.com/pycharm/"
conflicts=('pycharm' 'pycharm-community')
provides=('pycharm')
license=('Commercial')
install=${pkgname}.install
depends=('java-environment' 'giflib' 'ipython' 'ipython2' 'ttf-font')
source=(http://download.jetbrains.com/python/$pkgname-$_pkgver.tar.gz
        'pycharm-professional.desktop'
        'pycharm-professional.install'
        'pycharm')
optdepends=('openssh: For deployment and remote connections'
            'python2-setuptools: Packages manager for Python 2, for project interpreter'
            'python-setuptools: Packages manager for Python 3, for project interpreter'
            'python2-coverage: For support code coverage measurement for Python 2'
            'python-coverage: For support code coverage measurement for Python 3'
            'vagrant: For support virtualized development environments')
sha256sums=('0d3a0a627901a1519ee77a0f2b34bc9cd7ba9a20c1276862ed5324187d25c6b7'
            '016db1860a8b36d408c827f90aeb04b9d55cf21ea36788a9d8510cc54fae1c49'
            '6442ec9f0690f743da697a2a65b0784017de501e7f39d5de0879153fbf85dc7a'
            'ad59415f8ac2c623f9c61453caf70bf75b6b14db2f09807e4ea339a2dc740be9')

package() {
  # base
  cd $srcdir
  mkdir -p $pkgdir/opt/$pkgname
  cp -R $srcdir/pycharm-$_pkgver/* $pkgdir/opt/$pkgname
  mkdir -p $pkgdir/usr/share/{applications,pixmaps}
  mkdir -p $pkgdir/usr/bin/
  install -Dm644 $pkgdir/opt/$pkgname/bin/pycharm.png $pkgdir/usr/share/pixmaps/pycharm.png
  # lisense
  mkdir -p $pkgdir/usr/share/licenses/$pkgname/
  install -Dm644 $srcdir/pycharm-$_pkgver/license/PyCharm_license.txt $pkgdir/usr/share/licenses/$pkgname/PyCharm_license.txt
  # exec
  install -Dm755 $startdir/pycharm $pkgdir/usr/bin/
  # app file desktop
  install -Dm644 $startdir/pycharm-professional.desktop $pkgdir/usr/share/applications/
  
  # delete some conflicts files for i686 
  if [[ $CARCH = 'i686' ]]; then
          rm -f $pkgdir/opt/$pkgname/bin/libyjpagent-linux64.so
          rm -f $pkgdir/opt/$pkgname/bin/fsnotifier64
  fi

  # enable anti-aliasing text in pycharm options
  if [[ $CARCH = 'i686' ]]; then
	#echo '-Dawt.useSystemAAFontSettings=on' >> $pkgdir/opt/$pkgname/bin/pycharm.vmoptions
        echo '-Dswing.aatext=true' >> $pkgdir/opt/$pkgname/bin/pycharm.vmoptions
  else
	#echo '-Dawt.useSystemAAFontSettings=on' >> $pkgdir/opt/$pkgname/bin/pycharm64.vmoptions
        echo '-Dswing.aatext=true' >> $pkgdir/opt/$pkgname/bin/pycharm64.vmoptions
  fi
  
}

# vim:set ts=2 sw=2 et:
