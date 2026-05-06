from app import create_table, insert_user, get_users, update_user, delete_user

def test_db_flow():
    create_table()

    insert_user("TestUser", 30)

    users = get_users()
    assert len(users) > 0

    user_id = users[-1][0]

    update_user(user_id, "UpdatedUser")

    users = get_users()
    assert any(u[1] == "UpdatedUser" for u in users)

    delete_user(user_id)

    users = get_users()
    assert not any(u[0] == user_id for u in users)