# load_env_file(){
# 	set -o allexport
# 	source $1
# 	set +o allexport
# }

# load_env_file .env



API_NAME=$(basename $(pwd))
DATE="$(date +%Y-%m-%d)"


if [[ "$*" == *--current* ]]; then
    docker exec $API_NAME  bash -c "alembic current"
    exit 0
fi
if [[ "$*" == *--init* ]];then
    docker exec $API_NAME  bash -c "alembic init alembic"
    exit 0
fi
if [[ "$*" == *--auto* ]]; then
    docker exec $API_NAME  bash -c "alembic revision --autogenerate "
    exit 0
fi
if [[ "$*" == *--up-1* ]]; then
    docker exec $API_NAME  bash -c "alembic upgrade +1"
    exit 0
fi
if [[ "$*" == *--down-1* ]]; then
    docker exec $API_NAME  bash -c "alembic downgrade -1"
    exit 0
fi

#actualiza a la ultima version
if [[ "$*" == *--up* ]]; then
    docker exec $API_NAME  bash -c "alembic upgrade head"
    exit 0
fi
#hace downgrade a la version anterior a la ultima
if [[ "$*" == *--down* ]]; then
    docker exec $API_NAME  bash -c "alembic downgrade head-1"
    exit 0
fi
if [[ "$*" == *--recreate* ]]; then
    docker exec $API_NAME  bash -c "alembic downgrade base"
    docker exec $API_NAME  bash -c "alembic upgrade head"
    exit 0
fi
