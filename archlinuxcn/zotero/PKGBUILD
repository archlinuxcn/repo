# Maintainer: Aaron Keesing <agkphysics at gmail dot com>

pkgname=zotero
pkgver=7.0.24
pkgrel=1
pkgdesc="A free, easy-to-use tool to help you collect, organize, cite, and share your research sources."
arch=('x86_64' 'i686')
url="https://github.com/zotero/zotero"
license=('AGPL-3.0-or-later')
depends=('dbus-glib' 'gtk3' 'nss' 'libxt')
makedepends=('npm' 'git' 'zip' 'unzip' 'perl' 'python>=3' 'curl' 'wget' 'rsync' 'nodejs' 'patch')
_tag=245c018ec0d15cf32cc123bc57ecb0f155634fde  # git rev-parse $pkgver
source=("zotero.desktop"
        "zotero-client::git+https://github.com/zotero/zotero.git#tag=${_tag}"
        "zotero-translators::git+https://github.com/zotero/translators.git"
        "zotero-styles::git+https://github.com/zotero/bundled-styles.git"
        "zotero-pdf-worker::git+https://github.com/zotero/pdf-worker.git"
        "zotero-note-editor::git+https://github.com/zotero/note-editor.git"
        "zotero-reader::git+https://github.com/zotero/reader.git"
        "zotero-schema::git+https://github.com/zotero/zotero-schema.git"
        "zotero-SingleFile::git+https://github.com/gildas-lormeau/SingleFile.git"
        "zotero-utilities::git+https://github.com/zotero/utilities.git"
        "zotero-translate::git+https://github.com/zotero/translate.git"
        "zotero-csl::git+https://github.com/citation-style-language/locales.git"
        "zotero-libreoffice-integration::git+https://github.com/zotero/zotero-libreoffice-integration.git"
        "zotero-pdf-js::git+https://github.com/zotero/pdf.js.git"
        "zotero-epub-js::git+https://github.com/zotero/epub.js.git"
        "disable-updater.patch")
sha256sums=('eab76db7a56a4d9aaa17baaf240b82fcf57944a4ddf8ef1b58cc64182426cedc'
            'e7f21a0a0d8561b8e58a2ecba564f89aceff87792b84083360deb460787601a4'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'dc1894ac2e1520c3dae8e9cd5e09608f4bb3298bdede2891a77118187edffa9d')

pkgver() {
  cd "$srcdir/zotero-client"
  git describe --tags
}

prepare() {
  cd "$srcdir/zotero-client"

  patch -N -p1 < "$srcdir/disable-updater.patch"

  npm i --legacy-peer-deps

  git submodule init
  git submodule deinit --force app/modules/zotero-word-for-mac-integration app/modules/zotero-word-for-windows-integration
  git config submodule.translators.url "$srcdir/zotero-translators"
  git config submodule.styles.url "$srcdir/zotero-styles"
  git config submodule.pdf-worker.url "$srcdir/zotero-pdf-worker"
  git config submodule.note-editor.url "$srcdir/zotero-note-editor"
  git config submodule.reader.url "$srcdir/zotero-reader"
  git config submodule.resource/schema/global.url "$srcdir/zotero-schema"
  git config submodule.resource/SingleFile.url "$srcdir/zotero-SingleFile"
  git config submodule.chrome/content/zotero/xpcom/utilities.url "$srcdir/zotero-utilities"
  git config submodule.chrome/content/zotero/xpcom/translate.url "$srcdir/zotero-translate"
  git config submodule.chrome/content/zotero/locale/csl.url "$srcdir/zotero-csl"
  git config submodule.app/modules/zotero-libreoffice-integration.url "$srcdir/zotero-libreoffice-integration"
  git -c protocol.file.allow=always submodule update

  cd "$srcdir/zotero-client/chrome/content/zotero/xpcom/utilities"
  git config submodule.resource/schema/global.url "$srcdir/zotero-schema"
  git -c protocol.file.allow=always submodule update

  cd "$srcdir/zotero-client/chrome/content/zotero/xpcom/translate/modules/utilities"
  git config submodule.resource/schema/global.url "$srcdir/zotero-schema"
  git -c protocol.file.allow=always submodule update

  cd "$srcdir/zotero-client/reader"
  git submodule init
  # Stupid hack because of dangling commit
  git -C "$srcdir/zotero-pdf-js" fetch "https://github.com/zotero/pdf.js.git" 67a1769bdaa0e89a6e239fcbaa5bf72b845223a0
  git config submodule.pdfjs/pdf.js.url "$srcdir/zotero-pdf-js"
  git config submodule.epubjs/epub.js.url "$srcdir/zotero-epub-js"
  git -c protocol.file.allow=always submodule update

  cd "$srcdir/zotero-client/pdf-worker"
  git submodule init
  # Ditto
  git -C "$srcdir/zotero-pdf-js" fetch "https://github.com/zotero/pdf.js.git" 8ac2ccc54dab2049cd92096c3448d6fdfab436ac
  git config submodule.pdf.js.url "$srcdir/zotero-pdf-js"
  git -c protocol.file.allow=always submodule update
}

build() {
  cd "$srcdir/zotero-client"
  NODE_OPTIONS=--openssl-legacy-provider npm run build
  app/scripts/dir_build -q
}

package() {
  install -dDm755 "$pkgdir"/usr/{bin,lib/zotero}
  cp -r "$srcdir/zotero-client/app/staging/Zotero_linux-$CARCH"/* "$pkgdir/usr/lib/zotero"
  ln -s /usr/lib/zotero/zotero "$pkgdir/usr/bin/zotero"
  install -Dm644 "$srcdir/zotero.desktop" "$pkgdir/usr/share/applications/zotero.desktop"

  # Copy zotero icons to a standard location
  install -Dm644 "$pkgdir/usr/lib/zotero/icons/icon32.png" "$pkgdir/usr/share/icons/hicolor/32x32/apps/zotero.png"
  install -Dm644 "$pkgdir/usr/lib/zotero/icons/icon64.png" "$pkgdir/usr/share/icons/hicolor/64x64/apps/zotero.png"
  install -Dm644 "$pkgdir/usr/lib/zotero/icons/icon128.png" "$pkgdir/usr/share/icons/hicolor/128x128/apps/zotero.png"
  install -Dm644 "$pkgdir/usr/lib/zotero/icons/symbolic.svg" "$pkgdir/usr/share/icons/hicolor/symbolic/apps/zotero-symbolic.svg"

  # Close shell when launching
  sed -i -r 's:^("\$CALLDIR/zotero-bin" -app "\$CALLDIR/application.ini" "\$@"):exec \1:' "$pkgdir/usr/lib/zotero/zotero"
}
