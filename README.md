
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


### Retrieve an actual list of buckets from S3

- Edit bucket_list/views.py to get buckets and attributes with boto3
- Edit the urls config file bucket_list/urls.py for the buckets/ path
- Create a new template file - templates/bucket_list/bucket.html


### Prepare deploy to ECS

- Create Dockerfile
- Create docker-compose.yml
- Push image to Docker Hub

```
docker build -t bucket_peek .
docker login --username=tmcgz
docker tag bucket_peek tmcgz/bucket_peek
docker push tmcgz/bucket_peek:latest
```

### Deploy to ECS

- Create a task role in IAM e.g. 'ecsBucketPeekRole' and attach ecsBucketPeekPolicy.json inline policy
- Create a ECS cluster (Fargate)
- When creating the ECS task definition:
    * use 'ecsBucketPeekRole' for the task role (taskRoleArn, the credentials of the actual task)
    * use 'ecsTaskExecutionRole' for the task execution role (to retrieve container images)
- When adding the container:
    * Container name = 'BucketPeekContainer' 
    * Image = docker.io/tmcgz/containerofcats
    * Command (comma-separated) = python,bucket_peek/manage.py,runserver,0.0.0.0:80
- Run a new task based off the ECS task definition
    * Type = FARGATE
    * Select a security group that allows incoming port 80 and all outbound traffic
- Go to the public IP address, e.g. http://54.206.6.121


TODO: Push image to Elastic Container Registry instead of Docker Hub!