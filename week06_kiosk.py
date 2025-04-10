# 1 ) 아아 : 2000 2) 라떼 : 2500

prices = [2000, 2500]
drinks = ["아이스 아메리카노","카페 라떼"]
total_price = 0
amounts = [0, 0]
# order_list = ""
while True:
    menu = input(f"1) {drinks[0]} {prices[0]}원 2) {drinks[1]} {prices[1]}원 3) 주문종료 : ")
    if menu == "1":
        print(f"{drinks[0]}를 주문하셨습니다. 가격은 {prices[0]}원입니다.")
        total_price += prices[0]
        amounts[0] +=1
        # order_list += drinks[0] + "\n"
    elif menu == "2":
        print(f"{drinks[1]}를 주문하셨습니다. 가격은 {prices[1]}원입니다.")
        total_price += prices[1]
        amounts[1] += 1
        # order_list += drinks[1] + "\n"
    elif menu == "3":
        print("주문을 종료합니다.")
        break
    else:
        print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요.")

# print(order_list)
print(f"{drinks[0]} {prices[0]}원 {amounts[0]}잔 {amounts[0] * prices[0]}원")
print(f"{drinks[1]} {prices[1]}원 {amounts[1]}잔 {amounts[1] * prices[1]}원")
print(f"총 주문 급액 : {total_price}")
