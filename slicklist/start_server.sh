#! /bin/sh

cd "$(dirname "$0")"
export CONFIG=config_prod.json && python3 mitchell_server.py