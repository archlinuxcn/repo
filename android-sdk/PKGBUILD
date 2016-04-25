# Maintainer: Alexander F Rødseth <xyproto@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: Gordin <9ordin @t gmail dot com>

pkgname=android-sdk
pkgver=24.4.1
pkgrel=4
pkgdesc='Google Android SDK'
arch=('x86_64' 'i686')
url='http://developer.android.com/sdk/'
license=('custom')
depends_x86_64=('java-environment' 'lib32-alsa-lib' 'lib32-openal'
  'lib32-libstdc++5' 'lib32-libxv' 'lib32-mesa' 'lib32-ncurses' 'lib32-sdl'
  'lib32-zlib' 'lib32-fontconfig' 'lib32-libpulse' 'swt' 'ncurses5-compat-libs')
depends_i686=('java-environment' 'alsa-lib' 'openal' 'libstdc++5' 'libxv' 'sdl'
              'ncurses' 'swt' 'zlib' 'ncurses5-compat-libs')
install="$pkgname.install"
optdepends=('android-udev: udev rules for Android devices'
            'android-sdk-platform-tools: adb, aapt, aidl, dexdump and dx')
source=("https://dl.google.com/android/repository/tools_r${pkgver}-linux.zip"
        'https://developer.android.com/assets/images/android_logo.png'
        "$pkgname.desktop"
        "$pkgname.sh"
        "$pkgname.csh"
        "$pkgname.conf"
        'license.html')
sha1sums=('7e00ea3715f2cf666296ce22058764ec7ecb3b7e'
          'b8726c63294a23e5fea066a36061164e583b5732'
          '8f886de363ad91a7f93a0c6ded993e99bef3e1a7'
          '78f8574e651c9bf8b7515ecb30c7ef93edbc4a96'
          '08c85aab7523e22b298891c7047bc0e7adbf3437'
          '145bdf3eb41a56574b289c1577a24bc47097ec83'
          'bfb91be7e0b602d765b7a1fcaf0ce1b7e1a93faa')

package() {
  install -Dm755 "$pkgname.sh" "$pkgdir/etc/profile.d/$pkgname.sh"
  install -Dm755 "$pkgname.csh" "$pkgdir/etc/profile.d/$pkgname.csh"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"
  install -Dm644 android_logo.png "$pkgdir/usr/share/pixmaps/$pkgname.png"
  install -Dm644 "$pkgname.desktop" \
    "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 license.html \
    "$pkgdir/usr/share/licenses/$pkgname/license.html"
  install -d "$pkgdir/opt/$pkgname/platforms"
  install -d "$pkgdir/opt/$pkgname/add-ons"

  cp -a tools "$pkgdir/opt/$pkgname"

  if [[ $CARCH = i686 ]]; then
    rm -rf ${pkgdir}/opt/android-sdk/tools/lib/{monitor-,}x86_64 \
      ${pkgdir}/opt/android-sdk/tools/lib/lib64* \
      ${pkgdir}/opt/android-sdk/tools/emulator64-*
  fi

  # Fix broken permissions
  chmod -R o=g "$pkgdir/opt/$pkgname"
  find "$pkgdir/opt/$pkgname" -perm 744 -exec chmod 755 {} +
}

# getver: developer.android.com/tools/sdk/tools-notes.html
# vim:set ts=2 sw=2 et:
