# Maintainer: Det <nimetonmaili g-mail>
# Contributors: t3ddy, Lex Rivera aka x-demon, ruario

# Check for new Linux releases in: http://googlechromereleases.blogspot.com/search/label/Stable%20updates
# or use: $ curl -s https://dl.google.com/linux/chrome/rpm/stable/x86_64/repodata/other.xml.gz | gzip -df | awk -F\" '/pkgid/{ sub(".*-","",$4); print $4": "$10 }'

pkgname=google-chrome
pkgver=61.0.3163.79
pkgrel=1
pkgdesc="An attempt at creating a safer, faster, and more stable browser (Stable Channel)"
arch=('x86_64')
url="https://www.google.com/chrome"
license=('custom:chrome')
depends=('alsa-lib' 'gconf' 'gtk3' 'libcups' 'libxss' 'libxtst' 'nss')
optdepends=('kdialog: needed for file dialogs in KDE'
            'gnome-keyring: for storing passwords in GNOME keyring'
            'kwallet: for storing passwords in KWallet'
            'libunity: download progress on KDE'
            'ttf-liberation: fix fonts for some PDFs (CRBug #369991)'
            'xdg-utils')
options=('!emptydirs' '!strip')
install=$pkgname.install
_channel=stable
source=("google-chrome-${_channel}_${pkgver}_amd64.deb::https://dl.google.com/linux/direct/google-chrome-${_channel}_current_amd64.deb"
        "$url/browser/privacy/eula_text.html"
        "google-chrome-$_channel.sh")
md5sums=('949b2e20ecfe0e77d3388f9f1c9a16ed'
         'SKIP'
         '99fa93d5e7fb5d622cef0f9621f3ffa3')

## Previous versions (also see: /var/cache/pacman/pkg/google-chrome-[^a-z]*):
#source[0]="https://dl.google.com/linux/deb/pool/main/g/google-chrome-${_channel}/google-chrome-${_channel}_${pkgver}-1_amd64.deb"
#md5sums[0]='SKIP'

package() {
  msg2 "Extracting the data.tar.xz..."
  bsdtar -xf data.tar.xz -C "$pkgdir/"

  msg2 "Moving stuff in place..."
  # Launcher
  install -m755 google-chrome-$_channel.sh "$pkgdir"/usr/bin/google-chrome-$_channel

  # Icons
  for i in 16x16 22x22 24x24 32x32 48x48 64x64 128x128 256x256; do
    install -Dm644 "$pkgdir"/opt/google/chrome/product_logo_${i/x*}.png \
                   "$pkgdir"/usr/share/icons/hicolor/$i/apps/google-chrome.png
  done

  # Man page
  gzip "$pkgdir"/usr/share/man/man1/google-chrome.1

  # License
  install -Dm644 eula_text.html "$pkgdir"/usr/share/licenses/google-chrome/eula_text.html

  msg2 "Fixing Chrome icon resolution..."
  sed -i "/Exec=/i\StartupWMClass=Google-chrome" "$pkgdir"/usr/share/applications/google-chrome.desktop

  msg2 "Removing Debian Cron job and duplicate product logos..."
  rm -r "$pkgdir"/etc/cron.daily/ "$pkgdir"/opt/google/chrome/cron/
  rm "$pkgdir"/opt/google/chrome/product_logo_*.png
}
