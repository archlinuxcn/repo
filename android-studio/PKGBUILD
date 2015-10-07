# Maintainer:  danyf90 <daniele.formichelli@gmail.com>
# Contributor: Philipp 'TamCore' B. <philipp [at] tamcore [dot] eu>
# Contributor: Jakub Schmidtke <sjakub-at-gmail-dot-com>
# Contributor: Christoph Brill <egore911-at-gmail-dot-com>
# Contributor: Lubomir 'Kuci' Kucera <kuci24-at-gmail-dot-com>

pkgname=android-studio
pkgver=1.4.0.10
pkgrel=2
_build=141.2288178
pkgdesc="A new Android development environment based on IntelliJ IDEA."
arch=('i686' 'x86_64')
url="http://developer.android.com/sdk/installing/studio.html"
license=('APACHE')
depends=('java-environment' 'python' 'ttf-font')
makedepends=('unzip')
optdepends=('android-google-repository' 'android-sdk' 'android-sdk-platform-tools' 'android-sdk-build-tools' 'android-support' 'android-support-repository')
conflicts=('android-studio-beta' 'android-studio-dev' 'android-studio-canary')
options=('!strip')
install=$pkgname.install
source=("https://dl.google.com/dl/android/studio/ide-zips/$pkgver/android-studio-ide-$_build-linux.zip"
        "$pkgname.desktop")
sha512sums=('afc77575f9261060c28f27ee49b05b88de338c0b2b8d91eea2a8585243dc6404bc2784b7d15b2c05ac504228ceea11ccbbdfd4fa79a1037893232c55cb524b2f'
            '7c1ab152b3f26a0a4796c085bb7bf66aa4711a010910636c0c82a37609155c819b21a732fc3874b55e7d443c989c46f29d51ed54538795829c8eb835308b5aaa')

if [[ $CARCH == "x86_64" ]]; then
  depends+=('lib32-fontconfig' 'lib32-libxrender' 'lib32-mesa')
else
  depends+=('fontconfig' 'libxrender' 'mesa')
fi

prepare() {
  cd $srcdir/$pkgname

  # extract the application icon
  unzip -qo lib/resources.jar artwork/icon_AS_128.png

  # enable anti aliasing
  echo "-Dswing.aatext=true" >> studio.vmoptions
  echo "-Dswing.aatext=true" >> studio64.vmoptions
}

package() {
  cd $srcdir/$pkgname

  # application stuff
  install -d $pkgdir/{opt/$pkgname,usr/bin}
  cp -a bin lib plugins $pkgdir/opt/$pkgname
  ln -s /opt/android-studio/bin/studio.sh $pkgdir/usr/bin/android-studio

  # starter stuff
  install -Dm644 artwork/icon_AS_128.png $pkgdir/usr/share/pixmaps/$pkgname.png
  install -Dm644 $srcdir/$pkgname.desktop $pkgdir/usr/share/applications/$pkgname.desktop

  chmod -R ugo+rX $pkgdir/opt
}
