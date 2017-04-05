# Maintainer:  danyf90 <daniele.formichelli@gmail.com>
# Contributor: Philipp 'TamCore' B. <philipp [at] tamcore [dot] eu>
# Contributor: Jakub Schmidtke <sjakub-at-gmail-dot-com>
# Contributor: Christoph Brill <egore911-at-gmail-dot-com>
# Contributor: Lubomir 'Kuci' Kucera <kuci24-at-gmail-dot-com>
# Contributor: Tad Fisher <tadfisher at gmail dot com>

pkgname=android-studio
pkgver=2.3.1.0
pkgrel=1
_build=162.3871768
pkgdesc="The official Android IDE (Stable branch)"
arch=('i686' 'x86_64')
url="http://tools.android.com/"
license=('APACHE')
makedepends=('unzip')
depends=('alsa-lib' 'freetype2' 'libxrender' 'libxtst')
optdepends=('gtk2: GTK+ look and feel'
            'libgl: emulator support')
options=('!strip')
source=("https://dl.google.com/dl/android/studio/ide-zips/$pkgver/android-studio-ide-$_build-linux.zip"
        "$pkgname.desktop")
sha256sums=('36520f21678f80298b5df5fe5956db17a5984576f895fdcaa36ab0dbfb408433'
            '73cd2dde1d0f99aaba5baad1e2b91c834edd5db3c817f6fb78868d102360d3c4')

if [ "$CARCH" = "i686" ]; then
    depends+=('java-environment')
fi

package() {
  cd $srcdir/$pkgname

  # Install the application
  install -d $pkgdir/{opt/$pkgname,usr/bin}
  cp -a bin gradle lib jre plugins $pkgdir/opt/$pkgname
  ln -s /opt/android-studio/bin/studio.sh $pkgdir/usr/bin/$pkgname

  # Add the icon and desktop file
  install -Dm644 bin/studio.png $pkgdir/usr/share/pixmaps/$pkgname.png
  install -Dm644 $srcdir/$pkgname.desktop $pkgdir/usr/share/applications/$pkgname.desktop

  chmod -R ugo+rX $pkgdir/opt
}
