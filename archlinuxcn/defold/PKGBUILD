# Maintainer: Asakura Mizu <asakuramizu111@gmail.com>
pkgname=defold
pkgver=1.8.0
pkgrel=2
epoch=
pkgdesc="Defold is a completely free to use game engine for development of desktop, mobile and web games."
arch=(x86_64)
url="https://defold.com/"
license=("custom")
groups=()
depends=("glu")
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("https://github.com/defold/defold/releases/download/${pkgver}/Defold-x86_64-linux.tar.gz"
        "https://github.com/defold/defold/releases/download/${pkgver}/defoldsdk_headers.zip"
        "https://github.com/defold/defold/releases/download/${pkgver}/bob.jar"
        "Defold.desktop"
        "LICENSE"
        "logo.zip")
noextract=("bob.jar")
sha256sums=('3df316f1cd946d07698f543cd381fa67f5ca6cc0f6f93ff45df3e525b3489a19'
            '2f0b876fec08bf0eab5f3c8038979df2abb55836f3b0535eeeaf3f07096bd8b6'
            '452b84eabf5cff5cc70b3a411c8d6e46a74fe06142d7f02f87c36a730285bd9c'
            '9725d96324da56845f78a74352340e72366efa448d7ad05af3d5ed8a22ab873a'
            'be6e9921ba01445d200ba3dc09b5cab149a58d57a76ca98376b52af87d817a7a'
            '3b8caea5c51ed35d0b192b621e55102c7336904d5bc096d801cbbe700ebf17ca')
validpgpkeys=()

package() {
    cd "$srcdir"

    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 Defold.desktop "$pkgdir/usr/share/applications/Defold.desktop"
    install -Dm644 "logo/64.png" "$pkgdir/usr/share/icons/hicolor/64x64/apps/defold.png"
    install -Dm644 "logo/128.png" "$pkgdir/usr/share/icons/hicolor/128x128/apps/defold.png"
    install -Dm644 "logo/150.png" "$pkgdir/usr/share/icons/hicolor/150x150/apps/defold.png"
    install -Dm644 "logo/310.png" "$pkgdir/usr/share/icons/hicolor/310x310/apps/defold.png"
    install -Dm644 "logo/1024.png" "$pkgdir/usr/share/icons/hicolor/1024x1024/apps/defold.png"
    mkdir -p "$pkgdir/opt/Defold"
    cp -r Defold "$pkgdir/opt"
    cp -r defoldsdk "$pkgdir/opt/Defold"
    mkdir -p "$pkgdir/usr/include"
    ln -s "/opt/Defold/defoldsdk/sdk/include/dmsdk" "$pkgdir/usr/include/dmsdk"
    install -Dm644 bob.jar "$pkgdir/opt/Defold"
}
