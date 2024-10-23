from pylint.checkers.utils import is_super


valid_uuids = [
    "c13b8ed0-33c0-4b56-9512-f3178a3c17e2",
    "3b795b52-5541-48fc-82fe-1441f42b318d",
    "e7ae9b59-5ba1-4c93-908f-38068337a1a0",
    "36e286ce-02b1-426d-b874-7f27c9bedb75",
    "eec96111-7d60-4c05-abb7-b9c30a7d91a4",
    "53395bfe-ca65-4247-b096-494645cae21e",
    "e4aba6df-1ea7-4d0c-9274-83c1b65fb889",
    "0c951677-bc0d-4b5c-ae4f-2dade92e7279",
    "101ee338-a1c1-4703-bd64-8748386e5a85",
    "5c9454c6-3392-4f9f-8eb9-d07f196e4180",
    "bdde0b5f-7893-4143-baf4-f89c17905dfa",
    "356c6355-9ef6-45d8-8058-f7dc8d812b5c",
    "c9b90dcd-877f-4efb-8a2d-cf5bb28acdde",
    "3d1da362-2b2a-4a63-bd12-24bc06d8fc62",
    "960e899a-2a03-46ff-985e-1fa022feb4eb",
    "21cac52f-b975-4172-bcba-334cd9da0265",
    "58e719ce-b5da-4336-9884-7917b973b570"
]

users_data = [
    {
        "id": valid_uuids[0],
        "name": "Admin",
        "email": "admin@empresa.com",
        "is_active": True,
        "is_superuser": True,
        "password": "admin"
    },
    {
        "id": valid_uuids[1],
        "name": "User 1",
        "email": "user1@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user1"
    },
    {
        "id": valid_uuids[2],
        "name": "User 2",
        "email": "user2@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user2"
    },
    {
        "id": valid_uuids[3],
        "name": "User 3",
        "email": "user3@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user3"
    },
    {
        "id": valid_uuids[4],
        "name": "User 4",
        "email": "user4@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user4"
    },
    {
        "id": valid_uuids[5],
        "name": "User 5",
        "email": "user5@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user5"
    },
    {
        "id": valid_uuids[6],
        "name": "User 6",
        "email": "user6@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user6"
    },
    {
        "id": valid_uuids[7],
        "name": "User 7",
        "email": "user7@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user7"
    },
    {
        "id": valid_uuids[8],
        "name": "User 8",
        "email": "user8@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user8"
    },
    {
        "id": valid_uuids[9],
        "name": "User 9",
        "email": "user9@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user9"
    },
    {
        "id": valid_uuids[10],
        "name": "User 10",
        "email": "user10@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user10"
    },
    {
        "id": valid_uuids[11],
        "name": "User 11",
        "email": "user11@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user11"
    },
    {
        "id": valid_uuids[12],
        "name": "User 12",
        "email": "user12@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user12"
    },
    {
        "id": valid_uuids[13],
        "name": "User 13",
        "email": "user13@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user13"
    },
    {
        "id": valid_uuids[14],
        "name": "User 14",
        "email": "user14@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user14"
    },
    {
        "id": valid_uuids[15],
        "name": "User 15",
        "email": "user15@empresa.com",
        "is_active": True,
        "is_superuser": False,
        "password": "user15"
    }
]
