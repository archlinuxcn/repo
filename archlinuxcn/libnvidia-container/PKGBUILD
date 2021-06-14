# Maintainer: Joel Shapiro <jshapiro at nvidia dot com>
# Maintainer: Kien Dang <mail at kien dot ai>

pkgbase=libnvidia-container
pkgname=(libnvidia-container libnvidia-container-tools)

pkgver=1.4.0
pkgrel=1
_elfver=0.7.1
_nvmpver=450.57

pkgdesc='NVIDIA container runtime library'
arch=('x86_64')
url='https://github.com/NVIDIA/libnvidia-container'
license=('Apache')

makedepends=(bmake lsb-release rpcsvc-proto pkgconf)
depends=(libcap libseccomp libtirpc)

# yikes! somehow the default flags cause a linking error :(
options=(!makeflags)

# This make process downloads files from other sources to build the libs as deps cleanly in place.
# This pkgbuild elects to download them ahead of time so their checksums can be validated.
# See:
# https://github.com/NVIDIA/libnvidia-container/blob/e3a2035da5a44b8a83d9568b91a8a0b542ee15d5/mk/elftoolchain.mk
# https://github.com/NVIDIA/libnvidia-container/blob/56704b8dd297bf4daf82a2da4b270dc7f14e0008/mk/nvidia-modprobe.mk
source=("https://github.com/NVIDIA/${pkgbase}/archive/v${pkgver}.tar.gz"
        "https://sourceforge.net/projects/elftoolchain/files/Sources/elftoolchain-${_elfver}/elftoolchain-${_elfver}.tar.bz2"
        "https://github.com/NVIDIA/nvidia-modprobe/archive/${_nvmpver}.tar.gz"
        fix_rpc_flags.patch
        fix_git_rev_unavail.patch
        fix_libelf_so_name.patch
        fix_elftoolchain.patch)
sha256sums=('5cf5a9054aeae53f48556c31856f9aabc51b35749f7d815356974c051911bdb7'
            '44f14591fcf21294387215dd7562f3fb4bec2f42f476cf32420a6bbabb2bd2b5'
            '396b4102d3075a2dee3024652fae206a1b38ace54b8efb1e2c20757a11ec19f1'
            'c8c600d753d1f98464667d56e011b868eed3c8364280ed33c0435974f800d3bb'
            '48edab623a44e42d3310c87bf38df56878e68146ae4ac446c28d460fa0a4385b'
            '42412db6bbcf0c2f76c426b6f51cf12eda6a78b5c9c64d29e9a80739790ea6b9'
            '1af7dcdc7f13cac3ddf1f4b4c7b225d8cd7f8407915b63aacea736a2a751db46')

_srcdir="${pkgname}-${pkgver}"

prepare(){
  cd ${_srcdir}

  patch -Np1 -i "${srcdir}/fix_rpc_flags.patch"
  patch -Np1 -i "${srcdir}/fix_git_rev_unavail.patch"
  patch -Np1 -i "${srcdir}/fix_libelf_so_name.patch"

  deps_dir="deps/src/"
  # mimic behavior from:
  # https://github.com/NVIDIA/libnvidia-container/blob/56704b8dd297bf4daf82a2da4b270dc7f14e0008/mk/libtirpc.mk
  for dep in "elftoolchain-${_elfver}.tar.bz2" "${_nvmpver}.tar.gz"; do
    dep_dir="${deps_dir}/${dep%.tar*}"
    mkdir -p ${dep_dir}
    # untar the download into the deps dir
    tar -xf "${srcdir}/${dep}" -C "${dep_dir}" --strip-components=1
    # tell make to ignore this target, it's already done
    touch "${dep_dir}/.download_stamp"
  done

  patch -Np1 -i "${srcdir}/fix_elftoolchain.patch"

  # the tar isn't named correctly, so the dir needs moving
  if [ ! -d "${deps_dir}/nvidia-modprobe-${_nvmpver}" ]; then
    mv "${deps_dir}/${_nvmpver}" "${deps_dir}/nvidia-modprobe-${_nvmpver}"
    patch -d "${deps_dir}/nvidia-modprobe-${_nvmpver}" -p1 < "mk/nvidia-modprobe.patch"
  fi
}

build(){
  cd ${_srcdir}

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
