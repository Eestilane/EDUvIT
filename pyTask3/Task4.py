class Student:
    university = "Advanced Engineering School of Hybrid Technologies in Machine Tool Building of the Union State"
    default_year = 2023

    def __init__(self, name: str, group: str, course: int, major: str, admission_year: int) -> None:
        self.name = name
        self.group = group
        self.course = course
        self.major = major
        self.admission_year = admission_year

    def __str__(self) -> str:
        return f"Студент: {self.name}, Группа: {self.group}, {self.course} курс"

    def is_graduated(self, current_year: int) -> bool:
        return current_year - self.admission_year >= 4

    def change_group(self, new_group: str) -> None:
        self.group = new_group

    def promote(self) -> None:
        self.course += 1

    def get_study_years(self, current_year: int) -> int:
        return current_year - self.admission_year


student1 = Student("Лев Иванов", "0482-05", 2, "ИСТ", 2023)
student2 = Student("Никита Молоков", "0482-05", 2, "ИСТ", 2023)

print(student1)
print(student2)

print(f"\n{student1.name} выпустился? {student1.is_graduated(2025)}")
print(f"{student2.name} выпустился? {student2.is_graduated(2025)}")

student1.promote()
print(f"\n{student2.name} переведён на {student1.course} курс")

student2.change_group("0482-06")
print(f"\n{student1.name} переведён в группу {student2.group}, подальше от нас")

print(f"\n{student1.name} обучается уже аж целых {student1.get_study_years(2025)} год(а)")
print(f"{student2.name} обучается уже аж целых {student2.get_study_years(2025)} год(а)")