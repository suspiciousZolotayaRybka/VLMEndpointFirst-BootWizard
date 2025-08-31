"""
development_HTTPS_signed_certifications.py

16 August 2025
Author: Isaac Finehout

This .py create self signed HTTPS certs for testing

NOT FOR PRODUCTION ENVIRONMENT
"""

import datetime

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

# Generate key
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
with open("key.pem", "wb") as f:
    f.write(
        key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )

# Generate certificate
subject = issuer = x509.Name(
    [
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "SD"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "Rapid City"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Scarecrow"),
        x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
    ]
)
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.datetime.utcnow())
    .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
    .sign(key, hashes.SHA256())
)

with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Generated cert.pem and key.pem")
