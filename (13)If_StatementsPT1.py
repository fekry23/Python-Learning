
is_male = True
is_tall = True

if is_male or is_tall:                      #or is equal to ||
    print("You are a male or tall or both")
else:
    print("You are not a male nor tall")


if is_male and is_tall:                      #and is equal to &&
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:              #Not : jika true, maka akan jadi false.
    print("You are a male but are tall")    #Not : jika false, maka akan jadi true.
else:
    print("You are not a male and not tall")