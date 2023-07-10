# 가상계좌 모듈 임포트
import virtual_account


# 상품권 구매 함수 정의
def buy_gift_card(amount):
    # 가상계좌 생성
    account = virtual_account.create()
    # 가상계좌 정보 출력
    print(f"가상계좌 번호: {account.number}")
    print(f"가상계좌 예금주: {account.owner}")
    print(f"가상계좌 입금액: {amount}원")
    # 가상계좌 입금 대기
    print("가상계좌에 입금해주세요.")
    account.wait_for_deposit()
    # 입금 확인 후 상품권 발급
    print("입금이 확인되었습니다.")
    gift_card = virtual_account.issue_gift_card(amount)
    # 상품권 정보 출력
    print(f"상품권 번호: {gift_card.number}")
    print(f"상품권 잔액: {gift_card.balance}원")
    print("감사합니다.")


# 예시 실행
buy_gift_card(10000)
