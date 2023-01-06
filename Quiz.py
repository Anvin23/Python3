marks = 0
questions = [["C++ was developed by  " , "Thomas Kushz" , "John Kemney" , "Bjarne Stroutstrup" , "James Gosling",3] , 

["Python was developed by " , "Wick van Rossum" , "Rasmus Lerdorf" , "Niene Stom" , "Guido van Rossum" , 4] , 

["Which of the following is used to define a block of code in Python language?" , "Indentation" , "Key" , "Brackets" , "All of the above",1] , 

["What does pip stands for in python ? " , "Pip Installs Python" , "Pip Installs Packages" , "Preffered Installer Program" , "None" , 3] , 

["Who invented java programming ?" , "Guido van Rossum" , "James Gosling" , "Dennis Ritchie" , "Bjarne Stroustrup" , 2] , 

["Which one of the following is not a feature of java ?" , "Object-oriented" , "Portable" , "Dynamic and Extensible" , "Use of pointers" , 4] , 

["Which of the following user-defined header file extension used in c++?" , "hf" , "h" , "cpp" , "hgg" , 2]

]

for i in range (0 , len(questions)):
    current_question = questions[i]
    print(current_question[0])
    print(f"1. {current_question[1]}          2. {current_question[2]}")
    print(f"3. {current_question[3]}          4. {current_question[4]}")
    choice = int(input("Enter your answer : "))

    if(choice == current_question[-1]):
        marks+=1


print(f"Your final score is {marks}/6")