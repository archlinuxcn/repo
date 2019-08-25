# Maintainer: Pavan Rikhi <pavan.rikhi@gmail.com>
pkgname=pencil
pkgver=3.0.4
pkgrel=3
pkgdesc="Sketching and GUI prototyping/wireframing tool"
arch=('any')
license=('GPL2')
url="http://github.com/evolus/pencil"
source=("https://github.com/evolus/pencil/archive/v$pkgver.tar.gz"
        "pencil.desktop"
        "pencil-mime.xml")
sha256sums=('f00b06d7db9583479597db827ebe1371ad0878a947a28c97c00895e50f2476f4'
            '6d467da74509e74e06325e7464a6a177164ae8977470423da6cae43265dedd4d'
            '87aac9f5005ccd57aa6b1bf190052fcc4915eff1d7bddb2723863739545e42fc')
conflicts=('evolus-pencil-bin' 'pencil-v2')
depends=('nodejs' 'npm' 'libxss' 'nss' 'gconf' 'libxtst' 'gtk2' 'alsa-lib')

package() {
    cd "$srcdir/$pkgname-$pkgver"

    if [ -d "$HOME" ]; then
        TMP_HOME="$HOME"
    else
        TMP_HOME="$(pwd)/tmp-home"
        mkdir -p "$TMP_HOME/.config"
    fi

    # Temporary fix for segfaults until next Pencil release(3.0.5+)
    HOME="$TMP_HOME" npm i -s electron@"==1.8"
    cd app/
    HOME="$TMP_HOME" npm i -s unzipper
    sed -i 's/unzip2/unzipper/' app.js
    cd ..

    HOME="$TMP_HOME" npm install --unsafe-perm
    HOME="$TMP_HOME" node_modules/.bin/build --linux dir

    install -d "$pkgdir/usr/share/$pkgname/" "$pkgdir/usr/bin" \
        "$pkgdir/usr/share/applications" "$pkgdir/usr/share/mime/packages"

    cp -r dist/linux-unpacked/* "$pkgdir/usr/share/$pkgname/"
    cp app/css/images/logo-shadow.png "$pkgdir/usr/share/$pkgname/icon.png"

    cp "$srcdir/pencil.desktop" "$pkgdir/usr/share/applications/"
    cp "$srcdir/pencil-mime.xml" "$pkgdir/usr/share/mime/packages/"

    ln -s "/usr/share/$pkgname/pencil" "$pkgdir/usr/bin/"
}
