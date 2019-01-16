# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: Det
# Contributor: Joris Steyn, Florian Dejonckheere, Tevin Zhang, Andrea Fagiani, Biru Ionut, Paul Bredbury
# Installation order:  freetype2 → fontconfig-ubuntu → cairo-ubuntu

# nice pages to test font matching:
# http://zipcon.net/~swhite/docs/computers/browsers/fonttest.html
# http://getemoji.com/

_srcname=fontconfig
_ubuver=5ubuntu3

pkgname=fontconfig-ubuntu
pkgver=2.13.0
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
source=("https://launchpad.net/ubuntu/+archive/primary/+files/fontconfig_${pkgver}.orig.tar.bz2"
        "https://launchpad.net/ubuntu/+archive/primary/+files/fontconfig_${pkgver}-${_ubuver}.debian.tar.xz"
        '53-monospace-lcd-filter.patch'
        'fontconfig-ubuntu.hook')
sha256sums=('91dde8492155b7f34bb95079e79be92f1df353fcc682c19be90762fd3e12eeb9'
            'ff3bed047dc345a5925be6bf7c4739d4d416ad8ab89dd9c4261f23da1f45f6a6'
            'c759702ba66fe88768aa93035637401085bb5c02d898c960b68291aea10daa8d'
            '672f6a1c5e164671955ce807e670306194142a1794ce88df653aa717a972e274')

prepare() {
    cd "${_srcname}-${pkgver}"
    
    local _patch
    
    # apply Debian patches
    while read _patch
    do
        if printf '%s' "$_patch" | grep -q '\.patch$\|\.diff$'
        then
            printf '%s\n' "  -> Applying Debian patch: ${_patch}"
            patch -Np1 -i "${srcdir}/debian/patches/${_patch}"
        fi
    done < "${srcdir}/debian/patches/series"
    
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
    install -D -m644 "${srcdir}/${pkgname}.hook" -t "${pkgdir}/usr/share/libalpm/hooks"
    
    # license
    install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    
    # Debian changelog
    install -D -m644 "${srcdir}/debian/changelog" -t "${pkgdir}/usr/share/doc/${pkgname}"
}
