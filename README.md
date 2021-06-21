# Start

```
% docker-compose up -d
```

# Stop

```
% docker-compose down
```

# update code

```
% docker-compose up -d --no-deps --build $SERVICE_NAME 
```

# Mongodb init set
```
cfg =  {
		"_id" : "RS",
		members : [
					{
						"_id" : 0,
						"host" : "rs1:27041"
					},
					{
						"_id" : 1,
						"host" : "rs2:27042"
					},
					{
						"_id" : 2,
						"host" : "rs3:27043"
					},
		]
		
	}
```

```
rs.initiate(cfg);
```
```
rs.status().members.forEach(m => print(`${m.name} => ${m.stateStr}`))
```

# Server info


1. create user : <http://127.0.0.1/create_user/adduser>
2. list user : <http://127.0.0.1/list_user/list_user>
3. Login : <http://127.0.0.1/login/login>
