# Maintainer: Alexander Phinikarides (alexisph -at- gmail -dot- com)

pkgname=microsoft-r-open
pkgver=3.5.1
pkgrel=1
_majorver=3.5
_mrandate=2018-08-01
pkgdesc="Language and environment for statistical computing and graphics, enhanced by Microsoft"
arch=('x86_64')
license=('GPL')
url='https://mran.revolutionanalytics.com/open/'
provides=("r=${pkgver}")
conflicts=('r' 'r-mkl')
depends=('bzip2'
        'curl'
        'desktop-file-utils'
        'gcc-libs'
        'icu60'
        'libjpeg'
        'libpng'
        'libpng12'
        'libtiff'
        'libxmu'
        'libxt'
        'ncurses'
        'pango'
        'pcre'
        'perl'
        'readline'
        'unzip'
        'xz'
        'zip'
        'zlib')
makedepends=('java-environment'
            'gcc-fortran'
            'tk')
optdepends=('tk: tcl/tk interface'
            'texlive-bin: latex sty files')
backup=('etc/R/Makeconf'
        'etc/R/Renviron'
        'etc/R/ldpaths'
        'etc/R/repositories'
        'etc/R/javaconf')
options=('!makeflags' '!emptydirs')
install=microsoft-r-open.install
source=("https://mran.blob.core.windows.net/install/mro/${pkgver}/microsoft-r-open-${pkgver}.tar.gz"
        'mro.desktop'
        'mro.png'
        'R.conf')
md5sums=('fd1e4123943cfad35fc85c219c22bb46'
         '70e8f9d0b1eebeb1f0b45f4568bc0701'
         '8e0c51650b8a63f110fa7b09e699e9c4'
         '1dfa62c812aed9642f6e4ac34999b9fe')
sha512sums=('98a1b701b9cdee46a53a6f86468057d7a475bc7ffdc2b1d87c9c1b753c6bede72d53bbc790e8fbd1b2b1dca8561a3a1136ceb0d4764288574efe3b55aead2268'
            '2b0221bd1e0fdd399284333e6f2020bb9ad11395ad39dd2fca688b7ebc68fbbc60de59a757e1898be8bcd9e2926afccc121043f38445e7693f177c3076f92b61'
            '1491b01d3d14b86d26c383e00e2305858a52ddd498158c9f7f6b33026ee01f246408b1676cffea73f7783c8c4cf546285705c43c0286adbd75ad77706918b5fe'
            'aae388c5b6c02d9fb857914032b0cd7d68a9f21e30c39ba11f5a29aaf1d742545482054b57ce18872eabb6605bbb359b2fc1e9be5ce6881443fdbdf6b67fab3b')

prepare() {
  cd ${pkgname}
  # extract rpms
  bsdtar -xf "rpm/${pkgname}-mro-${pkgver}.rpm"
  bsdtar -xf "rpm/${pkgname}-mkl-${pkgver}.rpm"
  bsdtar -xf "rpm/${pkgname}-foreachiterators-${pkgver}.rpm"
}

package() {
  cd ${pkgname}
  mv opt/microsoft/ropen/${pkgver}/lib64 opt/microsoft/ropen/${pkgver}/lib
  mv opt/microsoft/ropen/${pkgver} "${pkgdir}/usr"

  # Install MKL libs
  install -d "${pkgdir}/usr/lib/R/backup/lib"
  mv ${pkgdir}/usr/lib/R/lib/*.so "${pkgdir}/usr/lib/R/backup/lib"
  install -Dm644 "${pkgdir}/usr/lib/R/backup/lib/libR.so" "${pkgdir}/usr/lib/R/lib/libR.so"
  install -Dm644 ${pkgdir}/usr/stage/Linux/bin/x64/*.so "${pkgdir}/usr/lib/R/lib"
  rm -rf ${pkgdir}/usr/stage

  # Link R binaries to system path
  install -d "${pkgdir}/usr/bin"
  cd "${pkgdir}/usr/bin"
  ln -s ../lib/R/bin/R
  ln -s ../lib/R/bin/Rscript

  # Create etc config directory
  install -d "${pkgdir}/etc/R"
  cd "${pkgdir}/usr/lib/R/etc"
  for i in *; do
    mv -f ${i} "${pkgdir}/etc/R"
    ln -s /etc/R/${i} ${i}
  done
  # fix typos
  sed -i "s|IMPLEMENTATIN|IMPLEMENTATION|g" "${pkgdir}/etc/R/Makeconf"
  sed -i "s|3.3|3.4|g" "${pkgdir}/etc/R/Renviron"

  # Ensure other applications can access the shared libs
  install -Dm644 "${srcdir}/R.conf" "${pkgdir}/etc/ld.so.conf.d/R.conf"
  sed -i "s/VERSION/${_majorver}/" "${pkgdir}/etc/ld.so.conf.d/R.conf"

  # Install pkgconfig file
  cd "${pkgdir}/usr/lib/"
  sed -i "s|rhome=.*$|rhome=/usr/lib/R|" pkgconfig/libR.pc
  sed -i "s|rincludedir=.*$|rincludedir=/usr/include/R|" pkgconfig/libR.pc
  sed -i "s|-L/builddir/vendor/build/lib||" pkgconfig/libR.pc

  # Install header files
  install -d "${pkgdir}/usr/include/R"
  cp -r ${pkgdir}/usr/lib/R/include/* "${pkgdir}/usr/include/R/"

  # Install man pages
  cd "${pkgdir}/usr/share/man/man1"
  gzip -9 *

  # Install shared files
  install -d "${pkgdir}/usr/share/R"
  cp -r "${pkgdir}/usr/lib/R/share/dictionaries" "${pkgdir}/usr/share/R/"
  cp -r "${pkgdir}/usr/lib/R/share/encodings" "${pkgdir}/usr/share/R/"
  cp -r "${pkgdir}/usr/lib/R/share/java" "${pkgdir}/usr/share/R/"
  cp -r "${pkgdir}/usr/lib/R/share/licenses" "${pkgdir}/usr/share/R/"
  cp -r "${pkgdir}/usr/lib/R/share/make" "${pkgdir}/usr/share/R/"
  cp -r "${pkgdir}/usr/lib/R/share/R" "${pkgdir}/usr/share/R/"
  cp -r "${pkgdir}/usr/lib/R/share/Rd" "${pkgdir}/usr/share/R/"
  cp -r "${pkgdir}/usr/lib/R/share/sh" "${pkgdir}/usr/share/R/"
  # LaTeX templates
  cp -r "${pkgdir}/usr/lib/R/share/texmf" "${pkgdir}/usr/share/"

  # Install docs
  install -d "${pkgdir}/usr/share/doc/R"
  cp -r ${pkgdir}/usr/lib/R/doc/* "${pkgdir}/usr/share/doc/R/"
  # Copy EULAs
  install -m644 ${srcdir}/${pkgname}/*.txt "${pkgdir}/usr/share/doc/R/"

  # Install freedesktop.org compatibility
  install -Dm644 "${srcdir}/mro.desktop" "${pkgdir}/usr/share/applications/mro.desktop"
  install -Dm644 "${srcdir}/mro.png" "${pkgdir}/usr/share/pixmaps/mro.png"
}

