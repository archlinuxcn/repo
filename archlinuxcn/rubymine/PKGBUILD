# Maintainer: Mario Finelli <mario at finel dot li>
# Contributor: Tom Richards <tom at tomrichards dot net>
# Contributor: Alexsandr Pavlov <kidoz at mail dot ru>
# Contributor: Ernie Brodeur <ebrodeur at ujami dotnet>
# Contributor: Rogof <fake dot bios at gmail dot com>
# Contributor: m4.rc0 <m4 dot rc0 at o2 dot pl>

pkgname=rubymine
_pkgname=RubyMine
pkgver=2018.3.2
pkgrel=2
pkgdesc="Ruby and Rails IDE with the full stack of essential developer tools."
arch=('i686' 'x86_64')
options=(!strip)
url="https://www.jetbrains.com/ruby/"
license=('custom')
depends=('desktop-file-utils' 'gtk-update-icon-cache')
optdepends=('ruby: Ruby run/debug support')
install=rubymine.install
source=(https://download.jetbrains.com/ruby/${_pkgname}-${pkgver}.tar.gz
        rubymine.desktop
        rubymine.install)
sha256sums=('79eef49448d7cc943d943bd8cf419cba2785b2c95d0299ea1f6499938a5845b3'
            '72df0e7c605caf7b6c98e9335f4eee9c8bfe8fcc24523634fd8c1ebe019534d6'
            '7ecadddf2b315b22df3a5c7b90e18be7ea69e2a0d869ee18bf0e031b2c508f76')

prepare() {
    cd "${srcdir}/${_pkgname}-${pkgver}"

    #Remove non-linux libs
    rm -rf "lib/libpty/macosx"
    rm -rf "lib/libpty/win"

    #Remove bin/libs if architecture doesn't match
    if [[ $CARCH = 'i686' ]]; then
        rm -f "bin/fsnotifier64"
        rm -f "bin/libbreakgen64.so"
        rm -f "bin/libyjpagent-linux64.so"
        rm -f "bin/rubymine64.vmoptions"
        rm -rf "lib/libpty/linux/x86_64"
    fi
    if [[ $CARCH = 'x86_64' ]]; then
        rm -f "bin/fsnotifier"
        rm -f "bin/libbreakgen.so"
        rm -f "bin/libyjpagent-linux.so"
        rm -f "bin/rubymine.vmoptions"
        rm -rf "lib/libpty/linux/x86"
    fi
}

package() {
    cd "${srcdir}"
    [ $CARCH == "x86_64" ] && SUFFIX=64

    #Pre-packaged program files
    install -d -m 755 "${pkgdir}/usr/share"
    cp -a "${srcdir}/${_pkgname}-${pkgver}" "${pkgdir}/usr/share/${pkgname}"

    #Desktop application
    install -Dm644 "${pkgdir}/usr/share/${pkgname}/bin/RMlogo.svg" "${pkgdir}/usr/share/icons/hicolor/scalable/apps/${pkgname}.svg"
    install -Dm644 "rubymine.desktop" "${pkgdir}/usr/share/applications/rubymine.desktop"
    install -d -m 755 "${pkgdir}/usr/bin"
    ln -s "/usr/share/${pkgname}/bin/${pkgname}.sh" "${pkgdir}/usr/bin/jetbrains-${pkgname}"

    #License
    install -dm755 "$pkgdir/usr/share/licenses/$pkgname"
    find "$srcdir/$_pkgname-$pkgver/license/" -type f -exec \
        install -Dm644 '{}' "$pkgdir/usr/share/licenses/$pkgname/" \;

    #Java config
    sed -i 's/lcd/on/' "${pkgdir}/usr/share/rubymine/bin/rubymine${SUFFIX}.vmoptions"
    echo "-Dswing.aatext=true" >> "${pkgdir}/usr/share/rubymine/bin/rubymine${SUFFIX}.vmoptions"
}
