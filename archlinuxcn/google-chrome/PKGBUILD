# Maintainer: Knut Ahlers <knut at ahlers dot me>
# Contributor: Det <nimetonmaili g-mail>
# Contributors: t3ddy, Lex Rivera aka x-demon, ruario

# Check for new Linux releases in: http://googlechromereleases.blogspot.com/search/label/Stable%20updates
# or use: $ curl -s https://dl.google.com/linux/chrome/rpm/stable/x86_64/repodata/other.xml.gz | gzip -df | awk -F\" '/pkgid/{ sub(".*-","",$4); print $4": "$10 }'

pkgname=google-chrome
pkgver=75.0.3770.90
pkgrel=1
pkgdesc="The popular and trusted web browser by Google (Stable Channel)"
arch=('x86_64')
url="https://www.google.com/chrome"
license=('custom:chrome')
depends=('alsa-lib' 'gtk3' 'libcups' 'libxss' 'libxtst' 'nss')
optdepends=('kdialog: for file dialogs in KDE'
            'gnome-keyring: for storing passwords in GNOME keyring'
            'kwallet: for storing passwords in KWallet'
            'gtk3-print-backends: for printing'
            'libunity: for download progress on KDE'
            'ttf-liberation: fix fonts for some PDFs (CRBug #369991)'
            'xdg-utils')
options=('!emptydirs' '!strip')
install=$pkgname.install
_channel=stable
source=("google-chrome-${_channel}_${pkgver}_amd64.deb::https://dl.google.com/linux/direct/google-chrome-${_channel}_current_amd64.deb"
        'eula_text.html'
        "google-chrome-$_channel.sh")
sha512sums=('6d993160674ce0eef89ccd396216bcf5dfb8ff8b770aff918f13e2f0003deb5a92a9177cdb28321a54138d5f4b5a551c2282fcb986e70a3f68745c547a261bc3'
            'a225555c06b7c32f9f2657004558e3f996c981481dbb0d3cd79b1d59fa3f05d591af88399422d3ab29d9446c103e98d567aeafe061d9550817ab6e7eb0498396'
            'e1a76d6aa17a13325e30329fde5d7acd5f6863c6b4fc8a9b521b1995342447ab71188b1a176b58ed95a409659936544cf4e8cb492e0fda69dabfeae24f02bbf3')

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

  # License
  install -Dm644 eula_text.html "$pkgdir"/usr/share/licenses/google-chrome/eula_text.html

  msg2 "Fixing Chrome icon resolution..."
  sed -i "/Exec=/i\StartupWMClass=Google-chrome" "$pkgdir"/usr/share/applications/google-chrome.desktop

  msg2 "Removing Debian Cron job and duplicate product logos..."
  rm -r "$pkgdir"/etc/cron.daily/ "$pkgdir"/opt/google/chrome/cron/
  rm "$pkgdir"/opt/google/chrome/product_logo_*.png
}
