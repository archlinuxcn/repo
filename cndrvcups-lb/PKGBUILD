#Maintainer: Lone_Wolf <lonewolf@xs4all.nl>
# Contributor: Steven She <mintcoffee@gmail.com>
# Contributor: vbPadre <vbPadre@gmail.com>
pkgbase=cndrvcups-lb
pkgname=cndrvcups-lb
pkgver=3.40
pkgrel=1
pkgdesc="Canon UFR II /LIPSLX Printer Driver build from source for LBP, iR & MF printers"
arch=('i686' 'x86_64')
url="http://support-au.canon.com.au/contents/AU/EN/0100270808.html"
license=('custom')
install=${pkgname}.install
depends_i686=('cndrvcups-common-lb=3.80' 'libxml2')
depends_x86_64=('cndrvcups-common-lb=3.80' 'lib32-libxml2')
makedepends=('autoconf' 'automake')
optdepends_i686=('libjpeg6-turbo: improves printing results for color imageRUNNER/i-SENSYS LBP devices')
optdepends_x86_64=('lib32-libjpeg6-turbo: improves printing results for color imageRUNNER/i-SENSYS LBP devices')
conflicts=('cndrvcups-lb-bin' 'cndrvcups-lb-cpca')
source=('http://gdlp01.c-wss.com/gds/8/0100002708/17/linux-UFRII-drv-v340-uken.tar.gz'
       'how-to.txt')
# http://gdlp01.c-wss.com/gds/8/0100002708/17/linux-UFRII-drv-v340-uken.tar.gz
options=('!emptydirs' '!strip' '!libtool')
sha512sums=('05f12d2cac5ae9987fe389be1a15b11d280734f6d47b86f04fa2fcb61bf94175b7afdba4cc1cf5ecf2c1ef5a8e2c14eda5d72f7671618d7c94581c620fea4494'
            '736e1785c443c4d129c8801a127410012889f46691259e8a7f6a54106a0647beb5b6267aabb78b3ed0a1c7a9d8ce216e159515d3aad425812e5be52c8b58e4ee')
         
# build instructions are adapted from upstream cndrvcups-lb.spec file
prepare() {
    cd "${srcdir}"/linux-UFRII-drv-v340-uken/Sources
    bsdtar xf ${pkgbase}-${pkgver}-1.tar.gz -C "${srcdir}"
}

build() {
    
    cd "${srcdir}"/${pkgbase}-${pkgver}/ppd
    autoreconf -fi
    ./autogen.sh --prefix=/usr
        
    cd "${srcdir}"/${pkgbase}-${pkgver}/pstoufr2cpca
    autoreconf -fi
    ./autogen.sh --prefix=/usr --libdir=/usr/lib

    cd "${srcdir}"/${pkgbase}-${pkgver}/cpca
    autoreconf -fi
    ./autogen.sh --prefix=/usr --enable-progpath=/usr/bin --libdir=/usr/lib

    cd "${srcdir}"/${pkgbase}-${pkgver}/cngplp
    aclocal
    autoreconf -fi
    ./autogen.sh --prefix=/usr --libdir=/usr/lib
    
    cd files
    autoreconf -fi
    ./autogen.sh --prefix=/usr

    cd "${srcdir}"/${pkgbase}-${pkgver}
    make
    
}

package() {
  
    cd "${srcdir}"/${pkgbase}-${pkgver}

    if [[ $CARCH == "i686" ]]; then
      _lib32dir="lib"
    else
      _lib32dir="lib32"
      mkdir -p "${pkgdir}"/usr/${_lib32dir}
    fi

    mkdir -p "${pkgdir}"/usr/{bin,share/{caepcm,cnpkbidi,ufr2filter}}
    make install DESTDIR="${pkgdir}"
    
    cd "${srcdir}"/${pkgbase}-${pkgver}
    install -m 4755 libs/cnpkmoduleufr2  "${pkgdir}"/usr/bin

    install -m 755 libs/libcanonufr2.la  "${pkgdir}"/usr/${_lib32dir}
    install -s -m 755 libs/libcanonufr2.so.1.0.0  "${pkgdir}"/usr/${_lib32dir}
    install -s -m 755 libs/libufr2filter.so.1.0.0   "${pkgdir}"/usr/${_lib32dir}
    install -s -m 755 libs/libEnoJBIG.so.1.0.0   "${pkgdir}"/usr/${_lib32dir}
    install -s -m 755 libs/libEnoJPEG.so.1.0.0   "${pkgdir}"/usr/${_lib32dir}
    install -s -m 755 libs/cnpkbidi   "${pkgdir}"/usr/bin
    install -s -m 755 libs/libcaiocnpkbidi.so.1.0.0   "${pkgdir}"/usr/${_lib32dir}

    install -m 644 data/CnLB*  "${pkgdir}"/usr/share/caepcm
    install -m 644 libs/cnpkbidi_info* "${pkgdir}"/usr/share/cnpkbidi
    install -m 644 libs/ThLB*  "${pkgdir}"/usr/share/ufr2filter

    install -m 755 libs/libcnlbcm.so.1.0     "${pkgdir}"/usr/${_lib32dir}

    cd "${pkgdir}"/usr/${_lib32dir}
    ln -sf libcanonufr2.so.1.0.0 libcanonufr2.so
    ln -sf libcanonufr2.so.1.0.0 libcanonufr2.so.1
    ln -sf libufr2filter.so.1.0.0 libufr2filter.so
    ln -sf libufr2filter.so.1.0.0 libufr2filter.so.1
    ln -sf libEnoJBIG.so.1.0.0 libEnoJBIG.so
    ln -sf libEnoJBIG.so.1.0.0 libEnoJBIG.so.1
    ln -sf libEnoJPEG.so.1.0.0 libEnoJPEG.so
    ln -sf libEnoJPEG.so.1.0.0 libEnoJPEG.so.1
    ln -sf libcaiocnpkbidi.so.1.0.0 libcaiocnpkbidi.so
    ln -sf libcaiocnpkbidi.so.1.0.0 libcaiocnpkbidi.so.1
    ln -sf libcnlbcm.so.1.0     libcnlbcm.so.1
    ln -sf libcnlbcm.so.1.0     libcnlbcm.so
    
    # according to Gentoo ebuild v2.90 c3pldrv dlopens the absolute path /usr/lib/libcnlbcm.so 
    cd "${pkgdir}"/usr/lib
    if [[ ${CARCH} == "x86_64" ]]; then
        ln -s /usr/lib32/libcnlbcm.so libcnlbcm.so
    fi

    cd "${srcdir}"/${pkgbase}-${pkgver}
    install -m755 -d "${pkgdir}"/usr/share/licenses/${pkgname}
    install -m644 LICENSE-*.txt "${pkgdir}"/usr/share/licenses/${pkgname}/
    install -m755 -d "${pkgdir}"/usr/share/doc/${pkgname}
    install -m644 README* "${pkgdir}"/usr/share/doc/${pkgname}
    install -m644 "${srcdir}"/linux-UFRII-drv-v340-uken/Documents/guide-ufr2-3.4xUK.tar.gz "${pkgdir}"/usr/share/doc/${pkgname}
}
