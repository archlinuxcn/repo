# Maintainer: Nicolas Iooss (nicolas <dot> iooss <at> m4x <dot> org)
# Contributor: Timothée Ravier <tim@siosm.fr>
# Contributor: Nicky726 (Nicky726 <at> gmail <dot> com)
# Contributor: Sergej Pupykin (pupykin <dot> s+arch <at> gmail <dot> com)
# Contributor: Zezadas
#
# This PKGBUILD is maintained on https://github.com/archlinuxhardened/selinux.
# If you want to help keep it up to date, please open a Pull Request there.

pkgname=libselinux
pkgver=2.9
pkgrel=3
pkgdesc="SELinux library and simple utilities"
arch=('i686' 'x86_64' 'armv6h')
url='http://userspace.selinuxproject.org'
license=('custom')
groups=('selinux')
makedepends=('python2' 'python' 'ruby' 'xz' 'swig')
depends=('libsepol>=2.8' 'pcre')
optdepends=('python2: python2 bindings'
            'python: python bindings'
            'ruby: ruby bindings')
conflicts=("selinux-usr-${pkgname}")
provides=("selinux-usr-${pkgname}=${pkgver}-${pkgrel}")
source=("https://github.com/SELinuxProject/selinux/releases/download/20190315/${pkgname}-${pkgver}.tar.gz"
        "libselinux.tmpfiles.d"
        '0001-libselinux-Use-Python-distutils-to-install-SELinux-p.patch'
        '0001-libselinux-Fix-security_get_boolean_names-build-erro.patch')
sha256sums=('1bccc8873e449587d9a2b2cf253de9b89a8291b9fbc7c59393ca9e5f5f4d2693'
            'afe23890fb2e12e6756e5d81bad3c3da33f38a95d072731c0422fbeb0b1fa1fc'
            '47e8c4b6c67d1778bd0a8de782ea6d2406e8de3ad13064c85d53deba222100af'
            '9a0bcf7b8e2ec60fe954d2bbcd527f3b5d34e4cdb898ab19cd8b2ef869eed241')

prepare() {
  cd "${pkgname}-${pkgver}"

  # Backport "libselinux: Use Python distutils to install SELinux python bindings"
  # https://github.com/SELinuxProject/selinux/commit/2efa06857575e4118e91ca250b6b92da68b130d5
  patch -Np2 -i ../0001-libselinux-Use-Python-distutils-to-install-SELinux-p.patch

  # Backport "libselinux: Fix security_get_boolean_names build error"
  # https://github.com/SELinuxProject/selinux/commit/ee8f7a870c625de139aa271eae0c40578488c2f6
  patch -Np2 -i ../0001-libselinux-Fix-security_get_boolean_names-build-erro.patch
}

build() {
  cd "${pkgname}-${pkgver}"

  # Do not build deprecated rpm_execcon() interface. It is useless on Arch Linux anyway.
  export DISABLE_RPM=y

  make swigify
  make all
  make PYTHON=/usr/bin/python2 pywrap
  make PYTHON=/usr/bin/python3 pywrap
  make RUBY=/usr/bin/ruby rubywrap
}

package() {
  cd "${pkgname}-${pkgver}"

  export DISABLE_RPM=y

  make DESTDIR="${pkgdir}" SBINDIR=/usr/bin SHLIBDIR=/usr/lib install
  make DESTDIR="${pkgdir}" PYTHON=/usr/bin/python2 SBINDIR=/usr/bin SHLIBDIR=/usr/lib install-pywrap
  make DESTDIR="${pkgdir}" PYTHON=/usr/bin/python3 SBINDIR=/usr/bin SHLIBDIR=/usr/lib install-pywrap
  make DESTDIR="${pkgdir}" RUBY=/usr/bin/ruby SBINDIR=/usr/bin SHLIBDIR=/usr/lib install-rubywrap
  /usr/bin/python2 -m compileall "${pkgdir}/$(/usr/bin/python2 -c 'from distutils.sysconfig import *; print(get_python_lib(plat_specific=1))')"
  /usr/bin/python3 -m compileall "${pkgdir}/$(/usr/bin/python3 -c 'from distutils.sysconfig import *; print(get_python_lib(plat_specific=1))')"

  install -Dm 0644 "${srcdir}"/libselinux.tmpfiles.d "${pkgdir}"/usr/lib/tmpfiles.d/libselinux.conf

  install -Dm 0644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
