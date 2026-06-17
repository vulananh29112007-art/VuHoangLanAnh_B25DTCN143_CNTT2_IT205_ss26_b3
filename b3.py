from abc import ABC, abstractmethod

class Champion(ABC):
    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    def get_combat_power(self):
        return self.base_hp + self.calculate_skill_damage() * 1.5

    def __add__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other

    def __radd__(self, other):
        return self.__add__(other)

    def __gt__(self, other):
        return self.get_combat_power() > other.get_combat_power()


class Warrior(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power

    def calculate_skill_damage(self):
        return self.base_atk * self.ability_power


champion_pool = [
    Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
    Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
    Mage("MAG01", "Rikkei Wizard", 800, 500, 2)
]


def find_champion(champion_id):
    for champion in champion_pool:
        if champion.champion_id == champion_id:
            return champion
    return None


def display_champions():
    for champion in champion_pool:
        if isinstance(champion, Warrior):
            role = "Warrior"
            info = f"Armor: {champion.shield_bonus}"
        else:
            role = "Mage"
            info = f"AP: {champion.ability_power}"

        print(f"{champion.champion_id} | {champion.name} | {role} | HP: {champion.base_hp} | ATK: {champion.base_atk} | {info} | Power: {champion.get_combat_power()}")


def add_champion():
    role = input("Chọn hệ (1-Warrior, 2-Mage): ")

    champion_id = input("Nhập mã tướng: ").strip().upper()

    if find_champion(champion_id):
        print("Mã tướng đã tồn tại!")
        return

    name = input("Nhập tên tướng: ")
    hp = int(input("Nhập HP: "))
    atk = int(input("Nhập ATK: "))

    if role == "1":
        armor = int(input("Nhập Armor: "))
        champion_pool.append(
            Warrior(champion_id, name, hp, atk, armor)
        )
        print("Thêm Warrior thành công!")

    elif role == "2":
        ap = float(input("Nhập Ability Power: "))
        champion_pool.append(
            Mage(champion_id, name, hp, atk, ap)
        )
        print("Thêm Mage thành công!")

    else:
        print("Hệ không hợp lệ")


def compare_champions():
    id1 = input("Nhập mã tướng thứ nhất: ").strip().upper()
    id2 = input("Nhập mã tướng thứ hai: ").strip().upper()

    champion1 = find_champion(id1)
    champion2 = find_champion(id2)

    if champion1 is None:
        print(f"Mã tướng {id1} không hợp lệ!")
        return

    if champion2 is None:
        print(f"Mã tướng {id2} không hợp lệ!")
        return

    if champion1 > champion2:
        print(f"{champion1.name} mạnh hơn {champion2.name}")
    else:
        print(f"{champion2.name} mạnh hơn hoặc bằng {champion1.name}")


def calculate_team_power():
    ids = input("Nhập danh sách mã tướng: ").upper().split(",")

    total_power = 0

    for champion_id in ids:
        champion = find_champion(champion_id.strip())

        if champion is None:
            print(f"Mã tướng {champion_id.strip()} không hợp lệ, bỏ qua!")
            continue

        total_power += champion

    print(f"Tổng chiến lực đội hình: {total_power:.0f}")


while True:
    print("""
===== RIKKEI RPG AUTO BATTLER =====
1. Hiển thị bể tướng
2. Thêm quân cờ
3. So sánh quân cờ
4. Tính tổng chiến lực đội hình
5. Thoát
""")

    choice = input("Chọn chức năng: ")

    match choice:
        case "1":
            display_champions()
        case "2":
            add_champion()
        case "3":
            compare_champions()
        case "4":
            calculate_team_power()
        case "5":
            print("Cảm ơn bạn đã sử dụng!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")
