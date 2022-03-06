
## An example site to view S3 buckets

### Creating the site

```
> pip install django
> python -m django --version
4.0.3
> django-admin startproject bucket_peek
> cd bucket_peek
> python manage.py migrate
```

### Running the site
```
> python manage.py runserver
```

### Viewing a list of buckets
```
> python manage.py startapp bucket_list
```

- Create the urls config file bucket_list/urls.py
- Include the urls config in the main file bucket_peek/urls.py 
- Add the app name to INSTALLED_APPS in bucket_peek/settings.py
- Add the view in bucket_list/views.py
- Create a new template file - templates/bucket_list/index.html
