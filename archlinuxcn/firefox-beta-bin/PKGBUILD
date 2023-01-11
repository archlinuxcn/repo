# Maintainer: Simon Brulhart <simon@brulhart.me>
# Contributors: Det <nimetonmaili g-mail>, Achilleas Pipinellis, speed145a, Schnouki, bittin

pkgname=firefox-beta-bin
_pkgname=firefox-beta
pkgver=109.0rc1
_major=${pkgver/rc*}
_build=${pkgver/*rc}
pkgrel=1
pkgdesc="Standalone web browser from mozilla.org - Beta"
arch=('x86_64')
url="https://www.mozilla.org/en-US/firefox/channel/#beta"
license=('MPL' 'GPL' 'LGPL')
depends=('dbus-glib' 'gtk3' 'libxt' 'nss')
optdepends=('ffmpeg: H264/AAC/MP3 decoding'
            'hunspell: Spell checking'
            'hyphen: Hyphenation'
            'libnotify: Notification integration'
            'networkmanager: Location detection via available WiFi networks'
            'pulseaudio: Sound'
            'upower: Battery API')
provides=("firefox=$pkgver")
conflicts=('firefox-beta')
install=$pkgname.install
source=("https://archive.mozilla.org/pub/firefox/releases/$pkgver/linux-x86_64/en-US/firefox-$pkgver.tar.bz2"
        "$_pkgname.sh"
        "$pkgname.desktop")
sha256sums=('c9ca7847bcd04b5c2d102ee305f1240c79618bd2a33d24fe4d87778557d473c9'
            '4bec62032e49c28ff27750abddbdbdbb1a4b5cba719c39498968fe53adee790b'
            '210f13ea47c4b96387f26ee7fc4dfc5c192cfb169aef2a13303fbd1ee58b3761')
# RC
if [[ $_build = ? ]]; then
  source[0]="firefox-$pkgver.tar.bz2::https://ftp.mozilla.org/pub/firefox/candidates/$_major-candidates/build$_build/linux-x86_64/en-US/firefox-$_major.tar.bz2"
fi

package() {
  # Create directories
  msg2 "Creating directory structure..."
  mkdir -p "$pkgdir"/usr/bin
  mkdir -p "$pkgdir"/usr/share/applications
  mkdir -p "$pkgdir"/opt

  msg2 "Moving stuff in place..."
  # Install
  cp -r firefox/ "$pkgdir"/opt/$_pkgname

  # Launchers
  install -m755 $_pkgname.sh "$pkgdir"/usr/bin/$_pkgname
  ln -s $_pkgname "$pkgdir"/usr/bin/$pkgname  # compatibility
#  ln -sf firefox "$pkgdir"/opt/$_pkgname/firefox-bin

  # Desktops
  install -m644 *.desktop "$pkgdir"/usr/share/applications/

  # Icons
  for i in 16x16 32x32 48x48 64x64 128x128; do
    install -d "$pkgdir"/usr/share/icons/hicolor/$i/apps/
    ln -s /opt/$_pkgname/browser/chrome/icons/default/default${i/x*}.png \
          "$pkgdir"/usr/share/icons/hicolor/$i/apps/$_pkgname.png
  done

  # Use system-provided dictionaries
  #rm -r "$pkgdir"/opt/$_pkgname/dictionaries
  ln -Ts /usr/share/hunspell "$pkgdir"/opt/$_pkgname/dictionaries
  ln -Ts /usr/share/hyphen "$pkgdir"/opt/$_pkgname/hyphenation

  # Use system certificates
  ln -sf /usr/lib/libnssckbi.so "$pkgdir"/opt/$_pkgname/libnssckbi.so
}
