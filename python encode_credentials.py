import base64

# Read the credentials file and encode it to base64
with open('gs_credentials.json', 'rb') as f:
    encoded = base64.b64encode(f.read()).decode('utf-8')

# Print the encoded string
print(encoded)
