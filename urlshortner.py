import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url, custom_name=None):
        # If a custom name is provided, use it as the short key
        if custom_name:
            short_key = custom_name
        else:
            # Use a simple hash function to generate a short key
            hash_object = hashlib.sha1(original_url.encode())
            short_key = hash_object.hexdigest()[:8]

        # Check if the short key is already in use
        if short_key in self.url_mapping:
            return "Custom name already in use. Please choose a different one."

        # Store the mapping between the short key and the original URL
        self.url_mapping[short_key] = original_url

        # Return the shortened URL
        return f"short.url/{short_key}"

    def expand_url(self, short_url):
        # Extract the short key from the short URLc
        short_key = short_url.split('/')[-1]

        # Retrieve the original URL from the mapping
        original_url = self.url_mapping.get(short_key)

        if original_url:
            return original_url
        else:
            return "URL not found"

# Example usage:
url_shortener = URLShortener()

original_url = input("Enter the URL to shorten: ")
custom_name = input("Enter a custom name (leave blank for automatic generation): ")

short_url = url_shortener.shorten_url(original_url, custom_name)
print(f"Original URL: {original_url}")
print(f"Shortened URL: {short_url}")

expanded_url = url_shortener.expand_url(short_url)
print(f"Expanded URL: {expanded_url}")
