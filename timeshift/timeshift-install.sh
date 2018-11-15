post_upgrade() {
  set -u
  if ! systemctl -q is-enabled 'cronie.service'; then
    echo 'TimeShift automatic backups require the cronie.service to be running.'
    echo 'Try:'
    echo '  systemctl enable --now cronie.service'
  fi
  set +u
}

post_install() {
  post_upgrade
}
