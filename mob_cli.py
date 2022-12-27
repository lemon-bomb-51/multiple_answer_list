def multiple_answer_list(mul_ans, max_num):
    for i in range(max_num):
        if i % mul_ans == 0 and i > 0:
            exponent = i // mul_ans
            print('배수 : ',i,' / ',exponent,' 승(제곱)')
            
# 0-199중에 9의 배수가 어떤것이 있는지 리스트로 만들어 주는 함수
multiple_answer_list(9, 200)
