from app import (
    create_table,
    insert_user,
    get_users,
    update_user,
    delete_user
)

import allure


@allure.feature("Database operations")
def test_db_flow():

    with allure.step("Create table"):
        create_table()

    with allure.step("Insert user"):
        insert_user("TestUser", 30)

    with allure.step("Get users"):
        users = get_users()
        assert len(users) > 0

    user_id = users[-1][0]

    with allure.step("Update user"):
        update_user(user_id, "UpdatedUser")

    with allure.step("Verify update"):
        users = get_users()
        assert any(u[1] == "UpdatedUser" for u in users)

    with allure.step("Delete user"):
        delete_user(user_id)

    with allure.step("Verify delete"):
        users = get_users()
        assert not any(u[0] == user_id for u in users)