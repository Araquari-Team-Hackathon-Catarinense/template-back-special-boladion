import random
import re
import uuid

from faker import Faker
from pycpfcnpj import gen

faker = Faker("pt_BR")


def generate_cpf():
    return re.sub("[^0-9]", "", gen.cpf())


def generate_cnpj():
    return re.sub("[^0-9]", "", gen.cnpj())


def generate_address():
    return {
        "zip_code": re.sub("[^0-9]", "", faker.postcode()),
        "address": faker.street_address(),
        "number": random.randint(1, 9999),
        "district": faker.bairro(),
        "city_name": faker.city(),
        "city_ibge_code": faker.random_number(digits=7),
        "state_acronym": faker.state_abbr(),
        "state_ibge_code": faker.random_number(digits=7),
    }


def generate_contacts(index, type):
    return [
        {
            "name": faker.name(),
            "phone": re.sub("[^0-9]", "", faker.phone_number()),
            "email": f"{type}{index}.admin@example.com",
            "obs": "Administrativo",
        }
    ]


def generate_companies():
    companies = []

    for index in range(10):
        index += 1
        company_pj = {
            "id": str(uuid.uuid4()),
            "name": f"Empresa {index}",
            "trade_name": f"Nome Fantasia {index}",
            "person_type": "PJ",
            "document_number": generate_cnpj(),
            "is_active": True,
            "system_admin": False,
            "address": generate_address(),
            "contacts": generate_contacts(index, "pj"),
        }
        companies.append(company_pj)

    for index in range(10):
        index += 1
        company_pf = {
            "id": str(uuid.uuid4()),
            "name": faker.name(),
            "trade_name": None,
            "person_type": "PF",
            "document_number": generate_cpf(),
            "is_active": True,
            "system_admin": False,
            "address": generate_address(),
            "contacts": generate_contacts(index, "pf"),
        }
        companies.append(company_pf)

    return companies


# companies_json = generate_companies()

# import json

# print(json.dumps(companies_json, indent=4, ensure_ascii=False))

