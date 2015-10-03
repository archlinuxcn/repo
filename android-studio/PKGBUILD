# Maintainer:  danyf90 <daniele.formichelli@gmail.com>
# Contributor: Philipp 'TamCore' B. <philipp [at] tamcore [dot] eu>
# Contributor: Jakub Schmidtke <sjakub-at-gmail-dot-com>
# Contributor: Christoph Brill <egore911-at-gmail-dot-com>
# Contributor: Lubomir 'Kuci' Kucera <kuci24-at-gmail-dot-com>

pkgname=android-studio
pkgver=1.4.0.10
pkgrel=1
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
            'fa3567f328af45d265c4fabf3e41b55d8e8cccfa9675e745f07dd6ae41950dd53a2ef41ef1caee86643f5c2ddf7a7681ee17155e208a7b6fdae6c0537dfc0c94')

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
