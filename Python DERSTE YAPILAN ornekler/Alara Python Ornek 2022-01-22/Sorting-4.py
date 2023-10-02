## Elemanın son harfine göre sıralamak istediğimiz bir dizimiz olsun.
strs = ['xc', 'zb', 'yd' ,'wa']

## Write a little function that takes a string, and returns its last letter.
## This will be the key function (takes in 1 value, returns 1 value).
def KendiYontemim(s):
    return s[-1]

## Now pass key=MyFn to sorted() to sort by the last letter:
print (sorted(strs, key=KendiYontemim))  ## ['wa', 'zb', 'xc', 'yd']
