# Maintainer: edward-p <edward At edward-p Dot xyz>

pkgname=proxmark3-iceman-git
pkgver=8267.9f787fae
pkgrel=1
pkgdesc='RRG / Iceman repo - Proxmark3 RDV4.0 and other Proxmark3 platforms.'
arch=('x86_64')
url='https://github.com/RfidResearchGroup/proxmark3'
license=('GPL2')
depends=('perl' 'python' 'libsndfile')
makedepends=('git' 'arm-none-eabi-gcc' 'arm-none-eabi-newlib')
options=(!buildflags)
provides=('proxmark3' 'proxmark3-iceman')
conflicts=('proxmark3' 'proxmark3-iceman')
replaces=($pkgname'-generic' $pkgname'-rdv4')
source=("$pkgname::git+https://github.com/RfidResearchGroup/proxmark3.git")
sha512sums=('SKIP')
install=proxmark3-iceman-git.install

pkgver() {
  cd $pkgname
  echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

build() {
  export DESTDIR="build"
  export PREFIX="/usr"
  export UDEV_PREFIX="/usr/lib/udev/rules.d"
  
  cd "${srcdir}/${pkgname}"

  mkdir "$DESTDIR"
  
  STANDALONE_MODES=(
          'LF_SAMYRUN'
          #'LF_ICERUN'
          'LF_PROXBRUTE'
          'LF_HIDBRUTE'
          'HF_YOUNG'
          'HF_MATTYRUN')
  RDV4_STANDALONE_MODES=('HF_COLIN' 'HF_BOG')
 
  # Build recovery (without PLATFORM_EXTRAS and STANDALONE)
  make \
    PLATFORM="PM3RDV4" STANDALONE= FWTAG="rdv4-nostandalone" recovery/install
  make \
    PLATFORM="PM3OTHER" STANDALONE= FWTAG="other-nostandalone" recovery/install

  # These firmware is not needed.
  # rm build/usr/share/proxmark3/firmware/{fullimage-rdv4-nostandalone.elf,fullimage-other-nostandalone.elf}

  # Build various firmwares
  for standalone in ${STANDALONE_MODES[@]}; do

      make \
        PLATFORM="PM3RDV4" PLATFORM_EXTRAS="BTADDON" STANDALONE="${standalone}" \
        FWTAG="rdv4-"$(echo ${standalone} | tr '[:upper:]' '[:lower:]') armsrc/install

      make \
        PLATFORM="PM3OTHER" STANDALONE="${standalone}" \
        FWTAG="other-"$(echo ${standalone} | tr '[:upper:]' '[:lower:]') armsrc/install

  done

  for standalone in ${RDV4_STANDALONE_MODES[@]}; do

      make \
        PLATFORM="PM3RDV4" PLATFORM_EXTRAS="BTADDON" STANDALONE="${standalone}" \
        FWTAG="rdv4-"$(echo ${standalone} | tr '[:upper:]' '[:lower:]') armsrc/install

  done

  # Build & install other targets
  make {bootrom,client,mfkey,nonce2key,common}/install
}

package() {
  export DESTDIR="build"
  cd "${srcdir}/${pkgname}"
  mv "$DESTDIR"/* "${pkgdir}/"
}
