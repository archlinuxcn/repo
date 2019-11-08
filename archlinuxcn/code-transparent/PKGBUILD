# Maintainer: frantic1048 <i@frantic1048.com>
# Contributor: Filipe Laíns (FFY00) <lains@archlinux.org>
# Contributor: Michael Hansen <zrax0111 gmail com>
# Contributor: Francisco Magalhães <franmagneto gmail com>

pkgname=code-transparent
_pkgname=code
pkgdesc='The Open Source build of Visual Studio Code (vscode) editor - with transparency enabled.'
# Important: Remember to check https://github.com/microsoft/vscode/wiki/How-to-Contribute#prerequisites for target node version
# NodeJS versioning cheatsheet:
#   - carbon: 8
#   - dubnium: 10
# Important: Remember to check https://github.com/microsoft/vscode/blob/master/.yarnrc (choose correct tag) for target electron version
pkgver=1.39.2
pkgrel=1
arch=('x86_64')
url='https://github.com/microsoft/vscode'
license=('MIT')
depends=('electron4' 'libsecret' 'libx11' 'libxkbfile' 'ripgrep')
optdepends=('bash-completion: Bash completions'
            'zsh-completions: ZSH completitons')
makedepends=('git' 'gulp' 'npm' 'python2' 'yarn' 'nodejs-lts-dubnium')
conflicts=('code')
provides=('code')
install='code-transparent.install'
source=("$_pkgname::git+https://github.com/Microsoft/vscode.git#tag=$pkgver"
        'code.js'
        'code.sh'
        'product_json.diff'
        'enable-proposed-apis.diff'
        'transparent.diff')
sha512sums=('SKIP'
            '814c9554427183cd893a33cd2cbe91f6e0ea71921ef0717c86217b1d3058d265f9ff7a9ace3e7b76f122e60b7686475cf4d999e581a1845face3033afb9f745f'
            'dfd9ca38e6510c9ad59fb24c1141fdfeb136f457392aee79b0bc2ff378c4c54d81a06728ba3ec4039d57dfcd730c26686585de9b4032a21ee8151a4f05195c15'
            '8ec47e497287d67f37e7b669af416f43d5cdbd4574892867d7b95996ef5de53640b5bc919b06b177e1fd91cb005579d6ed0c17325117b9914ba7cf28f5f06e40'
            'b267dcedaf51067a782d0f14007663b706973c1538f7fb91f093475134c2145fd0ffd5ed2b47ad7f01c6167a78a4af285d2818d7850fc67a7f7a473324824664'
            '09e417a861d8c84855714253a65aeb954575a1ca51f5ef0fc6bc2aaa6fee9ba507325ce9ed2d450ba070d461456ef5fa60993ac68fc89f21c7d2f9ebe6631266')

# Even though we don't officially support other archs, let's
# allow the user to use this PKGBUILD to compile the package
# for his architecture
case "$CARCH" in
  i686)
    _vscode_arch=ia32
    ;;
  x86_64)
    _vscode_arch=x64
    ;;
  armv7h)
    _vscode_arch=arm
    ;;
  *)
    # Needed for mksrcinfo
    _vscode_arch=DUMMY
    ;;
esac

