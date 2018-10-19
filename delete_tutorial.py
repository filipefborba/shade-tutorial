from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

instances = conn.list_servers()
for instance in instances:
    instance_id = instance.id

conn.delete_server(name_or_id=instance_id)
