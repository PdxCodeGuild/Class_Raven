from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
# import uuid # for unique key instances (eg. multiple keys for the same lock)

class KeyType(models.Model):
    """Model representing the key is used for."""
    name = models.CharField(max_length=200, help_text='Enter what key is used for (e.g. Vehicle, Door , Locker, Padlock)')

    def __str__(self):
        return self.name

class KeyId(models.Model):
    """Model representing a key (but not a specific copy of)."""
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the key')
    usefor = models.ManyToManyField(KeyType, help_text='Select what this key is used for')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this key."""
        return reverse('key-detail', args=[str(self.id)])                       #CHECK

    def display_usefor(self):
        """Create a string for usefor. This is required to display usefor in Admin.""" # CHECK THIS
        return ', '.join(genre.name for genre in self.usefor.all()[:3])

    display_usefor.short_description = 'usefor'



class KeyInstance(models.Model):
    """Model representing a specific copy of a key (i.e. that can be borrowed from the key library)."""
    id = models.CharField(max_length=10, primary_key=True, help_text='Unique ID for this particular key across whole library')
    key = models.ForeignKey('KeyId', on_delete=models.RESTRICT, null=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Missing'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Key availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.key.title})'
