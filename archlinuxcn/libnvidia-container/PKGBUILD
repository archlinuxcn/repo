# Maintainer: Julie Shapiro <jshapiro at nvidia dot com>
# Maintainer: Kien Dang <mail at kien dot ai>

pkgbase=libnvidia-container
pkgname=(libnvidia-container libnvidia-container-tools)

pkgver=1.13.5
pkgrel=1
_elfver=0.7.1
_nvmpver=495.44

pkgdesc='NVIDIA container runtime library'
arch=('x86_64')
url='https://github.com/NVIDIA/libnvidia-container'
license=('Apache')

makedepends=(go bmake lsb-release rpcsvc-proto pkgconf)
depends=(libcap libseccomp libtirpc)

# yikes! somehow the default flags cause a linking error :(
options=(!makeflags !lto)

# This make process downloads files from other sources to build the libs as deps cleanly in place.
# This pkgbuild elects to download them ahead of time so their checksums can be validated.
# See:
# https://github.com/NVIDIA/libnvidia-container/blob/c8f267be0bac1c654d59ad4ea5df907141149977/mk/elftoolchain.mk
# https://github.com/NVIDIA/libnvidia-container/blob/c8f267be0bac1c654d59ad4ea5df907141149977/mk/nvidia-modprobe.mk
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/NVIDIA/${pkgbase}/archive/v${pkgver}.tar.gz"
        "${pkgname}-${pkgver}-elftoolchain-${_elfver}.tar.bz2::https://sourceforge.net/projects/elftoolchain/files/Sources/elftoolchain-${_elfver}/elftoolchain-${_elfver}.tar.bz2"
        "${pkgname}-${pkgver}-nvidia-modprobe-${nvmpver}.tar.gz::https://github.com/NVIDIA/nvidia-modprobe/archive/${_nvmpver}.tar.gz"
        fix_rpc_flags.patch
        fix_git_rev_unavail.patch
        fix_libelf_so_name.patch
        fix_elftoolchain.patch)
sha256sums=('431522239d71728d2840b2f048d0a0733c3e6ad7a209bdf21c7d17c0aa661657'
            '44f14591fcf21294387215dd7562f3fb4bec2f42f476cf32420a6bbabb2bd2b5'
            'ae6e9c7e6b43368945c28f6b8b6d0d7cc36ee7e1be8955a009a1cb189e46de92'
            '6738c0f8738cb272ee5c723e77008f5f512be842bad26abc2e8f78911131165a'
            '12986dd405971dd2af9cd8ab0c75db37e09c8ec0657f1b148d59822831b8e40e'
            '42412db6bbcf0c2f76c426b6f51cf12eda6a78b5c9c64d29e9a80739790ea6b9'
            '1af7dcdc7f13cac3ddf1f4b4c7b225d8cd7f8407915b63aacea736a2a751db46')

_srcdir="${pkgname}-${pkgver}"

prepare(){
  cd ${_srcdir}

  patch -Np1 -i "${srcdir}/fix_rpc_flags.patch"
  patch -Np1 -i "${srcdir}/fix_git_rev_unavail.patch"
  patch -Np1 -i "${srcdir}/fix_libelf_so_name.patch"

  deps_dir="deps/src/"
  mkdir -p "${deps_dir}"
  # mimic behavior from:
  # https://github.com/NVIDIA/libnvidia-container/blob/56704b8dd297bf4daf82a2da4b270dc7f14e0008/mk/libtirpc.mk
  for dep in "elftoolchain-${_elfver}" "nvidia-modprobe-${_nvmpver}"; do
    mv "${srcdir}/${dep}" "${deps_dir}"
    touch "${deps_dir}/${dep}/.download_stamp"
  done

  patch -Np1 -i "${srcdir}/fix_elftoolchain.patch"
  patch -d "${deps_dir}/nvidia-modprobe-${_nvmpver}" -p1 < "mk/nvidia-modprobe.patch"
}

build(){
  cd ${_srcdir}

  export MAKESYSPATH=/usr/share/mk

  # finally actually make
  CC=gcc make
}

make_dist(){
  cd ${_srcdir}
  # package
  make dist prefix=/usr

  # untar into $pkgdir
  tar -xf "${srcdir}/${_srcdir}/dist/${pkgbase}_${pkgver}_x86_64.tar.xz" -C ${pkgdir} --strip-components=1
}

package_libnvidia-container() {
  make_dist

  # cleanup
  rm -rf "${pkgdir}/usr/lib/debug"
  rm -rf "${pkgdir}/usr/lib/pkgconfig"

  # save bin/ for -tools
  rm -rf "${pkgdir}/usr/bin"

  #mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  #install -D -m644 "${pkgdir}/usr/share/doc/${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/"
  #rm -rf "${pkgdir}/usr/share/doc"
  rm -rf "${pkgdir}/usr/share"
}

package_libnvidia-container-tools() {
  depends=(libnvidia-container)

  make_dist

  # cleanup
  rm -rf "${pkgdir}/usr/lib/debug"
  rm -rf "${pkgdir}/usr/lib/pkgconfig"

  # save lib/ and include/ for -tools
  rm -rf "${pkgdir}/usr/lib"
  rm -rf "${pkgdir}/usr/include"

  #mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  #install -D -m644 "${pkgdir}/usr/share/doc/${pkgbase}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/"
  #rm -rf "${pkgdir}/usr/share/doc"
  rm -rf "${pkgdir}/usr/share"
}

# vim:set ts=2 sw=2 et:
