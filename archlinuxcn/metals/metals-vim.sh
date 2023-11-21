#!/bin/bash

set -e

_METALS_CLIENT=vim-lsc exec metals-client "$@"
