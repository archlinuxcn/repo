# Maintainer : Daniel Bermond < yahoo-com: danielbermond >
# Contributor: Det
# Contributor: Joris Steyn, Florian Dejonckheere, Tevin Zhang, Andrea Fagiani, Biru Ionut, Paul Bredbury
# Installation order:  freetype2 → fontconfig-ubuntu → cairo-ubuntu

_srcname=fontconfig
_ubver=0ubuntu2

pkgname=fontconfig-ubuntu
pkgver=2.12.6
pkgrel=2
pkgdesc='A library for configuring and customizing font access (with Ubuntu patches)'
arch=('i686' 'x86_64')
url='https://launchpad.net/ubuntu/+source/fontconfig'
license=('custom')
depends=('expat' 'freetype2')
makedepends=('autoconf-archive' 'gperf' 'python-lxml' 'python-six' 'docbook-utils' 'docbook-sgml'
             'perl-sgmls' 'texlive-formatsextra>=2017' 'lynx')
provides=("fontconfig=${pkgver}")
conflicts=('fontconfig')
install="${pkgname}.install"
source=("https://launchpad.net/ubuntu/+archive/primary/+files/fontconfig_$pkgver.orig.tar.bz2"
        "https://launchpad.net/ubuntu/+archive/primary/+files/fontconfig_$pkgver-$_ubver.debian.tar.xz"
        '53-monospace-lcd-filter.patch'
        'fontconfig-ubuntu.hook')
sha256sums=('cf0c30807d08f6a28ab46c61b8dbd55c97d2f292cf88f3a07d3384687f31f017'
            '75c259e2d6b1944fe76a49f89b806b3ee34fe7a42eb25efd289e38b1b5e16517'
            'c759702ba66fe88768aa93035637401085bb5c02d898c960b68291aea10daa8d'
            '672f6a1c5e164671955ce807e670306194142a1794ce88df653aa717a972e274')

# nice pages to test font matching:
# http://zipcon.net/~swhite/docs/computers/browsers/fonttest.html
# http://getemoji.com/

prepare() {
    cd "${_srcname}-${pkgver}"
    
    # apply Debian patches
    for _patch in $(cat "${srcdir}/debian/patches/series")
    do
        msg2 "Applying Debian patch: ${_patch}"
        patch -Np1 -i "${srcdir}/debian/patches/${_patch}"
    done
    
    ## patch
    #patch -p1 -i conf.d/53-monospace-lcd-filter.conf ../53-monospace-lcd-filter.patch
}

build() {
    cd "${_srcname}-${pkgver}"
    
    ./configure \
        --prefix='/usr' \
        --sysconfdir='/etc' \
        --with-templatedir='/etc/fonts/conf.avail' \
        --with-xmldir='/etc/fonts' \
        --localstatedir='/var' \
        --disable-static \
        --with-default-fonts='/usr/share/fonts' \
        --with-add-fonts='/usr/share/fonts'
        
    make
}

package() {
    cd "${_srcname}-${pkgver}"
    
    make DESTDIR="$pkgdir" install
    
    # pacman hook
    install -D -m644 "${srcdir}/${pkgname}.hook" "${pkgdir}/usr/share/libalpm/hooks/fontconfig.hook"
    
    # license
    install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    
    # Debian changelog
    install -D -m644 "${srcdir}/debian/changelog" "${pkgdir}/usr/share/doc/fontconfig/changelog"
}
