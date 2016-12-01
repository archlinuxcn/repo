# Maintainer: Det <nimetonmaili g-mail>
# Contributors: 458italia, Madek, Berseker, Syr
# Check the latest version with:
# $ curl -s https://dl.google.com/dl/earth/client/current/google-earth-stable_current_x86_64.rpm | head -c96 | strings | cut -d "-" -f4

# Attempt to fix crashes and blank Panoramio: "1" to enable.
# - http://forums.fedoraforum.org/showthread.php?p=1678303#post1678303
_attempt_fix=0

pkgname=google-earth
pkgver=7.1.7.2600
pkgrel=1
pkgdesc="A 3D interface to view satellite images of Earth and other objects"
arch=('i686' 'x86_64')
url="https://www.google.com/earth/index.html"
license=('custom:earth')
depends=('desktop-file-utils' 'fontconfig' 'glu' 'hicolor-icon-theme' 'ld-lsb>=3-5'
         'libgl' 'libsm' 'libxrender' 'mesa' 'shared-mime-info' 'xdg-utils')
[[ $_attempt_fix = 1 ]] && depends+=('freeimage' 'libpng15' 'qtwebkit')
optdepends=('catalyst-utils: For AMD Catalyst'
            'nvidia-utils: For the NVIDIA driver')
options=('!emptydirs')
install=$pkgname.install
source=('googleearth.sh'
        'baifaao.cpp'
        'Google-Terms-of-Service.html::https://www.google.com/intl/ALL/policies/terms/index.html'
        'Google-Earth-Additional-Terms-of-Service.html::https://www.google.com/help/terms_maps.html'
        'Legal-Notices-for-Google-Earth-and-Google-Earth-APIs.html::https://www.google.com/help/legalnotices_maps.html'
        'Google-Privacy-Policy.html::https://www.google.com/intl/ALL/policies/privacy/index.html')
source_i686=("google-earth-stable_${pkgver}_i386.deb::https://dl.google.com/earth/client/current/google-earth-stable_current_i386.deb")
source_x86_64=("google-earth-stable_${pkgver}_amd64.deb::https://dl.google.com/earth/client/current/google-earth-stable_current_amd64.deb")
md5sums=('e84f5d51ea3545c131d1794f89f6464a'
         '598d579a1c3199c77850d86ba78f7b44'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP')
md5sums_i686=('cc02daa74d1b81daf44326a25460a88b')
md5sums_x86_64=('e6356f9bb99d9019ee0a156f9331beb8')

_instdir=/opt/google/earth/free/

# Build the baifaao.so
if [[ $_attempt_fix = 1 ]]; then
  build() {
    gcc -I /usr/include/qt4/ -O3 -fPIC --shared baifaao.cpp -o baifaao.so
  }
fi

package() {
  msg2 "Extracting the data.tar.xz..."
  bsdtar -xf data.tar.xz -C "$pkgdir/"

  msg2 "Moving stuff in place..."
  # The .desktop
  mv "$pkgdir"/$_instdir/google-earth.desktop "$pkgdir"/usr/share/applications/

  # Icons
  for i in 16 22 24 32 48 64 128 256; do
    install -Dm644 "$pkgdir"/$_instdir/product_logo_$i.png \
                   "$pkgdir"/usr/share/icons/hicolor/${i}x${i}/apps/google-earth.png
  done

  # Licenses
  install -Dm644 'Google-Terms-of-Service.html' \
      "$pkgdir/usr/share/licenses/$pkgname/Google-Terms-of-Service.html"
  install -Dm644 'Google-Earth-Additional-Terms-of-Service.html' \
      "$pkgdir/usr/share/licenses/$pkgname/Google-Earth-Additional-Terms-of-Service.html"
  install -Dm644 'Legal-Notices-for-Google-Earth-and-Google-Earth-APIs.html' \
      "$pkgdir/usr/share/licenses/$pkgname/Legal-Notices-for-Google-Earth-and-Google-Earth-APIs.html"
  install -Dm644 'Google-Privacy-Policy.html' \
      "$pkgdir/usr/share/licenses/$pkgname/Google-Privacy-Policy.html"

  msg2 "Removing the Debian-intended cron job and duplicated images..."
  rm -r "$pkgdir"/etc/cron.daily/ "$pkgdir"/$_instdir/product_logo_*.png

  if [[ $_attempt_fix = 1 ]]; then
    msg2 "Attempting a fix on Panoramio and certain crashes..."
    # Install baifaao.so
    install -m755 baifaao.so "$pkgdir"/$_instdir/

    # Preload it
    install -m755 googleearth.sh "$pkgdir"/$_instdir/googleearth

    # Remove the old, bundled Qt libs
    rm "$pkgdir"/$_instdir/libQt*
  fi
}
