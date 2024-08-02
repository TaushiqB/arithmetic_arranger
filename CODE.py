def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        return "Error: Too many problems."
    top = ''
    middle = ''
    bottom = ''
    ans = ''
    for i in problems:
        i = i.split(" ")
        #print(i[0])
        c = 0  ## Bigger Number
        b = 0  ## Smaller Number
        d = 0  ## Answer Number
        h = 0

        if not i[0].isdigit() or not i[2].isdigit():
            return "Error: Numbers must only contain digits."
        if i[1] == '+':
            a = str(int(i[0])+int(i[2]))
        elif i[1] == '-':
            a = str(int(i[0])-int(i[2]))
        else:
            return "Error: Operator must be '+' or '-'."
        
        if len(i[0])>4 or len(i[2])>4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(i[0]), len(i[2]))+2
        top += i[0].rjust(width)
        middle+= i[1]+i[2].rjust(width-1)
        bottom+= '-'*width
        ans+=a.rjust(width)

        top+="    "
        middle+="    "
        bottom+="    "
        ans+="    "

    if show_answers == True:
        final = '\n'.join((top.rstrip(),middle.rstrip(),bottom.rstrip(),ans.rstrip()))
        return final
    else:
        final = '\n'.join((top.rstrip(),middle.rstrip(),bottom.rstrip()))
        return final

    # return problems


print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
