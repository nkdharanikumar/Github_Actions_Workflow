import string
import random

class TinyURL:
    def __init__(self):
        self.url_map = {}

    def generate_code(self, length=6):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def shorten_url(self, original_url):
        short_code = self.generate_code()

        while short_code in self.url_map:
            short_code = self.generate_code()

        self.url_map[short_code] = original_url
        return short_code

    def get_original_url(self, short_code):
        return self.url_map.get(short_code)

    def delete_url(self, short_code):
        if short_code in self.url_map:
            del self.url_map[short_code]
            return True
        return False

    def total_urls(self):
        return len(self.url_map)