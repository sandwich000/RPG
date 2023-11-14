import random
import json

# 주사위 함수 정의
def dice6():
    return random.randint(1, 6)

# 랜덤 이벤트
def event():
    return random.randint(1, 3)

# 파일 이름
player_file = "player_stats.json"
enemy_file = "enemy_stats.json"

# 초기 플레이어와 적의 스탯
player_stats = {
    "maxhp": 100,
    "hp": 100,
    "atk": 10,
    "def": 3,
    "exp": 0,
    "mexp": 10  # 추가: 다음 레벨업에 필요한 경험치
}


# 파일에서 플레이어 스탯 불러오기
with open(player_file, "r") as file:
    player_stats = json.load(file)
# 파일에서 적 스탯 불러오기
with open(enemy_file, "r") as file:
    enemy_stats = json.load(file)


    


# 플레이어의 이전 스탯을 저장할 변수
previous_player_stats = None

enemy_stats = {
    "maxhp": 50,
    "hp": 50,
    "atk": 5,
    "def": 5,
    "exp": random.randint(1, 8)
}

# 레벨업 시 증가하는 스탯
plus_hp = random.randint(3, 10)
plus_def = random.randint(0, 2)
plus_atk = random.randint(2, 5)
plus_mexp = random.randint(2, 5)  # 추가: 다음 레벨업에 필요한 경험치 증가

while player_stats["hp"] > 0:
    # 플레이어의 공격
    user_input = input("플레이어의 공격을 실행하려면 엔터를 입력하세요. Q를 누르면 저장하고 나가기: ")
    if user_input.lower() == 'q':
        # 사용자가 'q'를 입력하면 현재 플레이어 스탯을 저장하고 프로그램 종료
        with open(player_file, "w") as file:
            json.dump(player_stats, file)
        break

    # 주사위 굴림
    d6 = dice6()

    # 주사위 결과 출력
    print(f'주사위 결과: {d6}')

    # 플레이어의 공격력을 주사위 결과에 반영
    player_damage = player_stats["atk"] * d6 / 2 - enemy_stats["def"]

    # 적의 체력을 플레이어의 공격력만큼 감소
    enemy_stats["hp"] = max(enemy_stats["hp"] - player_damage, 0)  # 음수 체력 방지

    # 적의 남은 체력 출력
    print(f'적의 남은 체력: {enemy_stats["hp"]}')

    # 적을 처치한 경우
    if enemy_stats["hp"] <= 0:
        print("적을 처치했다.")
        print(f'다음 레벨업까지 남은 경험치: {player_stats["exp"]} / {player_stats["mexp"]}')
        r_event = event()
        player_stats["exp"] += enemy_stats["exp"]

        # 레벨업 조건 확인
    if player_stats["exp"] >= player_stats["mexp"]:
        print('한층 더 강해진 느낌이다.')

        # 플레이어의 이전 스탯을 백업 (레벨업 이전 스탯 저장)
        previous_player_stats = {
            "maxhp": player_stats["maxhp"],
            "atk": player_stats["atk"],
            "def": player_stats["def"]
        }

        player_stats["maxhp"] += plus_hp
        player_stats["atk"] += plus_atk
        player_stats["def"] += plus_def

        # 플레이어의 체력을 최대 체력까지 회복
        player_stats["hp"] = player_stats["maxhp"]

        player_stats["exp"] = 0  # 경험치 초기화
        player_stats["mexp"] += plus_mexp  # 다음 레벨업 필요 경험치 업데이트
        # 재설정 및 다음 라운드 시작
        hp_up = random.randint(1, 5)
        atk_up = random.randint(1, 3)
        def_up = random.randint(1, 2)

        hp_up2 = random.randint(1, 3)
        atk_up2 = random.randint(1, 2)
        def_up2 = random.randint(1, 2)

        if r_event == 3:
            if player_stats["hp"] < player_stats["maxhp"] / 2:
                player_stats["hp"] = player_stats["maxhp"] / 2 + dice6()
                print("몸이 가벼워진 듯하다.")
            else:
                print('딱히 변화한건 없는듯하다.')
        if r_event == 2:  # 적 조금 강화
            enemy_stats["maxhp"] += hp_up2
            enemy_stats["def"] += def_up2
            enemy_stats["atk"] += atk_up2
            print('적이 조금 강해진 듯하다.')
        if r_event == 1:  # 적 강화
            enemy_stats["maxhp"] += hp_up
            enemy_stats["def"] += def_up
            enemy_stats["atk"] += atk_up
            print('적이 강해졌다..!')
        enemy_stats["exp"] = random.randint(1, 8)
        plus_hp = random.randint(3, 10)
        plus_def = random.randint(0, 2)
        plus_atk = random.randint(2, 5)

    if player_stats["hp"] > 0:
        # 적의 공격
        user_input = input("적의 공격을 실행하려면 엔터를 입력하세요. Q를 누르면 저장하고 나가기: ")
        if user_input.lower() == 'q':
            # 사용자가 'q'를 입력하면 현재 플레이어 스탯을 저장하고 프로그램 종료
            with open(player_file, "w") as file:
                json.dump(player_stats, file)
            break

        # 주사위 굴림
        d6 = dice6()

        # 주사위 결과 출력
        print(f'주사위 결과: {d6}')

        # 적의 공격력을 주사위 결과에 반영
        enemy_damage = enemy_stats["atk"] * d6 / 2 - player_stats["def"]

        # 플레이어의 체력을 적의 공격력만큼 감소
        player_stats["hp"] = max(player_stats["hp"] - enemy_damage, 0)  # 음수 체력 방지

        # 플레이어의 남은 체력 출력
        print(f'플레이어의 남은 체력: {player_stats["hp"]} / {player_stats["maxhp"]}')

# 게임 종료 시에 플레이어와 적의 스탯을 파일에 저장
with open(player_file, "w") as file:
    json.dump(player_stats, file)

with open(enemy_file, "w") as file:
    json.dump(enemy_stats, file)

# 게임 종료 메시지 출력
print("게임이 종료되었습니다!")

# 플레이어가 패배한 경우 이전 스탯을 불러와서 초기화
if player_stats["hp"] <= 0 and previous_player_stats is not None:
    print("플레이어가 패배했습니다.")
    player_stats = previous_player_stats
    print("이전 레벨 기준으로 플레이어 스탯을 초기화합니다.")
