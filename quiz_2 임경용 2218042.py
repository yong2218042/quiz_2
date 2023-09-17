# 환율표 (Dictionary 타입)
exchange_rates = {
    "달러": 1200,  # 1 달러 = 1,200 원
    "엔화": 10,    # 1 엔화 = 10 원
    "위안화": 150  # 1 위안화 = 150 원
}

# 철수가 가진 돈 (리스트 요소)
cheolsu_money = [13, 200, 13]  # 달러, 엔화, 위안화 순서로 나열

# 각 화폐를 원화로 환산하여 합산
total_won = 0
for i in range(len(cheolsu_money)):
    currency = list(exchange_rates.keys())[i]  # 환율표의 통화 이름
    exchange_rate = exchange_rates[currency]   # 해당 통화의 환율
    amount = cheolsu_money[i]                  # 철수가 가진 돈의 양
    total_won += amount * exchange_rate        # 환산한 금액을 누적

# 결과 출력
print(f"철수가 가지고 있는 돈의 원화 가치는 {total_won} 원 입니다.")
