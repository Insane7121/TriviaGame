print ('Hello,welcome to QUIZ GAME!')

ans = input('Are You Ready To PLay? (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1.what is my name?')
    if ans == 'shubham' :
        score += 1
        print('Correct')
    else :
        print('incorrect')


    ans = input('2.where do i stay?')
    if ans == 'thane' :
        score += 1
        print('Correct')
    else :
        print('incorrect')

    ans = input('3.do i own a pet?')
    if ans == 'yes' or ans.lower() == 'no':
        score += 1
        print('Correct')
    else :
        print('incorrect')


print ('Thankyou For Playing,You Got', score, "questions correct.")
mark = (score/total_q) * 100

print("mark: ", str (mark) + '%')
print('Congratulations!!! GOODBYE!!!')
