
#def game():
    # per = requests.get('https://wikiway.com/dostoprimechatelnosti/top100/')
    # per = per.content
    # soup = BeautifulSoup(per, 'lxml')
    #
    # ent = Entry(window, bd=2)
    # ent.place(x=150, y=400, width=90)
    #
    # ans = ent.get()
    # d = str(ans)
    # print(ans)
N = int(input())
a = []
for i in range(N):
    b = int(input())
    a.append(b)
    for j in range(i+1):
        if b < a[i-j]:
            a.append(a[i-1])
            a[i] = b
            a.pop()

print(a)