companies_data = [
    {
        "id": "51134a9e-ab9b-4d4d-9b34-905250b459a1",
        "name": "Empresa 1",
        "trade_name": "Nome Fantasia 1",
        "person_type": "PJ",
        "document_number": "45291724117522",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "40700848",
            "address": "Vale de Cardoso, 47",
            "number": 51,
            "district": "Cidade Nova",
            "city_name": "Novais de Goiás",
            "city_ibge_code": 9483100,
            "state_acronym": "AM",
            "state_ibge_code": 1285756,
        },
        "contacts": [
            {
                "name": "Ana Vitória Santos",
                "phone": "5508434956906",
                "email": "pj1.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "8f216264-99ce-457e-8eb1-eeed0779e54f",
        "name": "Empresa 2",
        "trade_name": "Nome Fantasia 2",
        "person_type": "PJ",
        "document_number": "26528122620104",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "17328961",
            "address": "Morro Nascimento, 24",
            "number": 8335,
            "district": "Jardim América",
            "city_name": "Câmara da Serra",
            "city_ibge_code": 2072633,
            "state_acronym": "RJ",
            "state_ibge_code": 2777199,
        },
        "contacts": [
            {
                "name": "Rafaela Lopes",
                "phone": "555163559619",
                "email": "pj2.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "9c6c5d6e-d9ca-41f6-80e9-aa9cee15ff9d",
        "name": "Empresa 3",
        "trade_name": "Nome Fantasia 3",
        "person_type": "PJ",
        "document_number": "61589512786158",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "64876907",
            "address": "Condomínio Duarte, 59",
            "number": 7637,
            "district": "Confisco",
            "city_name": "da Luz do Norte",
            "city_ibge_code": 6632474,
            "state_acronym": "PE",
            "state_ibge_code": 2024863,
        },
        "contacts": [
            {
                "name": "Luigi Guerra",
                "phone": "7161717850",
                "email": "pj3.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "e8bc8e00-b532-4f8c-acc7-21712c56f16a",
        "name": "Empresa 4",
        "trade_name": "Nome Fantasia 4",
        "person_type": "PJ",
        "document_number": "25307376090734",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "97137713",
            "address": "Fazenda de da Rosa, 52",
            "number": 413,
            "district": "São Lucas",
            "city_name": "Ramos do Amparo",
            "city_ibge_code": 809812,
            "state_acronym": "AC",
            "state_ibge_code": 3227974,
        },
        "contacts": [
            {
                "name": "Maria Helena Duarte",
                "phone": "5501139898800",
                "email": "pj4.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "b63400a0-f358-4b38-8e22-86a299ea94fa",
        "name": "Empresa 5",
        "trade_name": "Nome Fantasia 5",
        "person_type": "PJ",
        "document_number": "15999335183466",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "23740594",
            "address": "Praça de Porto",
            "number": 3347,
            "district": "Centro",
            "city_name": "Castro",
            "city_ibge_code": 3373212,
            "state_acronym": "AL",
            "state_ibge_code": 2595397,
        },
        "contacts": [
            {
                "name": "Ana Sophia Andrade",
                "phone": "5502159119471",
                "email": "pj5.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "cb6826cd-69f2-4d40-bcd0-a61cf9488190",
        "name": "Empresa 6",
        "trade_name": "Nome Fantasia 6",
        "person_type": "PJ",
        "document_number": "22127545654058",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "14305475",
            "address": "Travessa Gael Henrique Cardoso, 36",
            "number": 3228,
            "district": "Dom Joaquim",
            "city_name": "da Costa",
            "city_ibge_code": 8309345,
            "state_acronym": "MA",
            "state_ibge_code": 6594740,
        },
        "contacts": [
            {
                "name": "Benício Macedo",
                "phone": "558141163229",
                "email": "pj6.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "57273561-e183-45b9-b45e-dce9f6199a44",
        "name": "Empresa 7",
        "trade_name": "Nome Fantasia 7",
        "person_type": "PJ",
        "document_number": "04147545365516",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "60615032",
            "address": "Passarela de Aragão",
            "number": 7108,
            "district": "Vila Bandeirantes",
            "city_name": "da Rocha de Novaes",
            "city_ibge_code": 9999474,
            "state_acronym": "MG",
            "state_ibge_code": 3252420,
        },
        "contacts": [
            {
                "name": "Ana Júlia Cardoso",
                "phone": "4190323622",
                "email": "pj7.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "c06f3922-f391-44d7-84f6-df7071bcd8b5",
        "name": "Empresa 8",
        "trade_name": "Nome Fantasia 8",
        "person_type": "PJ",
        "document_number": "26808427187778",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "53968273",
            "address": "Jardim Leão, 61",
            "number": 7522,
            "district": "Jardim Vitoria",
            "city_name": "Andrade",
            "city_ibge_code": 8868971,
            "state_acronym": "MA",
            "state_ibge_code": 3650189,
        },
        "contacts": [
            {
                "name": "Dr. Daniel Marques",
                "phone": "1191809065",
                "email": "pj8.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "0fb48b90-6faf-4f2c-b0d4-9204a4013618",
        "name": "Empresa 9",
        "trade_name": "Nome Fantasia 9",
        "person_type": "PJ",
        "document_number": "34948322323867",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "33783848",
            "address": "Favela Sampaio, 53",
            "number": 9229,
            "district": "Heliopolis",
            "city_name": "Abreu",
            "city_ibge_code": 9913089,
            "state_acronym": "SP",
            "state_ibge_code": 2209896,
        },
        "contacts": [
            {
                "name": "Mariah Teixeira",
                "phone": "5501101118951",
                "email": "pj9.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "355edb16-0802-4699-a04f-4c9883bfb0a4",
        "name": "Empresa 10",
        "trade_name": "Nome Fantasia 10",
        "person_type": "PJ",
        "document_number": "63201464417680",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "67551153",
            "address": "Recanto Gael Cavalcante, 28",
            "number": 2958,
            "district": "Santo Agostinho",
            "city_name": "Sousa",
            "city_ibge_code": 3528000,
            "state_acronym": "PR",
            "state_ibge_code": 5258788,
        },
        "contacts": [
            {
                "name": "Sra. Milena Siqueira",
                "phone": "5504155523598",
                "email": "pj10.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "dc1e0e3b-fb2a-4e86-babe-1fe743a8b243",
        "name": "Liam Novaes",
        "trade_name": None,
        "person_type": "PF",
        "document_number": "19760855275",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "59544021",
            "address": "Feira da Mota, 99",
            "number": 2379,
            "district": "Jardim América",
            "city_name": "Freitas",
            "city_ibge_code": 4694493,
            "state_acronym": "MG",
            "state_ibge_code": 489117,
        },
        "contacts": [
            {
                "name": "Maria Fernanda da Cunha",
                "phone": "552182517399",
                "email": "pf1.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "4f15c32e-bf5e-4c83-9cad-107d984e1f9b",
        "name": "Lorena Barbosa",
        "trade_name": None,
        "person_type": "PF",
        "document_number": "66561205804",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "11711881",
            "address": "Chácara Caldeira, 29",
            "number": 2195,
            "district": "Comiteco",
            "city_name": "Mendonça",
            "city_ibge_code": 8610327,
            "state_acronym": "SP",
            "state_ibge_code": 4409560,
        },
        "contacts": [
            {
                "name": "Srta. Luara Ramos",
                "phone": "558165631669",
                "email": "pf2.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "92fca8a9-8831-47f0-8a44-9cdb638382ce",
        "name": "Henry Rios",
        "trade_name": None,
        "person_type": "PF",
        "document_number": "74495022598",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "32801365",
            "address": "Sítio Bárbara Nogueira, 79",
            "number": 2255,
            "district": "Aguas Claras",
            "city_name": "Mendonça da Prata",
            "city_ibge_code": 7973334,
            "state_acronym": "RS",
            "state_ibge_code": 1466066,
        },
        "contacts": [
            {
                "name": "Pedro Henrique Cirino",
                "phone": "553128421759",
                "email": "pf3.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "b6eee124-c5c0-4699-9dc6-c17fad0d6ce0",
        "name": "Ana Liz da Cunha",
        "trade_name": None,
        "person_type": "PF",
        "document_number": "03190007535",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "53659223",
            "address": "Aeroporto Cavalcante, 35",
            "number": 4510,
            "district": "Vila Suzana Primeira Seção",
            "city_name": "Gonçalves Alegre",
            "city_ibge_code": 8603661,
            "state_acronym": "SP",
            "state_ibge_code": 2017211,
        },
        "contacts": [
            {
                "name": "Maria Sophia Rios",
                "phone": "09000801432",
                "email": "pf4.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "52ea638f-a5fd-48c6-8301-fa7b1795262a",
        "name": "Clara Fogaça",
        "trade_name": None,
        "person_type": "PF",
        "document_number": "49757804703",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "32716433",
            "address": "Passarela de Câmara, 5",
            "number": 8529,
            "district": "Vila Canto Do Sabiá",
            "city_name": "Barros",
            "city_ibge_code": 5797730,
            "state_acronym": "PA",
            "state_ibge_code": 4262504,
        },
        "contacts": [
            {
                "name": "Luan Pires",
                "phone": "553134279495",
                "email": "pf5.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "fbbc1589-84fb-47ca-a522-b4d3b28fc16a",
        "name": "Henrique Gomes",
        "trade_name": None,
        "person_type": "PF",
        "document_number": "53633262806",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "39313865",
            "address": "Passarela Porto",
            "number": 6700,
            "district": "Barreiro",
            "city_name": "da Cruz da Prata",
            "city_ibge_code": 7444044,
            "state_acronym": "AC",
            "state_ibge_code": 4196021,
        },
        "contacts": [
            {
                "name": "Caio Farias",
                "phone": "6183489477",
                "email": "pf6.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "e207bd91-4388-4bf6-92e5-7fe5e04fbfb5",
        "name": "Isabelly Fonseca",
        "trade_name": None,
        "person_type": "PF",
        "document_number": "38026274903",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "08397647",
            "address": "Estação Benício Rezende, 679",
            "number": 2492,
            "district": "Marieta 3ª Seção",
            "city_name": "Lopes",
            "city_ibge_code": 3547780,
            "state_acronym": "BA",
            "state_ibge_code": 339437,
        },
        "contacts": [
            {
                "name": "Ana Laura Barros",
                "phone": "5508431952214",
                "email": "pf7.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "7c9c43d5-ef68-4ac5-ab9c-6cd3a427a5f7",
        "name": "Srta. Maitê Araújo",
        "trade_name": None,
        "person_type": "PF",
        "document_number": "41858789150",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "25030278",
            "address": "Feira de Teixeira, 222",
            "number": 6415,
            "district": "Lorena",
            "city_name": "Silveira de Vieira",
            "city_ibge_code": 7292007,
            "state_acronym": "RS",
            "state_ibge_code": 9408919,
        },
        "contacts": [
            {
                "name": "Srta. Gabriela Jesus",
                "phone": "5506138394970",
                "email": "pf8.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "3baf99d9-f7da-4cc1-b4f8-45c7986aa1d2",
        "name": "João Pedro Sampaio",
        "trade_name": None,
        "person_type": "PF",
        "document_number": "74439744001",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "19056004",
            "address": "Morro Sophia Sá, 73",
            "number": 6284,
            "district": "Andiroba",
            "city_name": "Nascimento do Campo",
            "city_ibge_code": 4032555,
            "state_acronym": "SC",
            "state_ibge_code": 2330152,
        },
        "contacts": [
            {
                "name": "Raul Araújo",
                "phone": "1124956237",
                "email": "pf9.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
    {
        "id": "fad6a6b7-93bf-4692-a2c5-4e60942e6121",
        "name": "Sr. Arthur Gabriel Fernandes",
        "trade_name": None,
        "person_type": "PF",
        "document_number": "91718212283",
        "is_active": True,
        "system_admin": False,
        "address": {
            "zip_code": "15047152",
            "address": "Travessa de Brito, 99",
            "number": 4942,
            "district": "Cidade Jardim",
            "city_name": "Campos",
            "city_ibge_code": 5746490,
            "state_acronym": "RJ",
            "state_ibge_code": 6419631,
        },
        "contacts": [
            {
                "name": "Dra. Luiza Ramos",
                "phone": "09002681638",
                "email": "pf10.admin@example.com",
                "obs": "Administrativo",
            }
        ],
    },
]
