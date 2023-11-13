import uuid


async def test_create_user(client, get_user_from_database):
    user_data = {
        "name": "Baby",
        "surname": "Bone",
        'email': "babybone@gmail.com"
    }
    resp = client.post("/user/", json=user_data)
    data_from_resp = resp.json()
    assert resp.status_code == 200
    assert data_from_resp["name"] == user_data["name"]
    assert data_from_resp["surname"] == user_data["surname"]
    assert data_from_resp["email"] == user_data["email"]
    assert data_from_resp["is_active"] is True
    users_from_db = await get_user_from_database(data_from_resp["user_id"])
    assert len(users_from_db) == 1
    user_from_db = dict(users_from_db[0])
    assert user_from_db["name"] == user_data["name"]
    assert user_from_db["surname"] == user_data["surname"]
    assert user_from_db["email"] == user_data["email"]
    assert user_from_db["is_active"] is True
    assert str(user_from_db["user_id"]) == data_from_resp["user_id"]


async def test_delete_user(client, create_user_in_database, get_user_from_database):
    user_data = {
        "user_id": uuid.uuid4(),
        "name": "Baby_del",
        "surname": "Bone_del",
        'email': "babybonedel@gmail.com",
        "is_active": True
    }
    await create_user_in_database(**user_data)
    resp = client.delete(f'/user/?user_id={user_data["user_id"]}')
    resp_json = resp.json()
    assert resp.status_code == 200
    assert resp_json == {"user_id": str(user_data["user_id"])}
    users_from_db = await get_user_from_database(user_data["user_id"])
    user_from_db = users_from_db[0]
    assert user_from_db["name"] == user_data["name"]
    assert user_from_db["surname"] == user_data["surname"]
    assert user_from_db["email"] == user_data["email"]
    assert user_from_db["is_active"] is False
    assert str(user_from_db["user_id"]) == resp_json["user_id"]


async def test_get_user(client, create_user_in_database, get_user_from_database):
    user_data = {
        "user_id": uuid.uuid4(),
        "name": "Baby_get",
        "surname": "Bone_get",
        'email': "babyboneget@gmail.com",
        "is_active": True
    }

    await create_user_in_database(**user_data)
    resp = client.get(f'/user/?user_id={user_data["user_id"]}')
    resp_json = resp.json()
    user_from_db = await get_user_from_database(user_data["user_id"])
    user_from_db = user_from_db[0]
    user_data['user_id'] = str(user_data['user_id'])

    assert resp.status_code == 200
    assert user_data == resp_json
    assert str(user_from_db['user_id']) == user_data['user_id']
    assert user_from_db['name'] == user_data['name']
    assert user_from_db['surname'] == user_data['surname']
    assert user_from_db['email'] == user_data['email']
    assert user_from_db['is_active'] == user_data['is_active']


async def test_update_user(client, create_user_in_database, get_user_from_database):
    user_data = {
        "user_id": uuid.uuid4(),
        "name": "Baby_get",
        "surname": "Bone_get",
        'email': "babyboneget@gmail.com",
        "is_active": True
    }

    await create_user_in_database(**user_data)
    changed_data = {
        "name": "justbaby"
    }
    user_data['name'] = changed_data['name']

    resp = client.put(f'/user/?user_id={user_data["user_id"]}', json=changed_data)
    resp_json = resp.json()
    user_from_db = await get_user_from_database(user_data['user_id'])
    user_from_db = user_from_db[0]
    user_data['user_id'] = str(user_data['user_id'])

    assert resp.status_code == 200
    assert user_data == resp_json
    assert str(user_from_db['user_id']) == user_data['user_id']
    assert user_from_db['name'] == user_data['name']
    assert user_from_db['surname'] == user_data['surname']
    assert user_from_db['email'] == user_data['email']
    assert user_from_db['is_active'] == user_data['is_active']
