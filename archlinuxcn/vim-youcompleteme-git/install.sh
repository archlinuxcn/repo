update_vim_help() {
  echo -n "Updating Vim help tags..."
  /usr/bin/vim --noplugin -u NONE -U NONE \
    --cmd ":helptags /usr/share/vim/vimfiles/doc" --cmd ":q" >/dev/null 2>&1
  echo "done."
}

post_install() {
  update_vim_help
  echo "For rust support be sure to setup a default toolchain with rustup"
  echo "rls, rust-analysis and rust-src are needed for whatever toolchain you are using."
  echo "Example:"
  echo -e "\trustup toolchain install nightly"
  echo -e "\trustup default nightly"
  echo -e "\trustup component add rls rust-analysis rust-src"
  echo -e "\n\n\n"
}

post_upgrade() {
  update_vim_help
  echo "For rust support be sure to setup a default toolchain with rustup"
  echo "rls, rust-analysis and rust-src are needed for whatever toolchain you are using."
  echo "Example:"
  echo -e "\trustup toolchain install nightly"
  echo -e "\trustup default nightly"
  echo -e "\trustup component add rls rust-analysis rust-src"
  echo -e "\n\n\n"
}

post_remove() {
  update_vim_help
}
