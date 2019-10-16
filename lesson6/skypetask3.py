def howmuch(k, s):
    """Как сделать рекурсивно не придумал"""
    summ = 0
    for i in range(int('1' + '0' * (k - 1)), int('9' * k) + 1):
        if sum(list(map(int, str(i)))) == s:
            #print(i) - выводит все эти числа
            summ += 1
    return summ


print(howmuch(5, 10))


#Нашел решение на С-подобном языке, но оно не мое
# int f(int n, int k)
# {
# if (k==1) {
#   if (n>9 || n<0) return 0;
#   else return 1;
# }
# else {
#   for(i=s=0; i<10; i++) s += f(n-i, k-1);
# }
# return s;