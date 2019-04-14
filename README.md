# Pickering

A website...

## Setting up the application - new developers

* Python 3.7.0
* SQLite Browser (optional)

Use python or python3 depending on the executable that has been installed

1. Create a python virtual environment
# macOS/Linux
```
sudo apt-get install python3-venv    # If needed
python3 -m venv env
```
# Windows
```
python -m venv env
```
2. Active the environment
# macOS/Linux
```
source env/bin/activate
```
# Windows
 ```
 env\scripts\activate
 ```

3. Restore packages

```
pip install -r requirements.txt
```

4. Setup the database

```
python manage.py migrate
``` 

5. Add yourself as a superuser

```
python manage.py createsuperuser --username=<username> --email=<email>
```

You can access this admin page by browsing to http://127.0.0.1:8000/admin

## Running the application


```
python manage.py runserver
```
Choose a different port by using the following command
```
python manage.py runserver 5000
```

TBC
Run static collected before deployment and copy files to...(azure storage)

```
python manage.py collectstatic
```

## Testing

Run the following command

```
python manage.py collectstatic
```

## Packaging

```
python setup.py sdist
```

## Deployment

Create azure web app and resource group
```
az webapp up -n pickering -l uksouth --sku B1
az webapp update -n pickering
az webapp show -n pickering
```

Delete resource group (and all resources)
```
az group delete --name appsvc_rg_Linux_uksouth
```

## Troubleshooting

## Notes