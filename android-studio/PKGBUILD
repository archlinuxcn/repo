# Maintainer:  danyf90 <daniele.formichelli@gmail.com>
# Contributor: Philipp 'TamCore' B. <philipp [at] tamcore [dot] eu>
# Contributor: Jakub Schmidtke <sjakub-at-gmail-dot-com>
# Contributor: Christoph Brill <egore911-at-gmail-dot-com>
# Contributor: Lubomir 'Kuci' Kucera <kuci24-at-gmail-dot-com>

pkgname=android-studio
pkgver=1.3.2.0
pkgrel=1
_build=141.2178183
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
sha512sums=('68f45638919d38a8c3c144ec2dc69ccbfe6467eddc570a2fadd7a36a79bdd609861224f06989b7e4ea1422c68914539221a4cf0a33e413da49fc72e1e418e717'
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
