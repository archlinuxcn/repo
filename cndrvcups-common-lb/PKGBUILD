# Maintainer : Lone_Wolf lonewolf@xs4all.nl
# Contributor: Steven She <mintcoffee@gmail.com>
# Contributor: vbPadre <vbpadre@gmail.com>

pkgbase=cndrvcups-common-lb
pkgname=cndrvcups-common-lb
# used this name to avoid conflict with the existing cndrvcups-common (no longer in aur) which was wrong version for cndrvcups-lb
_pkgname=cndrvcups-common
pkgver=3.71
pkgrel=1
pkgdesc="Common printer driver modules for cndrvcups-lb package, built from source"
arch=('i686' 'x86_64')
url="http://support-au.canon.com.au/contents/AU/EN/0100270808.html"
license=('GPL' 'MIT' 'custom')
depends_i686=('libglade' 'gcc-libs')
depends_x86_64=('libglade' 'lib32-gcc-libs')
makedepends=('automake' 'autoconf' 'glib2' 'gtk2')
conflicts=('cndrvcups-lb-bin')
# http://pdisp01.c-wss.com/gdl/WWUFORedirectTarget.do?id=MDEwMDAwMjcwODE0&cmp=ABS&lang=EN
#source=(Linux_UFRII_PrinterDriver_V320_uk_EN.tar.gz::'http://pdisp01.c-wss.com/gdl/WWUFORedirectTarget.do?id=MDEwMDAwMjcwODE0&cmp=ABS&lang=EN')
source=(http://gdlp01.c-wss.com/gds/8/0100007658/03/linux-UFRII-drv-v331-uken.tar.gz)
options=('!emptydirs' '!strip' 'staticlibs')
sha512sums=('db110d29011b356ab0df1534b0cab6be6dd224a076aef87bfb2f4add4d580c11e2a7aac2b622638b0e70abd0f36a7bf9f0832cf6c4fdacdeba3de99a375bb103')

# build instructions are adapted from upstream cndrvcups-common.spec file

prepare() {
    cd "${srcdir}"/linux-UFRII-drv-v331-uken/Sources
    bsdtar xf "${_pkgname}"-"${pkgver}"-1.tar.gz -C "${srcdir}"
}

build() {

    cd "${srcdir}"/"${_pkgname}"-"${pkgver}"/buftool
    autoreconf -i
    ./autogen.sh --prefix=/usr/ --enable-progpath=/usr/bin --libdir=/usr/lib

    cd "${srcdir}"/"${_pkgname}"-"${pkgver}"/cngplp
    autoreconf -i
    LIBS="-lgtk-x11-2.0 -lgobject-2.0 -lglib-2.0 -lgmodule-2.0" ./autogen.sh --prefix=/usr --libdir=/usr/lib

    cd "${srcdir}"/"${_pkgname}"-"${pkgver}"/backend
    autoreconf -i
    ./autogen.sh --prefix=/usr --libdir=/usr/lib

    cd "${srcdir}"/"${_pkgname}"-"${pkgver}"
    make

    cd "${srcdir}"/"${_pkgname}"-"${pkgver}"/c3plmod_ipc
    make 
}
package()
{

    cd "${srcdir}"/"${_pkgname}"-"${pkgver}"
    mkdir -p "${pkgdir}"/usr/{bin,lib/cups/backend,include}
    
    if [[ ${CARCH} == "i686" ]]; then
      _lib32dir="lib"
    else
      _lib32dir="lib32"
      mkdir -p "${pkgdir}"/usr/"${_lib32dir}"
    fi

    mkdir -p "${pkgdir}"/usr/share/{caepcm,cngplp,locale/ja/LC_MESSAGES}

    make install DESTDIR="${pkgdir}"

    cd c3plmod_ipc
    make install DESTDIR="${pkgdir}" LIBDIR=/usr/lib
    cd ..

    install -m 755 libs/libcaiowrap.so.1.0.0   "${pkgdir}"/usr/"${_lib32dir}"
    install -m 755 libs/libcaiousb.so.1.0.0    "${pkgdir}"/usr/"${_lib32dir}"

    install -m 755 libs/libc3pl.so.0.0.1     "${pkgdir}"/usr/"${_lib32dir}"
    install -m 755 libs/libcaepcm.so.1.0     "${pkgdir}"/usr/"${_lib32dir}"

    install -m 755 libs/libColorGear.so.0.0.0    "${pkgdir}"/usr/"${_lib32dir}"
    install -m 755 libs/libColorGearC.so.1.0.0    "${pkgdir}"/usr/"${_lib32dir}"


    install -m 644 data/*.ICC  "${pkgdir}"/usr/share/caepcm
    install -m 644 data/*.PRF  "${pkgdir}"/usr/share/caepcm

    install -s -m 755 libs/c3pldrv     "${pkgdir}"/usr/bin

    install -m 755 libs/libcanon_slim.so.1.0.0   "${pkgdir}"/usr/"${_lib32dir}"

    cd "${pkgdir}"/usr/"${_lib32dir}"
    ln -sf libc3pl.so.0.0.1     libc3pl.so.0
    ln -sf libc3pl.so.0.0.1     libc3pl.so
    ln -sf libcaepcm.so.1.0     libcaepcm.so.1
    ln -sf libcaepcm.so.1.0     libcaepcm.so
    ln -sf libcaiowrap.so.1.0.0   libcaiowrap.so.1
    ln -sf libcaiowrap.so.1.0.0   libcaiowrap.so
    ln -sf libcaiousb.so.1.0.0    libcaiousb.so.1
    ln -sf libcaiousb.so.1.0.0    libcaiousb.so
    ln -sf libcanon_slim.so.1.0.0   libcanon_slim.so.1
    ln -sf libcanon_slim.so.1.0.0   libcanon_slim.so

    ln -sf libColorGear.so.0.0.0    libColorGear.so.0
    ln -sf libColorGear.so.0.0.0    libColorGear.so
    ln -sf libColorGearC.so.0.0.0   libColorGearC.so.0
    ln -sf libColorGearC.so.0.0.0   libColorGearC.so

    cd "${pkgdir}"/usr/lib
    ln -sf libcanonc3pl.so.1.0.0    libcanonc3pl.so
    ln -sf libcanonc3pl.so.1.0.0    libcanonc3pl.so.1
    
    # according to gentoo ebuild (for 2.90 )c3pldrv dlopens the absolute path /usr/lib/libc3pl.so
    # this is only needed for x86_64 build
    if [[ ${CARCH} == "x86_64" ]]; then
        ln -s /usr/lib32/libc3pl.so libc3pl.so
    fi
    
    cd "${srcdir}"/"${_pkgname}"-"${pkgver}"
    install -m755 -d "${pkgdir}"/usr/share/licenses/"${pkgname}"
    install -m755 LICENSE-* "${pkgdir}"/usr/share/licenses/"${pkgname}"
}
