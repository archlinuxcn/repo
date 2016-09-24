# Maintainer:  danyf90 <daniele.formichelli@gmail.com>
# Contributor: Philipp 'TamCore' B. <philipp [at] tamcore [dot] eu>
# Contributor: Jakub Schmidtke <sjakub-at-gmail-dot-com>
# Contributor: Christoph Brill <egore911-at-gmail-dot-com>
# Contributor: Lubomir 'Kuci' Kucera <kuci24-at-gmail-dot-com>

pkgname=android-studio
pkgver=2.2.0.12
pkgrel=1
_build=145.3276617
pkgdesc="A new Android development environment based on IntelliJ IDEA."
arch=('i686' 'x86_64')
url="http://developer.android.com/sdk/installing/studio.html"
license=('APACHE')
depends=('java-environment' 'python' 'ttf-font')
makedepends=('unzip')
optdepends=('android-google-repository' 'android-platform' 'android-sdk' 'android-sdk-platform-tools' 'android-sdk-build-tools' 'android-sources' 'android-support' 
'android-support-repository' 'gtk2' 'libgl')
options=('!strip')
source=("https://dl.google.com/dl/android/studio/ide-zips/$pkgver/android-studio-ide-$_build-linux.zip"
        "$pkgname.desktop")
sha512sums=('71310d6b9fb071fc6b9810765389a2311a62cc706cbe71b2fe466167fb2ded7ebcc2441fe49d34a2942bb79d516f6acfcba5e214e1af42c9e2bc988a28c6fb79'
            '7c1ab152b3f26a0a4796c085bb7bf66aa4711a010910636c0c82a37609155c819b21a732fc3874b55e7d443c989c46f29d51ed54538795829c8eb835308b5aaa')

if [[ $CARCH == "x86_64" ]]; then
  depends+=('lib32-fontconfig' 'lib32-libxrender' 'lib32-mesa')
else
  depends+=('fontconfig' 'libxrender' 'mesa')
fi

package() {
  cd $srcdir/$pkgname

  # Install the application
  install -d $pkgdir/{opt/$pkgname,usr/bin}
  cp -a bin gradle lib jre plugins $pkgdir/opt/$pkgname
  ln -s /opt/android-studio/bin/studio.sh $pkgdir/usr/bin/android-studio

  # Add the icon and desktop file
  install -Dm644 bin/studio.png $pkgdir/usr/share/pixmaps/$pkgname.png
  install -Dm644 $srcdir/$pkgname.desktop $pkgdir/usr/share/applications/$pkgname.desktop

  chmod -R ugo+rX $pkgdir/opt
}
