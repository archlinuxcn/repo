#!/bin/sh
# Start the Paseo daemon inside the graphical session. Intended to be launched
# by paseo.service, which an XDG autostart entry starts once the session is up
# (see the package's post_install notes), so the daemon inherits
# DISPLAY/WAYLAND_DISPLAY from the systemd --user manager environment and does
# not race gnome-shell during session init.
#
# Entry point: the CLI launcher at /usr/lib/paseo/packages/cli/bin/paseo is a
# plain Node script, so it spawns the daemon supervisor correctly. Do NOT use
# /usr/bin/paseo here — that is the Electron GUI wrapper and cannot start the
# node-mode supervisor.
#
# Wrap in the interactive login shell (-ilc) so the daemon and its agents get
# the full PATH (git, node, ~/.local/bin CLIs). --foreground keeps this process
# as the daemon so logout/stop cleanly tears it down.
exec "$(getent passwd "$(id -u)" | cut -d: -f7)" -ilc \
  "exec /usr/lib/paseo/packages/cli/bin/paseo daemon start --foreground"
