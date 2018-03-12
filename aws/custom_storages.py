# FILE CONFIG TO UPLOAD FILES TO S3 BUCKET

from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

# DEFINE STATIC LOCATION
class StaticStorage(S3BotoStorage):
	
	def __init__(self, *args, **kwargs):
		kwargs['location'] = settings.STATICFILES_LOCATION
		super(StaticStorage, self).__init__(*args, **kwargs)


# DEFINE MEDIA LOCATION
class MediaStorage(S3BotoStorage):

	def __init__(self, *args, **kwargs):
		kwargs['location'] = settings.MEDIAFILES_LOCATION
		super(MediaStorage, self).__init__(*args, **kwargs)