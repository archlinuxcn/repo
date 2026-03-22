# Maintainer: Ruben Di Battista <rubendibattista@gmail.com>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
## Based on mambaforge aur package by Ashwin Vishn Immae, Martin Wimpress and Jingbei Li
pkgname=miniforge
pkgver=26.1.1.3
_pkgver=${pkgver%.*}-${pkgver##*.}
pkgrel=1
pkgdesc="Conda and Mamba package managers configured to use conda-forge"
arch=(x86_64 aarch64 powerpc64le)
url="https://github.com/conda-forge/miniforge"
license=(BSD-3-Clause)
provides=(conda mamba)
replaces=(mambaforge)
source_x86_64=(${url}/releases/download/${_pkgver}/Miniforge3-${_pkgver}-Linux-x86_64.sh)
source_aarch64=(${url}/releases/download/${_pkgver}/Miniforge3-${_pkgver}-Linux-aarch64.sh)
source_powerpc64le=(${url}/releases/download/${_pkgver}/Miniforge3-${_pkgver}-Linux-ppc64le.sh)
options=(!strip libtool staticlibs)
sha256sums_x86_64=('b25b828b702df4dd2a6d24d4eb56cfa912471dd8e3342cde2c3d86fe3dc2d870')
sha256sums_aarch64=('83280e4ee71a5bd547d6b318f96e9ababe1054911ff6cc2b8801ce5493fe67e5')
sha256sums_powerpc64le=('5711fd69219bc9746389ef751ee4c2549d40d9b1626a0ea93cc63db1a739eee6')
install="${pkgname}.install"

package() {
  prefix="${pkgdir}/opt/${pkgname}"
  LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

  # Packaging mambaforge for installation to /opt/mambaforge
  bash "${srcdir}/Miniforge3-${_pkgver}-Linux-${CARCH}.sh" -b -p $prefix -f
  [ "$BREAK_EARLY" = 1 ] && exit 1
  cd "${prefix}"

  # Correcting permissions
  chmod a+r -R pkgs

  # Stripping $pkgdir
  sed "s|${pkgdir}||g" -i $(grep "$pkgdir" . -rIl)

  # Set string path to a certificate SSL connection
  echo "ssl_verify: /opt/${pkgname}/ssl/cacert.pem" >>"${pkgdir}/opt/${pkgname}/.condarc"

  # Installing license
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
