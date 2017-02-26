# Maintainer: Det <nimetonmaili g-mail>
# Contributors: t3ddy, Lex Rivera aka x-demon, ruario

# Check for new Linux releases in: http://googlechromereleases.blogspot.com/search/label/Dev%20updates
# or use: $ curl -s https://dl.google.com/linux/chrome/rpm/stable/x86_64/repodata/other.xml.gz | gzip -df | awk -F\" '/pkgid/{ sub(".*-","",$4); print $4": "$10 }'

pkgname=google-chrome-dev
pkgver=58.0.3018.3
pkgrel=1
pkgdesc="An attempt at creating a safer, faster, and more stable browser (Dev Channel)"
arch=('x86_64')
url="https://www.google.com/chrome"
license=('custom:chrome')
depends=('alsa-lib' 'gconf' 'gtk2' 'libxss' 'libxtst' 'nss')
optdepends=('kdialog: needed for file dialogs in KDE'
            'gnome-keyring: for storing passwords in GNOME keyring'
            'kwallet: for storing passwords in KWallet'
            'ttf-liberation: fix fonts for some PDFs (CRBug #369991)')
provides=('google-chrome')
options=('!emptydirs' '!strip')
install=$pkgname.install
_channel=unstable
source=("google-chrome-${_channel}_${pkgver}_amd64.deb::https://dl.google.com/linux/direct/google-chrome-${_channel}_current_amd64.deb"
        "$url/browser/privacy/eula_text.html"
        'google-chrome-unstable.sh')
md5sums=('2f4af575456818bb484002d3ce365c88'
         'SKIP'
         '11b55a3fec7279db32b63e3a0b97dc01')

## Previous build (also see: /var/cache/pacman/pkg/google-chrome-dev-*):
#source[0]='http://mirror.glendaleacademy.org/chrome/pool/main/g/google-chrome-unstable/google-chrome-unstable_58.0.3013.3-1_amd64.deb'
#md5sums[0]='fc2f71495eb3c2038b39252becfecfed'

package() {
  msg2 "Extracting the data.tar.xz..."
  bsdtar -xf data.tar.xz -C "$pkgdir/"

  msg2 "Moving stuff in place..."
  # Launcher
  install -m755 google-chrome-$_channel.sh "$pkgdir"/usr/bin/google-chrome-$_channel

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
  sed -i "/Exec=/i\StartupWMClass=Google-chrome-$_channel" "$pkgdir"/usr/share/applications/google-chrome-$_channel.desktop

  msg2 "Removing Debian Cron job and duplicate product logos..."
  rm -r "$pkgdir"/etc/cron.daily/ "$pkgdir"/opt/google/chrome-$_channel/cron/
  rm "$pkgdir"/opt/google/chrome-$_channel/product_logo_*.png
}
