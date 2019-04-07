update_vim_help() {
  echo -n "Updating Vim help tags..."
  /usr/bin/vim --noplugin -u NONE -U NONE \
    --cmd ":helptags /usr/share/vim/vimfiles/doc" --cmd ":q" > /dev/null 2>&1
  echo "done."
}

post_install() {
  update_vim_help
  #echo "==> ------------------------------------------------------------------------------------------------------------------------------"
  #echo
  #echo "==> add: \"let g:ycm_global_ycm_extra_conf = '/usr/share/vim/vimfiles/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'\" to your vimrc"
  #echo
  #echo "==> ------------------------------------------------------------------------------------------------------------------------------"
}

post_upgrade() {
  update_vim_help
}

post_remove() {
  update_vim_help
  #echo "==> ---------------------------------------------------------------------------------------------------------------------------------"
  #echo
  #echo "==> remove: \"let g:ycm_global_ycm_extra_conf = '/usr/share/vim/vimfiles/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'\" in your vimrc"
  #echo
  #echo "==> ---------------------------------------------------------------------------------------------------------------------------------"
}