prepare() {
  cd $_pkgname

  # This patch no longer contains proprietary modifications.
  # See https://github.com/Microsoft/vscode/issues/31168 for details.
  patch -p0 < ../product_json.diff

  # enable window transparency
  patch -p1 <../transparent.diff

  # Set the commit and build date
  local _commit=$(git rev-parse HEAD)
  local _datestamp=$(date -u -Is | sed 's/\+00:00/Z/')
  sed -e "s/@COMMIT@/$_commit/" -e "s/@DATE@/$_datestamp/" -i product.json

  # See https://github.com/MicrosoftDocs/live-share/issues/262 for details
  # Also, https://github.com/microsoft/vscode/issues/48946
  patch -p1 < ../enable-proposed-apis.diff

  # Build native modules for system electron
  local _target=$(</usr/lib/electron4/version)
  sed -i "s/^target .*/target \"${_target//v/}\"/" .yarnrc

  # Patch appdata and desktop file
  sed -i 's|/usr/share/@@NAME@@/@@NAME@@|@@NAME@@|g
          s|@@NAME_SHORT@@|Code|g
          s|@@NAME_LONG@@|Code - OSS|g
          s|@@NAME@@|code-oss|g
          s|@@ICON@@|code-oss|g
          s|@@EXEC@@|/usr/bin/code-oss|g
          s|@@LICENSE@@|MIT|g
          s|@@URLPROTOCOL@@|vscode|g
          s|inode/directory;||' resources/linux/code{.appdata.xml,.desktop,-url-handler.desktop}

  # Add missing exectable name to bash completion
  sed -i 's|complete -F _code code|complete -F _code code code-oss|' resources/completions/bash/code
  # Create new zsh completion file for our binary
  cp resources/completions/zsh/_code resources/completions/zsh/_code-oss
  sed -i 's|#compdef code|#compdef code code-oss|' resources/completions/zsh/_code-oss

  # Fix bin path
  sed -i "s|return path.join(path.dirname(execPath), 'bin', \`\${product.applicationName}\`);|return '/usr/bin/code';|g
          s|return path.join(appRoot, 'scripts', 'code-cli.sh');|return '/usr/bin/code';|g" \
          src/vs/platform/environment/node/environmentService.ts
}

build() {
  # https://github.com/mapbox/node-sqlite3/issues/1044
  mkdir -p path
  ln -sf /usr/bin/python2 path/python
  export PATH="$PWD/path:$PATH"

  cd $_pkgname

  yarn install --arch=$_vscode_arch

  # The default memory limit may be too low for current versions of node
  # to successfully build vscode. Change it if this number still doesn't
  # work for your system.
  mem_limit="--max_old_space_size=8192"

  if ! /usr/bin/node $mem_limit /usr/bin/gulp vscode-linux-$_vscode_arch-min
  then
      echo
      echo "*** NOTE: If the build failed due to running out of file handles (EMFILE),"
      echo "*** you will need to raise your max open file limit."
      echo "*** You can check this for more information on how to increase this limit:"
      echo "***    https://ro-che.info/articles/2017-03-26-increase-open-files-limit"
      exit 1
  fi
}

package() {
  # Install resource files
  install -dm 755 "$pkgdir"/usr/lib/$_pkgname
  cp -r --no-preserve=ownership --preserve=mode VSCode-linux-$_vscode_arch/resources/app/* "$pkgdir"/usr/lib/$_pkgname/

  # replace statically included binary with system copy
  ln -sf /usr/bin/rg "$pkgdir"/usr/lib/code/node_modules.asar.unpacked/vscode-ripgrep/bin/rg

  # Install binary
  install -Dm 755 code.sh "$pkgdir"/usr/bin/code-oss
  install -Dm 755 code.js "$pkgdir"/usr/lib/$_pkgname/code.js
  ln -sf /usr/bin/code-oss "$pkgdir"/usr/bin/code

  # Install appdata and desktop file
  install -Dm 644 $_pkgname/resources/linux/code.appdata.xml "$pkgdir"/usr/share/metainfo/code-oss.appdata.xml
  install -Dm 644 $_pkgname/resources/linux/code.desktop "$pkgdir"/usr/share/applications/code-oss.desktop
  install -Dm 644 $_pkgname/resources/linux/code-url-handler.desktop "$pkgdir"/usr/share/applications/code-oss-url-handler.desktop
  install -Dm 644 VSCode-linux-$_vscode_arch/resources/app/resources/linux/code.png "$pkgdir"/usr/share/pixmaps/code-oss.png

  # Install bash and zsh completions
  install -Dm 644 $_pkgname/resources/completions/bash/code "$pkgdir"/usr/share/bash-completion/completions/code-oss
  ln -s code-oss "$pkgdir"/usr/share/bash-completion/completions/code
  install -Dm 644 $_pkgname/resources/completions/zsh/_code-oss "$pkgdir"/usr/share/zsh/site-functions/_code-oss

  # Install license files
  install -Dm 644 VSCode-linux-$_vscode_arch/resources/app/LICENSE.txt "$pkgdir"/usr/share/licenses/$_pkgname/LICENSE
  install -Dm 644 VSCode-linux-$_vscode_arch/resources/app/ThirdPartyNotices.txt "$pkgdir"/usr/share/licenses/$_pkgname/ThirdPartyNotices.txt
}
