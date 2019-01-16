# Maintainer: FadeMind <fademind@gmail.com>
# Contributor: Que Quotion <quequotion@bugmenot.com>
# Contributor: Jameson Pugh <imntreal@gmail.com>

_pkgbasename=python2
pkgname=lib32-$_pkgbasename
pkgver=2.7.15
pkgrel=1
_pybasever=2.7
pkgdesc="A high-level scripting language (32 bit)"
arch=('x86_64')
license=('PSF')
url="https://www.python.org/"
depends=(lib32-{bzip2,db,expat,gdbm,libffi,openssl,sqlite,zlib} python2)
makedepends=('lib32-tk')
optdepends=('lib32-tk: for IDLE')
conflicts=('lib32-python<3')
options=('!makeflags')
source=("https://www.python.org/ftp/python/${pkgver%rc?}/Python-${pkgver}.tar.xz"
        'descr_ref.patch' 'python-config-32.patch' 'lib32-distutils-sysconfig.patch')
sha256sums=('22d9b1ac5b26135ad2b8c2901a9413537e08749a753356ee913c84dbd2df5574'
            '8f84c2efd9963541a55e2caccbb2651a132430c49f9e66e8e299a9e34e1c74b8'
            '227230f73a2144f997c8246576e514783749b4432b45256765eee0193864f1eb'
            '54b58eb8d0083c9ff751763180e9951b776dfa0c65e6391b000c56a538e20ad9')

prepare() {
  cd "${srcdir}/Python-${pkgver}"
  
  # Enable built-in SQLite3 module to load extensions (fix FS#22122)
  sed -i "/SQLITE_OMIT_LOAD_EXTENSION/d" setup.py
 
  # Ensure that we are using the system copy of various libraries (expat, zlib and libffi),
  # rather than copies shipped in the tarball
  rm -r Modules/expat
  rm -r Modules/zlib
  rm -r Modules/_ctypes/{darwin,libffi}*
  
  # FS#48761
  # http://bugs.python.org/issue25750
  patch -Np1 -i "${srcdir}/descr_ref.patch"
  
  # Here start the patches lib32 specific
  
  # Temporary workaround for FS#22322
  # See http://bugs.python.org/issue10835 for upstream report
  sed -i "/progname =/s/python/python${_pybasever}-32/" Python/pythonrun.c
  
  # FS#23997
  sed -i -e "s|^#.* /usr/local/bin/python|#!/usr/bin/python2-32|" Lib/cgi.py
  
  # Just how many places does one have to patch Python?
  patch -Np2 < "${srcdir}/lib32-distutils-sysconfig.patch"

  # Give the configuration script an extention
  patch -Np2 < "${srcdir}/python-config-32.patch"

  # Fix hard-coded paths
  sed -i "s|base}/lib|base}/lib32|g" "${srcdir}/Python-${pkgver}/Lib/sysconfig.py"
  sed -i "s|/include|/lib32/python{py_version_short}/include|g" "${srcdir}/Python-${pkgver}/Lib/sysconfig.py"
  sed -i "s|lib/|lib32/|g" "${srcdir}/Python-${pkgver}/Modules/getpath.c"
  sed -i "s|base/lib|base/lib32|g" "${srcdir}/Python-${pkgver}/Lib/distutils/command/install.py"
  sed -i "s|/include|/lib32/python{py_version_short}/include|g" "${srcdir}/Python-${pkgver}/Lib/distutils/command/install.py"
  sed -i "s|prefix)/lib|prefix)/lib32|g" "${srcdir}/Python-${pkgver}/Makefile.pre.in"
}

build() {
  cd "${srcdir}/Python-${pkgver}"

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export LDFLAGS='-m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  export OPT="${CFLAGS}"
  ./configure --prefix=/usr \
              --enable-shared \
              --with-threads \
              --enable-optimizations \
              --with-lto \
              --enable-ipv6 \
              --enable-unicode=ucs4 \
              --with-system-expat \
              --with-system-ffi \
              --with-dbmliborder=gdbm:ndbm \
              --without-ensurepip \
              --libdir=/usr/lib32 \
              --libexecdir=/usr/lib32 \
              --includedir=/usr/lib32/python${_pybasever}/include \
              --exec_prefix=/usr/lib32/python${_pybasever}/ \
              --bindir=/usr/bin \
              --sbindir=/usr/bin \
              --with-suffix='-32'
  make
}
 
package() {
  cd "${srcdir}/Python-${pkgver}"
 
  make DESTDIR="${pkgdir}" altinstall
 
  ln -sf ../../libpython${_pybasever}.so "${pkgdir}"/usr/lib32/python${_pybasever}/config/libpython${_pybasever}.so
 
  mv "${pkgdir}"/usr/bin/smtpd.py "${pkgdir}"/usr/lib32/python${_pybasever}/
 
  # some useful "stuff"
  install -dm755 "${pkgdir}"/usr/lib32/python${_pybasever}/Tools/{i18n,scripts}
  install -m755 Tools/i18n/{msgfmt,pygettext}.py  "${pkgdir}"/usr/lib32/python${_pybasever}/Tools/i18n/
  install -m755 Tools/scripts/{README,*py}    "${pkgdir}"/usr/lib32/python${_pybasever}/Tools/scripts/
  
  # create symlinks
  ln -s python2.7-32     "${pkgdir}"/usr/bin/python2-32
  ln -s python2.7-32-config  "${pkgdir}"/usr/bin/python2-32-config

  # clean up #!s
  find "${pkgdir}"/usr/lib32/python2.7/ -name '*.py' | xargs sed -i "s|#[ ]*![ ]*/usr/bin/env python$|#!/usr/bin/env python2.7-32|"
 
  # clean-up reference to build directory
  sed -i "s#${srcdir}/Python-${pkgver}:##" "${pkgdir}"/usr/lib32/python${_pybasever}/config/Makefile
 
  # Clean up
  rm -rf "${pkgdir}"/{etc,usr/{share,include}} # needs bin/

  # Leave the python binary and configure script for depedants to find the headers
  cd "${pkgdir}"/usr/bin
  rm pydoc idle 2to3
}

