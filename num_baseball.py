# -*- coding: utf-8 -*-

import easygui
import random

select_mode=easygui.buttonbox("모드를 선택하세요.","제4회 BSS OPEN LAB - 숫자야구",choices=['1인용','2인용','종료'])


while True:
    if select_mode=='1인용':
        easygui.msgbox("숫자야구 1인 룰\n1) 처음 정한 4자리 수를 구성하는 숫자는 0에서 9까지 서로 다른 숫자이다.\n2) 숫자는 맞지만 위치가 틀렸을 때는 볼(Ball) 임을 알려준다.\n3) 숫자와 위치가 전부 맞으면 스트라이크(Strike) 임을 알려준다.\n4) 숫자와 위치가 전부 틀리면 아웃(Out) 임을 알려준다.\n","제4회 BSS OPEN LAB - 숫자야구")
        com=[]
        times=0
        correct=0
        while 4>len(com):
            x=str(random.randint(0,9))
            if x not in com:
                com.append(x)
        while True:
            choice_sub=easygui.buttonbox("무엇을 하시겠습니까?","제4회 BSS OPEN LAB - 숫자야구",choices=['숫자 찾기','정답 맞추기','새로 시작'])
            if choice_sub=='숫자 찾기':
                strike=0
                ball=0
                result=[]
                check=0
                choice_com=easygui.multenterbox("숫자를 입력하세요.","제4회 BSS OPEN LAB - 숫자야구",['첫번째 자리','두번째 자리','세번째 자리','네번째 자리'],['','','',''])
                for i in range(3):
                        for j in range(len(choice_com)-i-1):
                            if choice_com[i]==choice_com[i+j+1]:
                                check=1
                                break
                if check==1:
                    easygui.msgbox("같은 숫자는 입력할 수 없습니다. \n각 자리에는 서로 다른 숫자를 입력해주세요^^" ,"제4회 BSS OPEN LAB - 숫자야구")
                else:
                    if len(choice_com[0])==len(choice_com[1])==len(choice_com[2])==len(choice_com[3])==1 :                            
                        for i in range(4):
                            for j in range(4):
                                if choice_com[i]==com[j]:
                                    ball+=1
                            if choice_com[i]==com[i]:
                                ball-=1
                                strike+=1               
                        result.append(strike)
                        result.append(ball)
                        if ball==0 and strike==0:
                            print(''.join(choice_com),'OUT')
                            times+=1
                            easygui.msgbox('OUT'+'\n\n'+'횟수 : '+str(times),"제4회 BSS OPEN LAB - 숫자야구")
                        elif ball==0:
                            print(''.join(choice_com),str(result[0])+'S')
                            times+=1
                            easygui.msgbox(str(result[0])+'STRIKE'+'\n\n'+'횟수 : '+str(times),"제4회 BSS OPEN LAB - 숫자야구")
                        elif strike==0:
                            print(''.join(choice_com),str(result[1])+'B')
                            times+=1
                            easygui.msgbox(str(result[1])+'BALL'+'\n\n'+'횟수 : '+str(times),"제4회 BSS OPEN LAB - 숫자야구")
                        else:
                            print(''.join(choice_com),str(result[0])+'S'+str(result[1])+'B')
                            times+=1
                            easygui.msgbox(str(result[0])+'STRIKE'+' '+str(result[1])+'BALL'+'\n\n'+'횟수 : '+str(times),"제4회 BSS OPEN LAB - 숫자야구")  
                    else:
                         easygui.msgbox("숫자를 잘못 입력했습니다.\n각 자리에는 한 자리 수만 입력해주세요^^","제4회 BSS OPEN LAB - 숫자야구")
            elif choice_sub=='정답 맞추기':
                choice_really=easygui.buttonbox("정말 후회 안하시고 정답을 입력할 것 입니까? \n돌이킬 수 없어요. 진심으로.","제4회 BSS OPEN LAB - 숫자야구",choices=['정답 맞추기','숫자 찾으러 가기'])
                if choice_really=='정답 맞추기':
                    answer=easygui.multenterbox("컴퓨터의 숫자를 입력하세요.","제4회 BSS OPEN LAB - 숫자야구",['첫번째 자리','두번째 자리','세번째 자리','네번째 자리'],['','','',''])
                    if com==answer:
                        correct+=1
                        easygui.msgbox("정답입니다!\n상품을 받아가세요!\n숫자를 찾은 횟수 : "+str(times)+"\n"+"정답 시도 횟수 : "+str(correct),"제4회 BSS OPEN LAB - 숫자야구")
                        break
                    else:
                        correct+=1
                        easygui.msgbox("틀렸습니다.\n다시 한 번 잘 생각해보세요.\n숫자를 찾은 횟수 : "+str(times)+"\n"+"정답 시도 횟수 : "+str(correct),"제4회 BSS OPEN LAB - 숫자야구")
            else:
                break
        break
    elif select_mode=='2인용':
        easygui.msgbox("숫자야구 2인 룰\n1) 처음 정한 4자리 수를 구성하는 숫자는 0에서 9까지 서로 다른 숫자이다.\n2) 숫자는 맞지만 위치가 틀렸을 때는 볼(Ball) 임을 상대방에게 알린다.\n3) 숫자와 위치가 전부 맞으면 스트라이크(Strike) 임을 상대방에게 알린다.\n4) 숫자와 위치가 전부 틀리면 아웃(Out) 임을 상대방에게 알린다.\n","제4회 BSS OPEN LAB - 숫자야구")
        choice_p1=easygui.multenterbox("플레이어 1의 숫자를 입력하세요.","제4회 BSS OPEN LAB - 숫자야구",['첫번째 자리','두번째 자리','세번째 자리','네번째 자리'],['','','',''])
        choice_p2=easygui.multenterbox("플레이어 2의 숫자를 입력하세요.","제4회 BSS OPEN LAB - 숫자야구",['첫번째 자리','두번째 자리','세번째 자리','네번째 자리'],['','','',''])
        times_p1=0
        times_p2=0
        correct=0
        print('플레이어 1','                ','플레이어 2')
        while True:
            turn_p1=easygui.buttonbox("플레이어 1의 차례입니다.","제4회 BSS OPEN LAB - 숫자야구",choices=['숫자 찾기','정답 맞추기'])
            if turn_p1=='숫자 찾기':
                strike=0
                ball=0
                result=[]
                choice_com=easygui.multenterbox("숫자를 입력하세요.","제4회 BSS OPEN LAB - 숫자야구",['첫번째 자리','두번째 자리','세번째 자리','네번째 자리'],['','','',''])
                for i in range(4):
                    for j in range(4):
                        if choice_com[i]==choice_p2[j]:
                            ball+=1
                    if choice_com[i]==choice_p2[i]:
                        ball-=1
                        strike+=1               
                result.append(strike)
                result.append(ball)
                times_p1+=1
                if ball==0 and strike==0:
                    print(''.join(choice_com),'OUT',end='                     ')
                    easygui.msgbox('OUT'+'\n\n'+'횟수 : '+str(times_p1),"제4회 BSS OPEN LAB - 숫자야구")
                elif ball==0:
                    print(''.join(choice_com),str(result[0])+'S',end='                     ')
                    easygui.msgbox(str(result[0])+'STRIKE'+'\n\n'+'횟수 : '+str(times_p1),"제4회 BSS OPEN LAB - 숫자야구")
                elif strike==0:
                    print(''.join(choice_com),str(result[1])+'B',end='                     ')
                    easygui.msgbox(str(result[1])+'BALL'+'\n\n'+'횟수 : '+str(times_p1),"제4회 BSS OPEN LAB - 숫자야구")
                else:
                    print(''.join(choice_com),str(result[0])+'S'+str(result[1])+'B',end='                     ')
                    easygui.msgbox(str(result[0])+'STRIKE'+' '+str(result[1])+'BALL'+'\n\n'+'횟수 : '+str(times_p1),"제4회 BSS OPEN LAB - 숫자야구")  
            else:
                answer=easygui.multenterbox("플레이어 2의 숫자를 입력하세요.","제4회 BSS OPEN LAB - 숫자야구",['첫번째 자리','두번째 자리','세번째 자리','네번째 자리'],['','','',''])
                if choice_p2==answer:
                    correct+=1
                    easygui.msgbox("정답입니다!\n상품을 받아가세요!\n숫자를 찾은 횟수 : "+str(times_p1)+"\n"+"정답 시도 횟수 : "+str(correct),"제4회 BSS OPEN LAB - 숫자야구")
                    break
                else:
                    correct+=1
                    easygui.msgbox("틀렸습니다.\n다시 한 번 잘 생각해보세요.\n숫자를 찾은 횟수 : "+str(times_p1)+"\n"+"정답 시도 횟수 : "+str(correct),"제4회 BSS OPEN LAB - 숫자야구")
                    print('오답',end='                        ')
            turn_p2=easygui.buttonbox("플레이어 2의 차례입니다.","제4회 BSS OPEN LAB - 숫자야구",choices=['숫자 찾기','정답 맞추기'])
            if turn_p2=='숫자 찾기':
                strike=0
                ball=0
                result=[]
                choice_com=easygui.multenterbox("숫자를 입력하세요.","제4회 BSS OPEN LAB - 숫자야구",['첫번째 자리','두번째 자리','세번째 자리','네번째 자리'],['','','',''])
                for i in range(4):
                    for j in range(4):
                        if choice_com[i]==choice_p1[j]: 
                            ball+=1
                    if choice_com[i]==choice_p1[i]:
                        ball-=1
                        strike+=1               
                result.append(strike)
                result.append(ball)
                times_p2+=1
                if ball==0 and strike==0:
                    print(''.join(choice_com),'OUT')
                    easygui.msgbox('OUT'+'\n\n'+'횟수 : '+str(times_p2),"제4회 BSS OPEN LAB - 숫자야구")
                elif ball==0:
                    print(''.join(choice_com),str(result[0])+'S')
                    easygui.msgbox(str(result[0])+'STRIKE'+'\n\n'+'횟수 : '+str(times_p2),"제4회 BSS OPEN LAB - 숫자야구")
                elif strike==0:
                    print(''.join(choice_com),str(result[1])+'B')
                    easygui.msgbox(str(result[1])+'BALL'+'\n\n'+'횟수 : '+str(times_p2),"제4회 BSS OPEN LAB - 숫자야구")
                else:
                    print(''.join(choice_com),str(result[0])+'S'+str(result[1])+'B')
                    easygui.msgbox(str(result[0])+'STRIKE'+' '+str(result[1])+'BALL'+'\n\n'+'횟수 : '+str(times_p2),"제4회 BSS OPEN LAB - 숫자야구")
            else:
                answer=easygui.multenterbox("플레이어 1의 숫자를 입력하세요.","제4회 BSS OPEN LAB - 숫자야구",['첫번째 자리','두번째 자리','세번째 자리','네번째 자리'],['','','',''])
                if choice_p1==answer:
                    correct+=1
                    easygui.msgbox("정답입니다!\n상품을 받아가세요!\n숫자를 찾은 횟수 : "+str(times_p2)+"\n"+"정답 시도 횟수 : "+str(correct),"제4회 BSS OPEN LAB - 숫자야구")
                    break
                else:
                    correct+=1
                    easygui.msgbox("틀렸습니다.\n다시 한 번 잘 생각해보세요.\n숫자를 찾은 횟수 : "+str(times_p2)+"\n"+"정답 시도 횟수 : "+str(correct),"제4회 BSS OPEN LAB - 숫자야구") 
                    print('오답')
        break
    else:
        break 





















































