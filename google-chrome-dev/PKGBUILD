# Maintainer: Det <nimetonmaili g-mail>
# Contributors: t3ddy, Lex Rivera aka x-demon, ruario

# Check for new Linux releases in: http://googlechromereleases.blogspot.com/search/label/Dev%20updates
# or use: $ curl -s https://dl.google.com/linux/chrome/rpm/stable/x86_64/repodata/other.xml.gz | gzip -df | awk -F\" '/pkgid/{ sub(".*-","",$4); print $4": "$10 }'

pkgname=google-chrome-dev
pkgver=50.0.2661.11
pkgrel=1
pkgdesc="An attempt at creating a safer, faster, and more stable browser (Dev Channel)"
arch=('x86_64')
url="https://www.google.com/chrome"
license=('custom:chrome')
depends=('alsa-lib' 'desktop-file-utils' 'flac' 'gconf' 'gtk2' 'harfbuzz' 'harfbuzz-icu' 'hicolor-icon-theme'
         'icu' 'libpng' 'libxss' 'libxtst' 'nss' 'opus' 'snappy' 'speech-dispatcher' 'ttf-font' 'xdg-utils')
optdepends=('kdebase-kdialog: needed for file dialogs in KDE'
            'ttf-liberation: fix fonts for some PDFs')
makedepends=('pacman>=4.2.0')
provides=('google-chrome' 'pepper-flash')
options=('!emptydirs' '!strip')
install=$pkgname.install
_channel=unstable
source=("google-chrome-${_channel}_${pkgver}_amd64.deb::https://dl.google.com/linux/direct/google-chrome-${_channel}_current_amd64.deb"
        "$url/browser/privacy/eula_text.html"
        'google-chrome-unstable')
md5sums=('710da077a39ed0c88c25daf930c16299'
         'SKIP'
         '11b55a3fec7279db32b63e3a0b97dc01')

## Previous build (also see: /var/cache/pacman/pkg/google-chrome-dev-*):
#source[0]=('http://mirror.glendaleacademy.org/chrome/pool/main/g/google-chrome-unstable/google-chrome-unstable_50.0.2657.0-1_amd64.deb')
#md5sums[0]=('a58034acc41d37047f384007004b5585')

package() {
  msg2 "Extracting the data.tar.xz..."
  bsdtar -xf data.tar.xz -C "$pkgdir/"

  msg2 "Moving stuff in place..."
  # Launcher
  install -m755 google-chrome-$_channel "$pkgdir"/usr/bin/

  # Icons
  for i in 16x16 22x22 24x24 32x32 48x48 64x64 128x128 256x256; do
    install -Dm644 "$pkgdir"/opt/google/chrome-$_channel/product_logo_${i/x*}.png \
                   "$pkgdir"/usr/share/icons/hicolor/$i/apps/google-chrome-$_channel.png
  done

  # Man page
  gzip "$pkgdir"/usr/share/man/man1/google-chrome-$_channel.1

  # License
  install -Dm644 eula_text.html "$pkgdir"/usr/share/licenses/google-chrome-$_channel/eula_text.html

  msg2 "Fixing Chrome icon resolution..."
  sed -i "/Exec=/i\StartupWMClass=google-chrome-$_channel" "$pkgdir"/usr/share/applications/google-chrome-$_channel.desktop

  msg2 "Removing unnecessities (e.g. Debian Cron job)..."
  rm -r "$pkgdir"/etc/cron.daily/ "$pkgdir"/opt/google/chrome-$_channel/cron/
  rm "$pkgdir"/opt/google/chrome-$_channel/product_logo_*.png
}
