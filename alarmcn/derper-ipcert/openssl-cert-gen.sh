#!/usr/bin/bash

# Path to the OpenSSL configuration file
CONFIG_FILE="/etc/derper/openssl.cnf"

# Directory for storing generated certificate files
CERT_DIR="/var/lib/derper/certs"

# Extract the commonName (CN) from the OpenSSL configuration file
DOMAIN=$(sed -n 's/^[[:space:]]*commonName[[:space:]]*=[[:space:]]*//p' "$CONFIG_FILE")

# Paths for the generated certificate and key files
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
