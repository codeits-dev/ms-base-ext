# Base Api Project for Micro Services
--------------------------------------------

This is a  Flask-based service that significantly enhances the speed of development, thanks to its many built-in functionalities.
It will allow you to focus on developing business logic rather than technical aspects, enabling you to build applications more efficiently.

## Included functionalities.
 - Api Swagger (open api 3.0)
 - GraphQl
 - Sql Alchemy with Alembic
 - MongoEngine
 - Exception Api handle
 - Log level
 - Debug
 - JWT Auth
 - Unit Test
 - Test Coverage

--------------------------------------------
## How to run

```bash
cd ms-base-ext
docker-compose up --build
```

--------------------------------------------
## Try swagger-ui

```
http://localhost:8080/test/api/v1/ui/

```

--------------------------------------------
## Try graphql

```
http://localhost:8080/graphql

```
--------------------------------------------
## vscode launch.json debug sample

```json
{
    "version": "0.2.0",
    "configurations": [
        
        {
            "name": "API: Debug",
            "type": "python",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 5678
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}/ms-base-ext",
                    "remoteRoot": "/api-run"
                }
            ],
            "justMyCode": false
        }
    ]
}
```