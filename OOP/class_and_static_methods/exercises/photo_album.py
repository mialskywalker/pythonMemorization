class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        self.spots_remaining = self.get_capacity(PhotoAlbum.MAX_PHOTOS_PER_PAGE, self.pages)

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count)

    def add_photo(self, label: str):
        if self.spots_remaining <= 0:
            return "No more free spots"
        for i in range(self.pages):
            if len(self.photos[i]) >= 4:
                continue
            else:
                self.photos.append(label)
                self.spots_remaining -= 1
                return f"{label} photo added successfully on page " \
                       f"{i + 1} slot {self.photos.index(label)}"

    def display(self):
        result = ''
        for _ in range(self.pages + 1):
            result += '-----------'
            # TODO DISPLAY

    @staticmethod
    def get_capacity(max_per_page, pages):
        return max_per_page * pages


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
