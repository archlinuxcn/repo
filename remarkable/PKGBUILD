# Maintainer: Mikael Blomstrand <gmail: chawlindel>
# Contributor: MaryJaneInChain <gmail.com@maryjaneinchain>
# Contributor: Michael Goehler <somebody dot here at gmx dot de>

pkgname=remarkable
replaces=('remarkable-webkit2gtk')
pkgver=1.87
pkgrel=3
pkgdesc="A free fully featured markdown editor for Linux."
arch=('any')
url="http://remarkableapp.github.io"
license=('MIT')
depends=('python'
         'python-cairo'
         'python-gobject'
         'python-markdown'
         'python-beautifulsoup4'
         'python-lxml'
         'webkit2gtk'
         'wkhtmltopdf'
         'gtksourceview3'
         )
makedepends=('python')
optdepends=('python-lxml: export to HTML format support'
            'python-gtkspellcheck: Spellcheck (might cause problems)')

install="remarkable.install"
source=("https://github.com/jamiemcg/Remarkable/archive/v${pkgver}.tar.gz"
        "0003-fixes-184-port-to-WebKit2Gtk.patch"
        "0004-fixes-175-Live-Preview-Mode-Executes-JavaScript.patch"
        "remarkable.patch"
        "remarkable.install"
        "LICENSE")

sha1sums=('a492dc5d0a276f36846a99287ae93c02e22a5cd8'
          '097f12a6f499bd39b99c32301a9027a9457eaeac'
          'd90a26e2830f0306a07b76dc69aa211840f0223e'
          'd9fc74c5a0136649f670a345e16c1c88d21a97d2'
          'bdbfb750df9e5fb3022f47a46a80555259628cd1'
          '6e5ea06076c85fdd25b79bfc41588f7f7ee9ba29')

prepare() {
    msg2 "Applying patches for webkit2gtk..."
    cat *.patch | patch -p1 -d "${srcdir}/Remarkable-${pkgver}"
}

package() {
    _python_site=$(python -c 'import site; print(site.getsitepackages()[0]);')
    [ -z ${_python_site} ] && echo "error: could not identify python site_packages directory" && return 1

    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    
    cd "Remarkable-${pkgver}"

    install -Dm 755 "bin/remarkable" "${pkgdir}/usr/bin/remarkable"
    install -D "debian/remarkable.mime" "${pkgdir}/usr/lib/mime/packages/remarkable"
    install -D "data/media/remarkable.svg" "${pkgdir}/usr/share/icons/hicolor/scalable/apps/remarkable.svg"
    install -D remarkable.desktop "${pkgdir}/usr/share/applications/remarkable.desktop"
    
    mv data/glib-2.0 "${pkgdir}/usr/share/"

    install -d "${pkgdir}/${_python_site}"
    mv markdown pdfkit remarkable remarkable_lib "${pkgdir}/${_python_site}/"

    mv data "${pkgdir}/usr/share/remarkable/"
}
