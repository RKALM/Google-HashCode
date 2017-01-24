import fileinput

checkoftests=0
N=0
unregisteredcase=0
tendigits=list()
number_string=0
number_string2=0
f = open('output.txt','w')




for line in fileinput.input("happyinput.in"):
    if checkoftests == 0:
      checkoftests+=1
      print(line)
    else:
      N=line
      number_string = str(N)
      i=0
      tendigits = []
      if int(N) !=0:
          while len(tendigits) < 10:
            for number in str(number_string):
              if number not in tendigits and str(number).isdigit():
                tendigits.append(number)
                number_string2 = number_string
            i+=1
            number_string = int(N)*i

      else:
        print("Case #", str(unregisteredcase + 1), ": INSOMNIA ", sep="")
        print("Case #", str(unregisteredcase + 1), ": INSOMNIA ", sep="", end='\n', file=f)

        unregisteredcase+=1
    if checkoftests != 0 and int(N) !=0:
        unregisteredcase+=1
        print("Case #", str(unregisteredcase), ": ", number_string2, sep="")
        print("Case #", str(unregisteredcase), ": ", number_string2, " ",sep="", end='\n', file=f)




f.close()
print("That's all filks!")

