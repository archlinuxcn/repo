# Maintainer: AlphaLynx <alphalynx at alphalynx dot dev>

pkgname=proton-authenticator
pkgver=1.1.4
_commit=04205ef31c8edb37cfc700d0cf7f5647f83374be
pkgrel=4
pkgdesc='2FA app from Proton to securely sync and backup 2FA codes'
arch=('x86_64')
url='https://proton.me/authenticator'
license=('GPL-3.0-or-later')
depends=(
    'cairo'
    'dbus'
    'gcc-libs'
    'gdk-pixbuf2'
    'glib2'
    'glibc'
    'gtk3'
    'hicolor-icon-theme'
    'libsoup3'
    'pango'
    'webkit2gtk-4.1'
)
makedepends=('cargo' 'git' 'nodejs-lts-jod' 'yarn')
source=("ProtonWebClients::git+https://github.com/ProtonMail/WebClients.git#commit=$_commit"
        'Proton Authenticator.desktop'
        'add-missing-dnd-kit-sortable.patch')
b2sums=('173e01278d9e217d2c36c01135b556b74d6423557b7721be85cf07c2017ac32f84d9de3d45e27df91d19ac389e5d4d311d44c6fe47512415c3eaab519ffee7f1'
        '2d31d11d97e4a8163b199eed52d920d6ef68bb51e91aa6270e00350a3f9f8f4d265a1dfc995eb6a6e3a4a7ba4a52c49dfe66da32c146f36a5c2c44b68bcda531'
        'a4671d5b0b6a52b2e03986465ac396de600d71cc3d613a425d41f528950dcfb6a825ea6bfa27d0289b38a1ad426a8ff156ed58071f77492a68b1ca58848d7195')

prepare() {
    cd ProtonWebClients
    patch -p1 -i "$srcdir/add-missing-dnd-kit-sortable.patch"
    sed -i 's/"applications\/\*",/"applications\/authenticator",/' package.json
}

build() {
    cd ProtonWebClients

    # Fix ring crate LTO incompatibility with fat LTO objects
    export CFLAGS="${CFLAGS} -ffat-lto-objects"
    export CXXFLAGS="${CXXFLAGS} -ffat-lto-objects"

    yarn install
    yarn workspace proton-authenticator build:desktop
}

check() {
    cd ProtonWebClients
    yarn workspace proton-authenticator test:ci
}

package() {
    cd ProtonWebClients/applications/authenticator

    install -Dm755 src-tauri/target/release/$pkgname "$pkgdir/usr/bin/$pkgname"
    install -Dm644 "$srcdir/Proton Authenticator.desktop" \
        "$pkgdir/usr/share/applications/Proton Authenticator.desktop"

    cd src-tauri/icons
    install -Dm644 32x32.png "$pkgdir/usr/share/icons/hicolor/32x32/apps/$pkgname.png"
    install -Dm644 64x64.png "$pkgdir/usr/share/icons/hicolor/64x64/apps/$pkgname.png"
    install -Dm644 128x128.png "$pkgdir/usr/share/icons/hicolor/128x128/apps/$pkgname.png"
    install -Dm644 128x128@2x.png "$pkgdir/usr/share/icons/hicolor/256x256@2/apps/$pkgname.png"
}
