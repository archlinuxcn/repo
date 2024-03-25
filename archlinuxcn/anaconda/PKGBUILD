# Maintainer: Jingbei Li <i@jingbei.li>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: kastik <kastik69420@gmail.com>
# Contributor: Ismaël Bouya <ismael.bouya@normalesup.org>
# Contributor: Martin Wimpress <code@flexion.org>
pkgname=anaconda
pkgver=2024.02.1
_pkgver=${pkgver%.*}-${pkgver##*.}
pkgrel=1
pkgdesc="Simplifies package management and deployment of Anaconda"
arch=(x86_64 aarch64)
url="https://${pkgname}.com"
license=('custom')
provides=('conda')
optdepends=('libxau: for Anaconda Navigator support'
  'libxi: for Anaconda Navigator support'
  'libxss: for Anaconda Navigator support'
  'libxtst: for Anaconda Navigator support'
  'libxcursor: for Anaconda Navigator support'
  'libxcomposite: for Anaconda Navigator support'
  'libxdamage: for Anaconda Navigator support'
  'libxfixes: for Anaconda Navigator support'
  'libxrandr: for Anaconda Navigator support'
  'libxrender: for Anaconda Navigator support'
  'mesa: for Anaconda Navigator support'
  'alsa-lib: for Anaconda Navigator support'
  'libglvnd: for Anaconda Navigator support'
  'xdg-utils: for ')
source=(${pkgname}-navigator.desktop)
source_x86_64=(https://repo.${pkgname}.com/archive/Anaconda3-${_pkgver}-Linux-x86_64.sh)
source_aarch64=(https://repo.${pkgname}.com/archive/Anaconda3-${_pkgver}-Linux-aarch64.sh)
options=(!strip libtool staticlibs)
sha512sums=('5822dd55b1668b166134ec6dc414b3ad13f34c4271e9dba8d2d4adb34440c8b664ce5b6f2b6bb9752f5ec115d8671015fca035f2f94c92d5ce8aba2a1782a9d5')
sha512sums_x86_64=('a51008bb8534d1ed6b5cff2b9b818af6908f8e8faadfb7d75fcadc8ed6bca8ffab1bb00ba4a659935076e06df153752742e23eee7baccc32e75142e705d8c567')
sha512sums_aarch64=('7d26e607f31bf9da0c4454755a8271dc04f94b8cd84c5211fadbc2a7266d570e8c6dadd3663b61e3f93737216fe238fac37a45e877de1fc006862a749b53c2d1')
install="${pkgname}.install"

package() {
  prefix="${pkgdir}"/opt/${pkgname}
  LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

  # Packaging anaconda for installation to /opt/anaconda
  bash "${srcdir}"/Anaconda3-${_pkgver}-Linux-${CARCH}.sh -b -p $prefix -f
  [ "$BREAK_EARLY" = 1 ] && exit 1
  cd $prefix

  # Correcting permissions
  chmod a+r -R pkgs

  # Stripping $pkgdir
  sed -e "s|${pkgdir}||g" -i $(grep "${pkgdir}" . -rIl 2>/dev/null)

  # Installing license
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"

  # Installing .desktop for anaconda navigator
  install -Dm 644 "${srcdir}/${pkgname}-navigator.desktop" -t "${pkgdir}"/usr/share/applications/
}
