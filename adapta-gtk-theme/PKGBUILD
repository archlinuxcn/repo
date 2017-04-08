# Maintainer: Phillip Schichtel <phillip.public@schich.tel>
pkgname=adapta-gtk-theme
_gtk2_min='2.24.30'
_gtk3_min='3.18'
_gtk_max='4.0'
pkgver="3.90.0.44"
pkgrel=1
pkgdesc="An adaptive Gtk+ theme based on Material Design Guidelines."
arch=(any)
url="https://github.com/adapta-project/${pkgname}"
license=('GPL2' 'CCPL')
depends=("gtk2>=${_gtk2_min}"
         "gtk3>=${_gtk3_min}.9"
         "gtk3<=${_gtk_max}.99"
         'gdk-pixbuf2>=2.21.0'
         'gtk-engines>=2.21.0'
         'gtk-engine-murrine>=0.98.1'
         'cantarell-fonts')
optdepends=('ttf-roboto: The recommended font'
            'noto-fonts: The recommended font for improved language support'
            "gnome-shell>=${_gtk3_min}.3: The GNOME Shell"
            "gnome-flashback>=${_gtk3_min}.2: The GNOME flashback shell"
            'budgie-desktop>=10.2.7: The Budgie desktop'
            'cinnamon>=2.8.6: The Cinnamon desktop'
            'xfdesktop>=4.12.2: The Xfce desktop'
            'marco-gtk3>=1.14.0: The mate desktop in its GTK3 version'
            'ldm: The LXDE display manager in its GTK2 version'
            'paper-icon-theme: A fitting icon theme'
            'gnome-tweak-tool: A graphical tool to tweak gnome settings'
            'adapta-backgrounds: The corresponding backgrounds project'
            'telegram-desktop>=1.0.0: The Telegram desktop client'
            "unity>=7.4.0: Ubuntu's Unity desktop")
makedepends=('glib2>=2.48.0'
             'libxml2'
             'librsvg'
             'sassc>=3.3.2'
             'inkscape'
             'parallel')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
#        "${pkgname}-${pkgver}.tar.gz.asc::${url}/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.gz.asc")
sha256sums=('2e8697dd05739b7ef7d0d49366bfd72b128bd7836e302822d74068481e6d8e9f')

build() {
    cd "${pkgname}-${pkgver}"
    ./autogen.sh --enable-gtk_next \
                 --enable-chrome \
                 --enable-plank \
                 --enable-telegram \
                 --enable-parallel
    make
}

package() {
    cd "${pkgname}-${pkgver}"
    make DESTDIR="$pkgdir" install
}

