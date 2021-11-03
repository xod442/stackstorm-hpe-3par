# HPE 3Par Integration Pack
This pack allows you to integrate with HPE 3Par

## Configuration
Copy the example configuration in [hpe3Par.yaml.example](./hpe3Par.yaml.example) to
`/opt/stackstorm/configs/hpe3Par.yaml` and edit as required.

It must contain:

```
ipaddress - Your 3Par array IP address
username - 3Par User name
password - 3Par Password
dbuser  - Mongo database username
dbpass - Mongo database password
```

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

Example configuration:

```yaml
---
  ipaddress: "10.10.10.10"
  username: "Administrator"
  password: "password"
  dbuser: "appUser"
  dbpass: "passwordForAppUser"
```
You can also run `st2 pack config hpe3Par` and answer the prompts

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`


## Actions

Actions are defined in two groups:

### Individual actions: GET, POST, PUT with under bar will precede each individual action
* ``get_volumes``
* ``post_volumes``
* ``get_events``
* ``get_alarms``

### Orquestra Workflows: will not

This application uses the mongo db installed by StackStorm. Since the DB is secured
you will need to log into the StackStorm mongo DB as a StackStorm admin and create a separate DB

# To get this pack to work with StackStorm mongo DB

log in with admin first
--------------------------------------------------------------------------------------
mongo -u admin -p UkIbDILcNbMhkh3KtN6xfr9h admin  (passwd in /etc/st2/st2.config)

# Then create a new user
db.createUser({user: "appUser",pwd: "passwordForAppUser",roles: [ { role: "readWrite", db: "app_db" } ]})

# Then if necessary you can check the mongo database records by
mongo -u appUser -p passwordForAppUser admin
