# Maintainer: Yunhui Fu <yhfudev@gmail.com>

pkgname=xavs
pkgver=0.1.55
pkgrel=1
pkgdesc="XAVS is to implement high quality encoder and decoder of the Audio Video Standard of China (AVS)."
arch=(i686 x86_64 arm)
url="http://xavs.sourceforge.net/"
license=(GPL)
depends=()
makedepends=(yasm)
#options=(!strip)

source=(
    "${pkgname}-${pkgver}.tar.gz::https://github.com/OpenMandrivaAssociation/xavs/raw/master/xavs-${pkgver}.tar.xz" # pkgname=xavs, pkgver=0.1.55
    https://github.com/OpenMandrivaAssociation/xavs/raw/master/xavs-0.1.55-dont-strip-symbols.patch
    https://github.com/pld-linux/xavs/raw/master/xavs-dynamic-xavs.patch
    xavs-dup-asm.patch
    xavs-x32-yasm.patch
    )
md5sums=(
    '2986b9829e016e9800e50278469fdfae'
    '8ce1d21e378d234b949cb035c66d5655'
    'f6c2726fc2c11025b868952f389c0db3'
    'b39717e48edb5e8b8696e50d41c24ac0'
    'd42b193cb6f8c9bfd62a0631698e29f0'
    )

prepare() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    patch -Np1 -i ${srcdir}/xavs-dynamic-xavs.patch
    patch -Np1 -i ${srcdir}/xavs-0.1.55-dont-strip-symbols.patch
    patch -Np1 -i ${srcdir}/xavs-dup-asm.patch
    patch -Np1 -i ${srcdir}/xavs-x32-yasm.patch
    sed -i -e 's|$(CC) -o $@ $(OBJCLI) $(LDFLAGS) -L. -lxavs|$(CC) -o $@ $(OBJCLI) -L. -lxavs $(LDFLAGS)|' Makefile
    sed -i -e 's|xavs$(EXE): $(OBJCLI) $(SONAME)|xavs$(EXE): $(OBJCLI) $(SONAME) libxavs.a|' Makefile
}

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    ./configure --enable-shared --disable-asm --prefix=/usr
    make
}

package() {
    cd "$srcdir/${pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
    install -m 644 libxavs.a ${pkgdir}/usr/lib/libxavs.a
}
