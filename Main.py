
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


x = int((3+2*glass_size-straw_pos)/2+0.5)  # find x by equation to stop the code when the last star and slash cross
for z in range(x):                         #figured out how many times to print glasses
    for a in range(straw_pos):
        for b in range(a):
            print(' ', end='')
        print('o')
    if z == 0:                             #it is the first glass before drinking
        for i in range(glass_size):
            for j in range(i):
                print(' ', end='')          #how many times to space before reverse slash
            print('\\', end='')
            for k in range(2 * glass_size - 2 * i):   #find how many times to print stars
                print('*', end='')
            print('/')
    else:
      for i in range(z):                 # start printing the part of the glass we drank
        for j1 in range(i):
          print(' ',end='')
        print('\\',end='')
        for b1 in range(straw_pos-1):    #number of spaces before the tip of the straw
          print(' ',end='')
        print('o',end='')
        for b2 in range(2*glass_size-straw_pos-2*i):  #number of spaces after the tip of the straw
          print(' ',end='')
        print('/')
      for i in range(z,glass_size):     #start printing the part of the glass we haven't drunk yet
        for j2 in range(i):
          print(' ',end='')
        print('\\',end='')
        for k2 in range(2*glass_size-2*i):   #to print the rest of the cocktail
          print('*',end='')
        print('/')
    for l1 in range(glass_size + 1):     # draw the rest of the cocktail glass
      if l1 == 0:
        for m2 in range(glass_size):
            print(' ', end='')
        print('--')
      else:
        for m2 in range(glass_size):
            print(' ', end='')
        print('||')

















# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


