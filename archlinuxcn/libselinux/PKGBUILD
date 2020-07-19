# Maintainer: Nicolas Iooss (nicolas <dot> iooss <at> m4x <dot> org)
# Contributor: Timothée Ravier <tim@siosm.fr>
# Contributor: Nicky726 (Nicky726 <at> gmail <dot> com)
# Contributor: Sergej Pupykin (pupykin <dot> s+arch <at> gmail <dot> com)
# Contributor: Zezadas
#
# This PKGBUILD is maintained on https://github.com/archlinuxhardened/selinux.
# If you want to help keep it up to date, please open a Pull Request there.

pkgname=libselinux
pkgver=3.1
pkgrel=1
pkgdesc="SELinux library and simple utilities"
arch=('i686' 'x86_64' 'armv6h')
url='https://github.com/SELinuxProject/selinux'
license=('custom')
groups=('selinux')
makedepends=('pkgconf' 'python' 'ruby' 'xz' 'swig')
depends=('libsepol>=3.1' 'pcre')
optdepends=('python: python bindings'
            'ruby: ruby bindings')
conflicts=("selinux-usr-${pkgname}")
provides=("selinux-usr-${pkgname}=${pkgver}-${pkgrel}")
source=("https://github.com/SELinuxProject/selinux/releases/download/20200710/${pkgname}-${pkgver}.tar.gz"
        "libselinux.tmpfiles.d")
sha256sums=('ea5dcbb4d859e3f999c26a13c630da2f16dff9462e3cc8cb7b458ac157d112e7'
            'afe23890fb2e12e6756e5d81bad3c3da33f38a95d072731c0422fbeb0b1fa1fc')

build() {
  cd "${pkgname}-${pkgver}"

  # Do not build deprecated rpm_execcon() interface. It is useless on Arch Linux anyway.
  export DISABLE_RPM=y

  export CFLAGS="${CFLAGS} -fno-semantic-interposition"
  make swigify
  make all
  make PYTHON=/usr/bin/python3 pywrap
  make RUBY=/usr/bin/ruby rubywrap
}

package() {
  cd "${pkgname}-${pkgver}"

  export DISABLE_RPM=y

  make DESTDIR="${pkgdir}" SBINDIR=/usr/bin SHLIBDIR=/usr/lib install
  make DESTDIR="${pkgdir}" PYTHON=/usr/bin/python3 SBINDIR=/usr/bin SHLIBDIR=/usr/lib install-pywrap
  make DESTDIR="${pkgdir}" RUBY=/usr/bin/ruby SBINDIR=/usr/bin SHLIBDIR=/usr/lib install-rubywrap
  /usr/bin/python3 -m compileall "${pkgdir}/$(/usr/bin/python3 -c 'from distutils.sysconfig import *; print(get_python_lib(plat_specific=1))')"

  install -Dm 0644 "${srcdir}"/libselinux.tmpfiles.d "${pkgdir}"/usr/lib/tmpfiles.d/libselinux.conf

  install -Dm 0644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
