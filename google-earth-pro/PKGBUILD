# Maintainer: Det <nimetonmaili g-mail>
# Check the latest version with:
# $ curl -sL https://dl.google.com/linux/earth/deb/dists/stable/main/binary-amd64/Packages | grep -Pom1 "Version: \K[^-]*"

# Attempt to fix crashes and blank Panoramio: "1" to enable.
# - http://forums.fedoraforum.org/showthread.php?p=1678303#post1678303
_attempt_fix=0

pkgname=google-earth-pro
pkgver=7.3.0.3832
pkgrel=1
pkgdesc="3D interface to explore the globe, terrain, streets, buildings and other planets - Pro"
arch=('i686' 'x86_64')
url="https://www.google.com/earth/index.html"
license=('custom:earth')
depends=('glu' 'hicolor-icon-theme' 'ld-lsb>=3-5' 'libsm' 'libxrender' 'nss')
[[ $_attempt_fix = 1 ]] && depends+=('freeimage' 'libpng15' 'qtwebkit')
optdepends=('catalyst-utils: For AMD Catalyst'
            'nvidia-utils: For the NVIDIA driver')
provides=('google-earth')
options=('!emptydirs')
install=$pkgname.install
source=('googleearth.sh'
        'baifaao.cpp'
        'Google-Terms-of-Service.html::https://www.google.com/intl/ALL/policies/terms/index.html'
        'Google-Earth-Additional-Terms-of-Service.html::https://www.google.com/help/terms_maps.html'
        'Legal-Notices-for-Google-Earth-and-Google-Earth-APIs.html::https://www.google.com/help/legalnotices_maps.html'
        'Google-Privacy-Policy.html::https://www.google.com/intl/ALL/policies/privacy/index.html')
#source_i686=("google-earth-pro-stable_${pkgver}_i386.deb::https://dl.google.com/earth/client/current/google-earth-pro-stable_current_i386.deb")
#source_x86_64=("google-earth-pro-stable_${pkgver}_amd64.deb::https://dl.google.com/earth/client/current/google-earth-pro-stable_current_amd64.deb")
source_i686=("https://dl.google.com/linux/earth/deb/pool/main/g/google-earth-pro-stable/google-earth-pro-stable_$pkgver-r0_i386.deb")
source_x86_64=("https://dl.google.com/linux/earth/deb/pool/main/g/google-earth-pro-stable/google-earth-pro-stable_$pkgver-r0_amd64.deb")
md5sums=('34c413a93b06010e66a1a1c4c9386696'
         '598d579a1c3199c77850d86ba78f7b44'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP')
md5sums_i686=('5c298610ae4bd604fcfd54fdc32e53dd')
md5sums_x86_64=('b9d8281257b7ebf0dfac1ab1d3578681')

_instdir=/opt/google/earth/pro/

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
  mv "$pkgdir"/$_instdir/google-earth-pro.desktop "$pkgdir"/usr/share/applications/

  # Icons
  for i in 16 22 24 32 48 64 128 256; do
    install -Dm644 "$pkgdir"/$_instdir/product_logo_$i.png \
                   "$pkgdir"/usr/share/icons/hicolor/${i}x${i}/apps/google-earth-pro.png
  done

  # Licenses
  for i in 'Google-Terms-of-Service.html' \
           'Google-Earth-Additional-Terms-of-Service.html' \
           'Legal-Notices-for-Google-Earth-and-Google-Earth-APIs.html' \
           'Google-Privacy-Policy.html'; do
     install -Dm644 $i "$pkgdir"/usr/share/licenses/$pkgname/$i
  done

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