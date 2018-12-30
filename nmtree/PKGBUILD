# Maintainer: brent s. <bts[at]square-r00t[dot]net>
validpgpkeys=('748231EBCBD808A14F5E85D28C004C2F93481F6B')
# Bug reports can be filed at https://bugs.square-r00t.net/index.php?project=3
# News updates for packages can be followed at https://devblog.square-r00t.net
# A HUGE THANKS to @yan12125 on GitHub (https://github.com/archiecobbs/mtree-port/issues/11#issuecomment-343127667)
#  This is basically the PKGBUILD he wrote, all credit goes to him. Buy him a beer.
pkgname=nmtree
pkgver=20171109
pkgrel=4
pkgdesc="NetBSD's mtree (supports legacy mtree spec, newer specs, etc.)"
arch=( 'i686' 'x86_64' )
url="https://www.netbsd.org/"
license=( 'custom' )
makedepends=( 'bmake' 'cvs' 'libnbcompat' )
_pkgname=mtree
provides=('mtree' 'mtree-git')
conflicts=('mtree' 'mtree-git')
install=
changelog=
noextract=()
# We don't use a source since we use cvs
source=('license'
	'maj_min.patch'
	'license.sig'
	'maj_min.patch.sig')
sha512sums=('78f634baef190d4a52187e69344e50ae9544c95bd6243ebb22af727092edbb61c021ec38de1a85e38b08cb046b71bdbf6cc869af2d9a6365cb93c92e342dfe96'
	    '57daf0457877c5cfa0c9cddf3840d489e36de449cab417ee6a7197dc71a6fbc818900bbc133042bd4519ffa712b446e7791993e6ff1a67473a4c360ec3e35212'
	    'SKIP'
	    'SKIP')

_cvsroot=":pserver:anoncvs@anoncvs.NetBSD.org:/cvsroot"
_cvsmod="pkgsrc/pkgtools/${_pkgname}/files"

prepare() {
  cd "${srcdir}"

  # CHECK OUT SOURCE
  msg "Connecting to NetBSD CVS server...."

  if [[ -d "${_cvsmod}/CVS" ]]; then
    cd "${_cvsmod}"
    cvs -z3 update -d
  else
    cvs -z3 -d "${_cvsroot}" co -D "${pkgver}" -f "${_cvsmod}"
    cd "${_cvsmod}"
  fi

  msg "CVS checkout done or server timeout"
  msg "Starting build..."

  rm -rf "${srcdir}/${_cvsmod}-build"
  cp -r "${srcdir}/${_cvsmod}" "${srcdir}/${_cvsmod}-build"

  cd "${srcdir}/${_cvsmod}-build"

  # APPLY PATCHES
  patch -N < ${srcdir}/maj_min.patch

}

build() {
  cd "${srcdir}/${_cvsmod}-build"

  ./configure --prefix=/usr --sbindir=/usr/bin LIBS="-lnbcompat"

  bmake
}
package() {
  cd "${srcdir}/${_cvsmod}-build"
  bmake install DESTDIR="${pkgdir}/"
  install -D -m 0644 ${srcdir}/license ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
}
