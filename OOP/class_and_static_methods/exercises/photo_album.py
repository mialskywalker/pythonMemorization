class PhotoAlbum:
    MAX_PHOTOS = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]
        self.has_free_space = False

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        index = 0
        for i in range(self.pages):
            if len(self.photos[i]) >= PhotoAlbum.MAX_PHOTOS:
                self.has_free_space = False
            else:
                self.has_free_space = True
                index = i
                break
        if not self.has_free_space:
            return "No more free slots"

        self.photos[index].append(label)
        return f"{label} photo added successfully on page" \
               f" {index + 1} slot {self.photos[index].index(self.photos[index][-1]) + 1}"

    def display(self):
        result = "-----------\n"
        for i in range(self.pages):
            result += '[] ' * len(self.photos[i])
            result = result.strip()
            if len(self.photos[i]) <= 0:
                result += '\n'
            result += '\n-----------\n'
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
