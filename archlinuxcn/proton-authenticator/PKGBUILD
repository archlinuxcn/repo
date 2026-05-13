# Maintainer: AlphaLynx <alphalynx at alphalynx dot dev>

pkgname=proton-authenticator
pkgver=1.1.5
pkgrel=1
pkgdesc='2FA app from Proton to securely sync and backup 2FA codes'
arch=(x86_64)
url='https://proton.me/authenticator'
license=(GPL-3.0-or-later)
depends=(cairo
         dbus
         gdk-pixbuf2
         glib2
         glibc
         gtk3
         hicolor-icon-theme
         libsoup3
         libgcc
         webkit2gtk-4.1)
makedepends=(cargo git nodejs-lts-jod yarn)
source=($pkgname-$pkgver.tar.gz::https://github.com/ProtonMail/WebClients/archive/refs/tags/proton-authenticator@1.1.5.tar.gz
        $pkgname.desktop)
b2sums=('5517a797143fef200e0d9bef4061696e14b93c42fd43702bd4fc76d70408521cd73e56d8762a2a903788710c8373ae754c916e4f4910b25acaade05639cc5355'
        '2d31d11d97e4a8163b199eed52d920d6ef68bb51e91aa6270e00350a3f9f8f4d265a1dfc995eb6a6e3a4a7ba4a52c49dfe66da32c146f36a5c2c44b68bcda531')

prepare() {
    cd WebClients-$pkgname-$pkgver

    # Configure Yarn workspaces to build only authenticator instead of all applications
    sed -i 's/"applications\/\*",/"applications\/authenticator",/' package.json

    # Modify tauri build script to use --frozen flag for reproducible builds
    sed -i 's/tauri build -v --no-bundle/tauri build -v --no-bundle -- --frozen/g' \
        applications/authenticator/tools/build.sh

    export YARN_CACHE_FOLDER="$srcdir/.yarn-cache"
    yarn install

    cd applications/authenticator/src-tauri
    export RUSTUP_TOOLCHAIN=stable
    cargo fetch --locked --target host-tuple
}

build() {
    cd WebClients-$pkgname-$pkgver

    # Fix ring crate LTO incompatibility with fat LTO objects
    export CFLAGS="${CFLAGS} -ffat-lto-objects"
    export CXXFLAGS="${CXXFLAGS} -ffat-lto-objects"

    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    export CARGO_PROFILE_RELEASE_DEBUG=true
    yarn workspace proton-authenticator build:desktop
}

check() {
    cd WebClients-$pkgname-$pkgver
    yarn workspace proton-authenticator test:ci
}

package() {
    cd WebClients-$pkgname-$pkgver/applications/authenticator

    install -Dm755 src-tauri/target/release/$pkgname -t "$pkgdir/usr/bin"
    install -Dm644 "$srcdir/$pkgname.desktop" -t "$pkgdir/usr/share/applications"

    cd src-tauri/icons
    install -Dm644 32x32.png "$pkgdir/usr/share/icons/hicolor/32x32/apps/$pkgname.png"
    install -Dm644 64x64.png "$pkgdir/usr/share/icons/hicolor/64x64/apps/$pkgname.png"
    install -Dm644 128x128.png "$pkgdir/usr/share/icons/hicolor/128x128/apps/$pkgname.png"
    install -Dm644 128x128@2x.png "$pkgdir/usr/share/icons/hicolor/128x128@2/apps/$pkgname.png"
    install -Dm644 icon.png "$pkgdir/usr/share/icons/hicolor/512x512/apps/$pkgname.png"
}
