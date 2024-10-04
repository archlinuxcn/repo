#!/bin/bash

# Define the paths for the certificate and private key files
CERT_DIR="/var/lib/derper/certs"
CONFIG_FILE="/etc/derper/openssl.cnf"

# Extract the commonName (CN) value from the openssl.cnf file using sed
DOMAIN=$(sed -n 's/^[[:space:]]*commonName[[:space:]]*=[[:space:]]*//p' "$CONFIG_FILE")

# Define the certificate and key files based on the commonName
CERT_FILE="$CERT_DIR/$DOMAIN.crt"
KEY_FILE="$CERT_DIR/$DOMAIN.key"

# Check if the directory exists
if [[ ! -d "$CERT_DIR" ]]; then
    mkdir "$CERT_DIR"
fi

# Check if the certificate file exists
if [[ ! -f "$CERT_FILE" ]]; then
    echo "Certificate file does not exist, generating a new certificate..."
    openssl req -x509 -newkey ec:<(openssl ecparam -name prime256v1) -nodes -days 365 -keyout "$KEY_FILE" -out "$CERT_FILE" -config "$CONFIG_FILE"
else
    # Check if the certificate will expire within the next 30 days
    if openssl x509 -checkend 2592000 -in "$CERT_FILE"; then
        echo "Certificate is valid, no need to regenerate."
    else
        echo "Certificate is about to expire, generating a new certificate..."
        openssl req -x509 -newkey ec:<(openssl ecparam -name prime256v1) -nodes -days 365 -keyout "$KEY_FILE" -out "$CERT_FILE" -config "$CONFIG_FILE"
    fi
fi
