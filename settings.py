import os
MEDIA_URL='/images/'
STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'bookmyshow',
        'HOST':'localhost',
        'PORT':'3306', 
        'USER':'root',
        'PASSWORD':'sql123inlife'
    }
}
