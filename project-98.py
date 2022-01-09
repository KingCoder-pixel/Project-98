def myFunction():
    count = 0
    data_a = open("C:/Users/haris/OneDrive/Desktop/Hari/WhiteHat/Project/project 98/file1.txt")
    for lines in data_a: 
        myWords = lines.split()
        count=count+len(myWords)
    print(myWords)
    print(count)

    data_b = open("C:/Users/haris/OneDrive/Desktop/Hari/WhiteHat/Project/project 98/file2.txt")
    for lines in data_b: 
        myWords = lines.split()
        count=count+len(myWords)
    print(myWords)
    print(count)

myFunction()