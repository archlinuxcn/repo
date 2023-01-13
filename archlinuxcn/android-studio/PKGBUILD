# Contributor:  danyf90 <daniele.formichelli@gmail.com>
# Contributor: Philipp 'TamCore' B. <philipp [at] tamcore [dot] eu>
# Contributor: Jakub Schmidtke <sjakub-at-gmail-dot-com>
# Contributor: Christoph Brill <egore911-at-gmail-dot-com>
# Contributor: Lubomir 'Kuci' Kucera <kuci24-at-gmail-dot-com>
# Contributor: Tad Fisher <tadfisher at gmail dot com>
# Contributor: Philippe Hürlimann <p@hurlimann.org>
# Contributor: Julian Raufelder <aur@raufelder.com>
# Contributor: Dhina17 <dhinalogu@gmail.com>
# Maintainer: Kordian Bruck <k@bruck.me>

pkgname=android-studio
pkgver=2022.1.1.19
pkgrel=1
pkgdesc="The official Android IDE (Stable branch)"
arch=('i686' 'x86_64')
url="https://developer.android.com/"
license=('APACHE')
makedepends=()
depends=('alsa-lib' 'freetype2' 'libxrender' 'libxtst' 'which')
optdepends=('gtk2: GTK+ look and feel'
            'libgl: emulator support'
            'ncurses5-compat-libs: native debugger support')
options=('!strip')
source=("https://dl.google.com/dl/android/studio/ide-zips/$pkgver/android-studio-$pkgver-linux.tar.gz"
        "$pkgname.desktop"
        "license.html")
sha256sums=('96ec44e9ad82f3a241dbc7b3b88655e3d4f2137d784b545c3574270906a68d40'
            '73cd2dde1d0f99aaba5baad1e2b91c834edd5db3c817f6fb78868d102360d3c4'
            '9a7563f7fb88c9a83df6cee9731660dc73a039ab594747e9e774916275b2e23e')

if [ "$CARCH" = "i686" ]; then
    depends+=('java-environment')
fi

package() {
  cd $srcdir/$pkgname

  # Install the application
  install -d $pkgdir/{opt/$pkgname,usr/bin}
  cp -a bin lib jbr plugins license LICENSE.txt build.txt product-info.json $pkgdir/opt/$pkgname
  ln -s /opt/android-studio/bin/studio.sh $pkgdir/usr/bin/$pkgname

  # Copy licenses
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
  install -Dm644 $srcdir/license.html "${pkgdir}/usr/share/licenses/${pkgname}/license.html"

  # Add the icon and desktop file
  install -Dm644 bin/studio.png $pkgdir/usr/share/pixmaps/$pkgname.png
  install -Dm644 $srcdir/$pkgname.desktop $pkgdir/usr/share/applications/$pkgname.desktop

  chmod -R ugo+rX $pkgdir/opt
}
