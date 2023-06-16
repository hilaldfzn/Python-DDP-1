from __future__ import annotations
from random import randint

class Entity:
    def __init__(self, name: str, hp: int, atk: int) -> None:
        self.__name = name
        self.__atk = atk
        self.__hp = hp
        
    def get_name(self) -> str:
        return self.__name

    def get_atk(self) -> int:
        return self.__atk

    def get_hp(self) -> int:
        return self.__hp

    def set_hp(self, new_hp) -> None:
        self.__hp = new_hp

    def attack(self, other: Entity) -> int:
        return other.take_damage(self.__atk)

    def take_damage(self, damage) -> int:
        self.__hp -= damage
        return damage

    def is_alive(self) -> bool:
        return self.__hp > 0

    def __str__(self) -> str:
        return self.__name

# Class Player yang merupakan child class dari Entity
class Player(Entity):
    def __init__(self, name: str, hp: int, atk: int, defense: int) -> None:
        super().__init__(name, hp, atk)
        self.__defense = defense

    def attack(self, other) -> int:
        return super().attack(other)

    def get_defense(self) -> int:
        return self.__defense

    def take_damage(self, damage) -> int:
        new_damage = max(0, damage - self.__defense)
        return super().take_damage(new_damage)

# Class Boss yang merupakan child class dari Entity
class Boss(Entity):
    def __init__(self, name, hp, atk) -> None:
        super().__init__(name, hp, atk)

    def attack(self, other: Player) -> int:             # Type: ignore
        other.set_hp(other.get_hp() - self.get_atk())
        return self.get_atk()

def main():
    # Meminta input user untuk ATK dan DEF Depram
    atk = int(input("Masukkan ATK Depram: "))
    defense = int(input("Masukkan DEF Depram: "))

    # Membuat objek Player dengan nama "Depram" dan atribut ATK dan DEF dari input
    depram = Player("Depram", 100, atk, defense)

    # Membuat beberapa objek musuh dengan nama "Enemy {i}", HP dan ATK yang diacak dan jumlah 1 atau 2
    enemies = [
        Entity(f"Enemy {i}", randint(20, 100), randint(10, 30))
        for i in range(randint(1, 2))
    ]

    # Menambahkan satu objek Boss dengan nama "Ohio Final Boss", HP dan ATK yang diacak
    enemies.append(Boss("Ohio Final Boss", randint(20, 100), randint(10, 30)))

    # Mencetak banyak musuh yang menghadang
    print(f"Terdapat {len(enemies)} yang menghadang Depram!")
    print("------------")

    # Mencetak ringkasan enemy yang muncul serta ATK yang diberikan antara Depram dan enemy
    # Selain itu, terdapat info mengenai siapa yang terkalahkan
    for enemy in enemies:
        print(f"{enemy} muncul!")
        print()
        print("---Status---")
        print(f"{enemy.get_name():20} HP: {enemy.get_hp()}")
        print(f"{depram.get_name():20} HP: {depram.get_hp()}")
        print("------------")

        while enemy.is_alive() and depram.is_alive():
            damage = depram.attack(enemy)
            print(f"Depram menyerang {enemy} dengan {damage} ATK!")

            if not enemy.is_alive():
                break

            damage = enemy.attack(depram)
            print(f"{enemy} menyerang Depram dengan {damage} ATK!")

        if not depram.is_alive():
            print("------------")
            print()
            print("Tidak! Depram telah dikalahkan oleh musuhnya :(")
            return
        else:
            print(f"{enemy} telah kalah!")

        print("------------")
        print()

    print("Selamat! Semua musuh Depram telah kalah!")

if __name__ == "__main__":
    main()
