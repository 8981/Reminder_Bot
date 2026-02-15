from repositories.user_repo import (
    add_user as repo_add_user,
    update_user as repo_update_user,
    get_all_users as repo_get_all_users
)

async def create_user(user_id, username, full_name):
    await repo_add_user(user_id, username, full_name)


async def update_user(user_id, username, full_name):
    await repo_update_user(user_id, username, full_name)


async def get_all_users():
    return await repo_get_all_users()
