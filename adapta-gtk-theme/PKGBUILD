# Maintainer: Phillip Schichtel <phillip.public@schich.tel>
pkgname=adapta-gtk-theme
_gtk3_min='3.18'
_gtk3_max='4.0'
_theme_name=Adapta
_gtk2_min='2.24.30'
pkgver="3.22.2.81"
pkgrel=2
pkgdesc="An adaptive Gtk+ theme based on Material Design Guidelines."
arch=(any)
url="https://github.com/adapta-project/${pkgname}"
license=('GPL2' 'CCPL')
depends=("gtk2>=${_gtk2_min}"
         "gtk3>=${_gtk3_min}.9"
         "gtk3<=${_gtk3_max}.99"
         'gtk-engines>=2.21.0'
         'gtk-engine-murrine>=0.98.1'
         'cantarell-fonts')
optdepends=('ttf-roboto: The recommended font'
            'noto-fonts: The recommended font for improved language support'
            "gnome-shell>=${_gtk3_min}.3: The GNOME Shell"
            "gnome-flashback>=${_gtk3_min}.2: The GNOME flashback shell"
            'budgie-desktop>=10.2.5: The Budgie desktop'
            'cinnamon>=2.8.6: The Cinnamon desktop'
            'xfdesktop>=4.12.2: The Xfce desktop'
            'marco-gtk3>=1.14.0: The mate desktop in its GTK3 version'
            'ldm: The LXDE display manager in its GTK2 version'
            'paper-icon-theme: A fitting icon theme'
            'gnome-tweak-tool: A graphical tool to tweak gnome settings'
            'adapta-backgrounds: The corresponding backgrounds project'
            "unity>=7.4.0: Ubuntu's Unity desktop")
makedepends=('glib2>=2.48.0'
             'libxml2'
             'ruby-bundler>=1.11.0'
             'inkscape'
             'parallel')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('93aa3194ca6c9eef89a9bd0a3529ed7902d6ebc209fe1aa09670c5de8a7728e7')

_bundle="ruby-bundle"

prepare() {
    cd "${pkgname}-${pkgver}"
    export BUNDLE_PATH="${srcdir}/${_bundle}"
    bundle install
}

build() {
    export BUNDLE_PATH="${srcdir}/${_bundle}"
    export PATH="${BUNDLE_PATH}/bin:${PATH}"
    cd "${pkgname}-${pkgver}"
    ./autogen.sh --enable-gtk_next \
                 --enable-chrome \
                 --enable-plank \
                 --enable-parallel
    make
}

package() {
    cd "${pkgname}-${pkgver}"
    make DESTDIR="$pkgdir" install -j 8
}

