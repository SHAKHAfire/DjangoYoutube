from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.



class Posts(models.Model):
    title: str = models.CharField(max_length=50)
    content: str = models.TextField()
    author: User = models.ForeignKey(User,
                                     on_delete=models.SET_NULL, null=True, blank=True)
    # price: float = models.DecimalField(max_digits=5, decimal_places=2)
    created: datetime = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(
    #     default='books/book_default_img.png', upload_to="books")

    objects = models.Manager()  # default
    # c_objects = BooksManager()  # custom manager

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # if self.genre == None or self.genre == "":
        #     raise IntegrityError("Genre cannot be null")
        # if self.price == 0:
        #     raise NullPriceException
        super().save(*args, **kwargs)

        # We have to save the form first before getting the image path
        # img = Image.open(self.image.path)
        # if img.height > 600 or img.width > 600:
        #     output_size = (600, 600)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # image_url = self.image.url
        # if image_url != '/media/books/book_default_img.png':
        #     os.remove(self.image.path)

    # class Meta:
        # indexes = [
        #     models.Index(fields=['is_available', 'price']),
        # ]
        # permissions = [('can_change_book', 'Can change book')]