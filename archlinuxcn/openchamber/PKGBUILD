# Maintainer: Jasmin <theblazehen@gmail.com>
pkgname=openchamber
_npmname=@openchamber/web
pkgver=2.8.1
pkgrel=1
pkgdesc="Desktop and web interface for OpenCode AI agent"
arch=('x86_64')
url="https://github.com/btriapitsyn/openchamber"
license=('MIT')
depends=('nodejs' 'bash')
makedepends=('npm' 'jq' 'patchelf')
source=("https://registry.npmjs.org/@openchamber/web/-/web-${pkgver}.tgz")
noextract=("web-${pkgver}.tgz")
sha256sums=('89ca2d7c698eece62195ec04defef089b6c1b3c6bec1477a300d9bed8a03d14a')

package() {
    mkdir -p "${srcdir}/web"
    tar -xzf "${srcdir}/web-${pkgver}.tgz" -C "${srcdir}/web" --strip-components=1
    if ! npm view @openchamber/sdk@1.23.1 >/dev/null 2>&1; then
        sed -i 's|"@openchamber\\/sdk": "1.23.1"|"@openchamber\\/sdk": "1.24.0"|' "${srcdir}/web/package.json"
    fi
    npm install -g --install-links --cache "${srcdir}/npm-cache" --prefix "${pkgdir}/usr" "${srcdir}/web"

    find "${pkgdir}/usr" -type d -exec chmod 755 {} +
    chown -R root:root "${pkgdir}"

    find "$pkgdir" -name package.json -print0 | xargs -r -0 sed -i '/_where/d'

    local tmppackage="$(mktemp)"
    local pkgjson="$pkgdir/usr/lib/node_modules/@openchamber/web/package.json"
    jq '.|=with_entries(select(.key|test("_.+")|not))' "$pkgjson" > "$tmppackage"
    mv "$tmppackage" "$pkgjson"
    chmod 644 "$pkgjson"

    # Remove literal references to $srcdir and $pkgdir left in some upstream build files
    find "$pkgdir/usr/lib/node_modules" -type f -exec sed -i 's|\$srcdir||g;s|\$pkgdir||g' {} +
    rm -f "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules/node-pty/build/config.gypi" \
          "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules/node-pty/build/Makefile"

    # Remove leftover compiled object and dependency files to satisfy namcap warnings
    find "$pkgdir/usr/lib/node_modules" -type f \( -name '*.o' -o -name '*.o.d' -o -name '*.d' \) -delete || true

    # Remove better-sqlite3 build intermediates and config files that may reference build paths
    rm -rf "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules/better-sqlite3/build/Release/obj.target" || true
    rm -f "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules/better-sqlite3/build/config.gypi" \
          "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules/better-sqlite3/build/Makefile" || true

    # Install license file for namcap (search common license filenames)
    license_files=( "$pkgdir/usr/lib/node_modules/@openchamber/web/LICENSE" "$pkgdir/usr/lib/node_modules/@openchamber/web/license" "$pkgdir/usr/lib/node_modules/@openchamber/web/LICENSE.md" )
    for lf in "${license_files[@]}"; do
      if [ -f "$lf" ]; then
        install -Dm644 "$lf" "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
        break
      fi
    done

    rm -f "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules/bun-pty/rust-pty/target/release/librust_pty_arm64.so"
    rm -f "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules/bun-pty/rust-pty/target/release/librust_pty_musl.so" \
          "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules/bun-pty/rust-pty/target/release/librust_pty_arm64_musl.so"
    rm -f "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules/node-pty/prebuilds/linux-arm64/pty.node"

    # Remove empty prebuild directories left after removing arm64 artifacts
    find "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules" -type d -path '*/prebuilds/*' -empty -delete || true
    # Remove any other empty directories under node_modules to satisfy namcap
    find "$pkgdir/usr/lib/node_modules" -type d -empty -delete || true

    if [ -f "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules/node-pty/prebuilds/linux-x64/pty.node" ]; then
        if file "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules/node-pty/prebuilds/linux-x64/pty.node" | grep -qi 'x86-64'; then
            strip --strip-unneeded "$pkgdir/usr/lib/node_modules/@openchamber/web/node_modules/node-pty/prebuilds/linux-x64/pty.node" || true
        fi
    fi

    find "$pkgdir/usr/lib/node_modules" -type f \( -name '*.so' -o -name '*.node' \) -exec sh -c 'file "$1" | grep -qi x86-64 && strip --strip-unneeded "$1" || true' sh {} \;

    find "$pkgdir/usr/lib/node_modules" -type f \( -name '*.so' -o -name '*.node' \) -exec sh -c 'file "$1" | grep -qi x86-64 && patchelf --set-rpath '\''$ORIGIN'\'' "$1" >/dev/null 2>&1 || true' sh {} \;

    mkdir -p "$pkgdir/usr/share/licenses/${pkgname}"
    printf "%s\n" "MIT" > "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}
