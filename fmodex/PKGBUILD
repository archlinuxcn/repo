# $Id$
# Maintainer: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: Christoph Zeiler <archNOSPAM_at_moonblade.dot.org>

# Note: This packae is proprietary and distribution is limited. However, we
# have written permission to by the FMOD CEO to distribute this in binary form.
pkgname=fmodex
pkgver=4.44.58
pkgrel=1
pkgdesc="An advanced audio engine"
arch=('i686' 'x86_64')
url="http://www.fmod.org/"
license=('custom')
source=("fmodapi44458linux.tar.gz::https://www.dropbox.com/s/0z62kk2p79gs6bh/fmodapi44458linux.tar.gz?dl=1")
## source=fmodapi44433linux.tar.gz?dl=1
md5sums=('SKIP')

package() {
  cd fmodapi${pkgver//./}linux

  mkdir -p ${pkgdir}/usr/lib
  mkdir -p ${pkgdir}/usr/include/fmodex

  cp -d api/lib/* ${pkgdir}/usr/lib/
  [[ $CARCH == "i686" ]] && rm ${pkgdir}/usr/lib/*64*

  if [[ $CARCH == "x86_64" ]]; then
    cd ${pkgdir}/usr/lib
    ln -sf libfmodex64-${pkgver}.so libfmodex-${pkgver}.so
    ln -sf libfmodexL64-${pkgver}.so libfmodexL-${pkgver}.so
    cd ${srcdir}/fmodapi${pkgver//./}linux
  fi

  cp api/inc/* ${pkgdir}/usr/include/fmodex/

  install -Dm644 documentation/LICENSE.TXT ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE

  mkdir -p ${pkgdir}/usr/share/doc/fmodex
  cp -r documentation examples ${pkgdir}/usr/share/doc/fmodex
}

# vim:set ts=2 sw=2 et:
