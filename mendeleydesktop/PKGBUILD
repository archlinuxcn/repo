# Maintainer: xgdgsc <xgdgsc at gmail dot com>
# Maintainer: Alesandar Trifunović <akstrfn at gmail dot com>

pkgname=mendeleydesktop
pkgver=1.19
pkgrel=1
pkgdesc="Academic software for managing and sharing research papers (desktop client)"
url=http://www.mendeley.com/release-notes/
arch=(i686 x86_64)
depends=(qt5-webengine)
license=(custom:mendeley_eula)
source_i686=("https://desktop-download.mendeley.com/download/linux/$pkgname-$pkgver-linux-i486.tar.bz2")
source_x86_64=("https://desktop-download.mendeley.com/download/linux/$pkgname-$pkgver-linux-x86_64.tar.bz2")
sha512sums_i686=('9dd0a62b02a3b9a389cd6deb8c642b30c07043e695f01a7f928bc791f535aae98ebba85e7f8b28aeecb8b95d7d6c6e6eb9bc1744965ed145163af662415d627f')
sha512sums_x86_64=('cea139a30e220cc28ab82189ae81304a9f1003fc0afbecd7e14dc4956af69e14c8ff6110bbbf9eee1ab205950e6b45b91b04c623f5f2e418329d8d85953a6710')

if [[ $CARCH = i686 ]];then
$CARCH=i486
fi

prepare() {
    cd "$pkgname-$pkgver-linux-$CARCH"
    # Using shared libraries so remove the bundled ones
    rm -rf lib/cpp lib/qt lib/ssl lib/libpng12.so.0 lib/mendeleydesktop/plugins
    rm -rf lib/mendeleydesktop/libexec/resources
    rm -rf lib/mendeleydesktop/libexec/translations/qtwebengine_locales

    # TODO Run install-mendeley-link-handler.sh for gconf or just remove it?
    rm bin/install-mendeley-link-handler.sh

    # # Remove unneeded lines if gconf is not installed.
    # if ! which gconftool-2 &>/dev/null;then
    # sed -i '/GCONF/d' \
    #     "$pkgdir"/opt/"$pkgname"/bin/install-mendeley-link-handler.sh
    # fi
}

package() {
    cd "$pkgname-$pkgver-linux-$CARCH"

    # Link system Qt
    ln -s /usr/share/qt/resources \
          lib/mendeleydesktop/libexec/
    ln -s /usr/share/qt/translations/qtwebengine_locales \
          lib/mendeleydesktop/libexec/translations/

    install -d "$pkgdir/opt/$pkgname/"
    cp -a bin lib share "$pkgdir/opt/$pkgname/"

    # Replace default python laucher with custom bash
cat <<'EOF' > "$pkgdir/opt/$pkgname/bin/mendeleydesktop"
#!/bin/bash
export LD_LIBRARY_PATH=/usr/lib/:/opt/mendeleydesktop/lib/:/usr/lib/qt/
export MENDELEY_BUNDLED_QT_PLUGIN_PATH=/lib/qt/plugins/
/opt/mendeleydesktop/lib/mendeleydesktop/libexec/mendeleydesktop.x86_64 "$@"
EOF

    install -d "$pkgdir"/usr/bin
    ln -s "/opt/$pkgname/bin/mendeleydesktop" \
          "$pkgdir/usr/bin/mendeleydesktop"

    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 share/applications/mendeleydesktop.desktop \
                   "$pkgdir"/usr/share/applications/mendeleydesktop.desktop

    cp -a "$pkgdir/opt/$pkgname/share/icons" "$pkgdir/usr/share/icons"

    # Clean share from opt (don't remove mendeleydesktop)
    rm -rf "$pkgdir/opt/$pkgname/share/"{applications,doc,icons}
}
