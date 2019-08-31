# Maintainer: edward-p <edward At edward-p Dot xyz>

pkgname=proxmark3-iceman-git
pkgver=6934.b792d0d5
pkgrel=1
pkgdesc=pkgdesc='RRG / Iceman repo - Proxmark3 RDV4.0 and other Proxmark3 platforms.'
arch=('x86_64')
url='https://github.com/RfidResearchGroup/proxmark3'
license=('GPL2')
depends=('libusb' 'perl')
makedepends=('git' 'arm-none-eabi-gcc' 'arm-none-eabi-newlib')
provides=('proxmark3' 'proxmark3-iceman')
conflicts=('proxmark3' 'proxmark3-iceman')
options=('!makeflags')
replaces=($pkgname'-generic' $pkgname'-rdv4')
source=("$pkgname::git+https://github.com/RfidResearchGroup/proxmark3.git")
sha512sums=('SKIP')
install=proxmark3-iceman-git.install

pkgver() {
  cd $pkgname
  echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

build() {
  cd "${srcdir}/${pkgname}"

  mkdir "build"
  
  STANDALONE_MODES=('LF_SAMYRUN' 'LF_ICERUN' 'LF_PROXBRUTE' 'LF_HIDBRUTE' 'HF_YOUNG' 'HF_MATTYRUN')
  RDV4_STANDALONE_MODES=('HF_COLIN' 'HF_BOG')
 
  # Build recovery (without PLATFORM_EXTRAS and STANDALONE)
  make -j DESTDIR="build" PREFIX="/usr" \
    PLATFORM="PM3RDV4" STANDALONE= FWTAG="rdv4-nostandalone" recovery/install
  make -j DESTDIR="build" PREFIX="/usr" \
    PLATFORM="PM3OTHER" STANDALONE= FWTAG="other-nostandalone" recovery/install

  # Build various firmwares
  for standalone in ${STANDALONE_MODES[@]}; do

      make -j DESTDIR="build" PREFIX="/usr" \
        PLATFORM="PM3RDV4" PLATFORM_EXTRAS="BTADDON" STANDALONE="${standalone}" \
        FWTAG="rdv4-"$(echo ${standalone} | tr '[:upper:]' '[:lower:]') fullimage/install

      make -j DESTDIR="build" PREFIX="/usr" \
        PLATFORM="PM3OTHER" STANDALONE="${standalone}" \
        FWTAG="other-"$(echo ${standalone} | tr '[:upper:]' '[:lower:]') fullimage/install

  done

  for standalone in ${RDV4_STANDALONE_MODES[@]}; do

      make -j DESTDIR="build" PREFIX="/usr" \
        PLATFORM="PM3RDV4" PLATFORM_EXTRAS="BTADDON" STANDALONE="${standalone}" \
        FWTAG="rdv4-"$(echo ${standalone} | tr '[:upper:]' '[:lower:]') fullimage/install

  done

  make clean
  # Build other targets
  make -j1 DESTDIR="build" PREFIX="/usr" \
    PLATFORM="PM3RDV4" PLATFORM_EXTRAS="BTADDON" STANDALONE="${standalone}" \
    FWTAG="rdv4-"$(echo ${standalone} | tr '[:upper:]' '[:lower:]') install

  # Don't need this recovery
  make -j DESTDIR="build" PREFIX="/usr" \
    PLATFORM="PM3RDV4" PLATFORM_EXTRAS="BTADDON" STANDALONE="${standalone}" \
    FWTAG="rdv4-"$(echo ${standalone} | tr '[:upper:]' '[:lower:]') recovery/uninstall

}

package() {
  cd "${srcdir}/${pkgname}"
  mv build/* "${pkgdir}/"
}
