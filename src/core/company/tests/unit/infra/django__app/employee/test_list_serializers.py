import pytest
from model_bakery import baker

from core.company.infra.django_app.models import Employee
from core.company.infra.django_app.serializers import EmployeeListSerializer


@pytest.mark.django_db
class TestCompanyListSerializer:
    def test_list_serializer_with_many_employees(self) -> None:
        employees = baker.make(Employee, _quantity=3)
        serializer = EmployeeListSerializer(employees, many=True)
        assert len(serializer.data) == 3
        assert serializer.data == [
            {
                "id": str(employee.id),
                "company_id": str(employee.company_id),
                "user_id": str(employee.user_id),
                "is_active": employee.is_active,
            }
            for employee in employees
        ]

    def test_list_serializer_with_no_employees(self) -> None:
        employees = []
        serializer = EmployeeListSerializer(employees, many=True)
        assert serializer.data == []

    def test_list_serializer_with_one_employee(self) -> None:
        employee = baker.make(Employee)
        serializer = EmployeeListSerializer(employee, many=False)
        assert serializer.data == {
            "id": str(employee.id),
            "company_id": str(employee.company_id),
            "user_id": str(employee.user_id),
            "is_active": employee.is_active,
        }

    def test_retrieve_serializer_with_a_specific_employee(self) -> None:
        employee = baker.make(Employee)
        serializer = EmployeeListSerializer(employee)
        assert serializer.data == {
            "id": str(employee.id),
            "company_id": str(employee.company_id),
            "user_id": str(employee.user_id),
            "is_active": employee.is_active,
        }

    def test_retrieve_serializer_with_no_employee(self) -> None:
        employee = {}
        serializer = EmployeeListSerializer(employee)
        assert serializer.data == {}
