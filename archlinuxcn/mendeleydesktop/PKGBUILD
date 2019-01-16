# Maintainer: xgdgsc <xgdgsc at gmail dot com>
# Maintainer: Alesandar Trifunović <akstrfn at gmail dot com>

pkgbase=mendeleydesktop
pkgname=('mendeleydesktop'
         'mendeleydesktop-bundled')
pkgver=1.19.3
pkgrel=2
pkgdesc="Academic software for managing and sharing research papers."
url=http://www.mendeley.com/release-notes/
arch=(i686 x86_64)
license=(custom:mendeley_eula)
source_i686=("https://desktop-download.mendeley.com/download/linux/$pkgbase-$pkgver-linux-i486.tar.bz2")
source_x86_64=("https://desktop-download.mendeley.com/download/linux/$pkgbase-$pkgver-linux-x86_64.tar.bz2")
sha512sums_i686=('30e0460522474e68c1664256afc6e1d3af68443f75b0b5a76b76102ea812ed680d8d20e1d3f9dc4fc29408dd5e7718a8436ba34fc91a896fd9cbda702abcc3e8')
sha512sums_x86_64=('2c2d92d45730797f93eec74b23ea8d7f654388fd778063dcd92705fe019939f6d557bcaac13a14b021fcc4d785938921b19a9c8b821dfe6c18fb5c213eaa8a26')

if [[ $CARCH = i686 ]];then
    $CARCH=i486
fi

prepare() {
    cp -a "$pkgbase-$pkgver-linux-$CARCH" "mendeley-native"
}

package_mendeleydesktop() {
    depends=('qt5-webengine')
    cd "mendeley-native"

    # Using shared libraries so remove the bundled ones
    rm -rf lib/cpp lib/qt lib/ssl lib/libpng12.so.0 lib/mendeleydesktop/plugins
    rm -rf lib/mendeleydesktop/libexec/resources
    rm -rf lib/mendeleydesktop/libexec/translations/qtwebengine_locales

    # TODO Run install-mendeley-link-handler.sh for gconf or just remove it?
    rm bin/install-mendeley-link-handler.sh

    # # Remove unneeded lines if gconf is not installed.
    # if ! which gconftool-2 &>/dev/null;then
    # sed -i '/GCONF/d' \
    #     "$pkgdir"/opt/"$pkgbase"/bin/install-mendeley-link-handler.sh
    # fi

    # Link system Qt
    ln -s /usr/share/qt/resources \
          lib/mendeleydesktop/libexec/
    ln -s /usr/share/qt/translations/qtwebengine_locales \
          lib/mendeleydesktop/libexec/translations/

    install -d "$pkgdir/opt/$pkgbase/"
    cp -a bin lib share "$pkgdir/opt/$pkgbase/"

    # Replace default python laucher with custom bash
cat <<'EOF' > "$pkgdir/opt/$pkgbase/bin/mendeleydesktop"
#!/bin/bash
export LD_LIBRARY_PATH=/usr/lib/:/opt/mendeleydesktop/lib/:/usr/lib/qt/
export MENDELEY_BUNDLED_QT_PLUGIN_PATH=/lib/qt/plugins/
/opt/mendeleydesktop/lib/mendeleydesktop/libexec/mendeleydesktop.x86_64 "$@"
EOF

    install -d "$pkgdir"/usr/bin
    ln -s "/opt/$pkgbase/bin/mendeleydesktop" \
          "$pkgdir/usr/bin/mendeleydesktop"

    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgbase/LICENSE"
    install -Dm644 share/applications/mendeleydesktop.desktop \
                   "$pkgdir"/usr/share/applications/mendeleydesktop.desktop

    cp -a "$pkgdir/opt/$pkgbase/share/icons" "$pkgdir/usr/share/icons"

    # Clean share from opt (don't remove mendeleydesktop)
    rm -rf "$pkgdir/opt/$pkgbase/share/"{applications,doc,icons}
}

package_mendeleydesktop-bundled() {
    provides=('mendeleydesktop')
    conflicts=('mendeleydesktop')
    cd "$pkgbase-$pkgver-linux-$CARCH"

    sed -i 's/Exec=/&LD_LIBRARY_PATH=\/opt\/mendeleydesktop\/lib\/mendeleydesktop\/plugins\/platforms /' bin/install-mendeley-link-handler.sh

    install -d "$pkgdir/opt/$pkgbase"
    cp -a bin lib share "$pkgdir/opt/$pkgbase/"


    install -d "$pkgdir"/usr/bin
    ln -s "/opt/$pkgbase/bin/mendeleydesktop" \
          "$pkgdir/usr/bin/mendeleydesktop"

    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgbase/LICENSE"
    install -Dm644 share/applications/mendeleydesktop.desktop \
                   "$pkgdir"/usr/share/applications/mendeleydesktop.desktop

    cp -a "$pkgdir/opt/$pkgbase/share/icons" "$pkgdir/usr/share/icons"

    # Clean share from opt (don't remove mendeleydesktop)
    rm -rf "$pkgdir/opt/$pkgbase/share/"{applications,doc,icons}
}
