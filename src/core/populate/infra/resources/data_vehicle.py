import uuid

bodies_data = [
    {"description": "Baú", "id": "d77b81f3-8eaa-4b08-a8f4-a60524a3d40f"},
    {"description": "Carroceria Aberta", "id": "fea18fde-8c59-4e13-8dec-c3d9b866a74e"},
    {"description": "Sider", "id": "9ab9f166-2a19-4887-aae8-ff27c9aeacf7"},
    {"description": "Graneleiro", "id": "c326d1be-d9b0-4437-826a-6fbc4c036736"},
    {"description": "Porta-Container", "id": "5d611c2b-9693-47ba-9a42-09c7014c9d66"},
]


modalities_data = [
    {"id": uuid.uuid4(), "description": "Caminhão 2 eixos", "axle": "2 eixos"},
    {"id": uuid.uuid4(), "description": "Caminhão 3 eixos", "axle": "3 eixos"},
    {"id": uuid.uuid4(), "description": "Caminhão Toco", "axle": "2 eixos simples"},
    {"id": uuid.uuid4(), "description": "Caminhão Truck", "axle": "3 eixos simples"},
    {
        "id": uuid.uuid4(),
        "description": "Carreta Cavalo Mecânico 2 eixos",
        "axle": "4 eixos",
    },
    {
        "id": uuid.uuid4(),
        "description": "Carreta Cavalo Mecânico 3 eixos",
        "axle": "5 eixos",
    },
    {"id": uuid.uuid4(), "description": "Carreta Bitrem", "axle": "7 eixos"},
    {"id": uuid.uuid4(), "description": "Carreta Rodotrem", "axle": "9 eixos"},
    {"id": uuid.uuid4(), "description": "Caminhão Munck", "axle": "4 eixos"},
    {"id": uuid.uuid4(), "description": "Caminhão Baú", "axle": "3 eixos"},
]
