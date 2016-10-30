# Maintainer: Phillip Schichtel <phillip.public@schich.tel>
pkgname=adapta-gtk-theme
_gtk3_min='3.18'
_gtk3_max='3.22'
_theme_name=Adapta
_gtk2_min='2.24.30'
pkgver="${_gtk3_max}.2.29"
pkgrel=1
pkgdesc="An adaptive Gtk+ theme based on Material Design Guidelines."
arch=(any)
url="https://github.com/adapta-project/${pkgname}"
license=('GPL2' 'CCPL')
depends=("gtk2>=${_gtk2_min}"
         "gtk3>=${_gtk3_min}.9"
         "gtk3<=${_gtk3_max}.99"
         'gtk-engines>=2.21.0'
         'gtk-engine-murrine>=0.98.1')
optdepends=("gnome-shell>=${_gtk3_min}.3: The GNOME Shell"
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
sha256sums=('36f17061a0a8eef7114bbf1328339cbe984fa4549752b6643e675e9050e0dd66')

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

