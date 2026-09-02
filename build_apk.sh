#!/bin/bash
set -e
cd "$(dirname "$0")"
buildozer -v android debug
