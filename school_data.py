# school_data.py
# Hareem Khan, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt
import math

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """

        print("School Name: {0}, School Code: {1}".format(self.name, self.code))

# Import data here
# Hint: Create a dictionary for all school names and codes
school_names_dict = {'Centennial High School': '1224', 'Robert Thirsk School': '1697',                                                                                      #dictionary that has all of the school names and corresponding school codes
 'Louise Dean School': '9626', 'Queen Elizabeth High School': '9806', 
 'Forest Lawn High School': '9813', 'Crescent Heights High School': '9815',
 'Western Canada High School': '9816', 'Central Memorial High School': '9823',
 'James Fowler High School': '9825', 'Ernest Manning High School': '9826',
 'William Aberhart High School': '9829', 'National Sport School': '9830',
 'Henry Wise Wood High School': '9836', 'Bowness High School': '9847',
 'Lord Beaverbrook High School': '9850', 'Jack James High School': '9856',
 'Sir Winston Churchill High School': '9857', 'Dr. E. P. Scarlett High School': '9858',
 'John G Diefenbaker High School': '9860', 'Lester B. Pearson High School': '9865'}

# Hint: Create a list of school codes to help with index look-up in arrays
school_codes_list = list(school_names_dict.values())                                                                                                                        #list with the school codes, coming from the values of the school name/code dictionary
school_names_list = list(school_names_dict.keys())                                                                                                                          #list with the school names, coming from the keys of the school name/code dictionary 

# Add your code within the main function. A docstring is not required for this function.
def main():                                                                                                                                                                 #this function houses all of the main code, including the printing of the arrays, user input/validation, printing of the school name/code using the school class, printing the mean students, and also the plots of the data.
    print("ENDG 233 School Enrollment Statistics\n")

    # Print array data here
    school_data2020 = np.genfromtxt('SchoolData_2020-2021.csv', delimiter = ',', skip_header= True)                                                                         #here, the array for grades 10, 11, and 12 in 2020-2021 is being printed using the 2020-2021 csv file
    print('Array data for 2020 - 2021:\n', school_data2020)

    school_data2019 = np.genfromtxt('SchoolData_2019-2020.csv', delimiter = ',', skip_header= True)                                                                         #here, the array for grades 10, 11, and 12 in 2019-2020 is being printed using the 2019-2020 csv file 
    print('Array data for 2019 - 2020:\n', school_data2019)

    school_data2018 = np.genfromtxt('SchoolData_2018-2019.csv', delimiter = ',', skip_header= True)                                                                         #here, the array for grades 10, 11, and 12 in 2018-2019 is being printed using the 2018-2019 csv file
    print('Array data for 2018 - 2019:\n', school_data2018) 
    
    # Add request for user input here
    
    user_input = input('Please enter the high school name or code: ')                                                                                                       #the user is asked for a school name or code

    while user_input not in school_names_dict.keys() and user_input not in school_codes_list:                                                                               #while loop will run until a valid school name or code is inputted by the user
        print('You must enter a valid school name or code.')
        user_input = input('Please enter the high school name or code: ')

    # Print school name and code using the given class

    if user_input in school_names_dict.keys():                                                                                                                              #if the input is a valid school name, the school class will be called and the school name and code will be printed out using the input and school names dictionary
        
        user_school = School(user_input, int(school_names_dict[user_input]))

    else:
        school_name = school_names_list[school_codes_list.index(user_input)]                                                                                                #if the input is a valid school code, the school class will be called and the school name and code will be printed out using the index of the school codes list and the input to find the school name
        user_school = School(school_name, int(user_input))
   
    print("\n***Requested School Statistics***\n")
    
    user_school.print_all_stats()                                                                                                                                           #the print all stats function will be called depending on the input to print out the school name and code for the user

    #print mean students per grade    

    if user_input in school_names_dict.keys():                                                                                                                              #if the input is a valid school name, the mean amount of students is printed, and the enrollment by year/grade is plotted
        
        school_code_index = school_names_list.index(user_input)                                                                                                             #the index of the school names list with the user input, gives the row number when searching the arrays for the mean values of students

        mean_value_gr10 = math.floor(int((school_data2018[school_code_index, 1] + school_data2019[school_code_index, 1] + school_data2020[school_code_index, 1])/3))        #the mean value for grade 10 students is calculated by adding together the values in the second column and given row number of the arrays from each year, then dividing this by 3 (rounding down)
        print(f'Mean enrollment for Grade 10: {mean_value_gr10}')                                                                                                           #the mean value for students in grade 10 for the past 3 years is printed

        mean_value_gr11 = math.floor(int((school_data2018[school_code_index, 2] + school_data2019[school_code_index, 2] + school_data2020[school_code_index, 2])/3))        #the mean value for grade 11 students is calculated by adding together the values in the third column and given row number of the arrays from each year, then dividing this by 3 (rounding down)
        print(f'Mean enrollment for Grade 11: {mean_value_gr11}')                                                                                                           #the mean value for students in grade 11 for the past 3 years is printed

        mean_value_gr12 = math.floor(int((school_data2018[school_code_index, 3] + school_data2019[school_code_index, 3] + school_data2020[school_code_index, 3])/3))        #the mean value for grade 10 students is calculated by adding together the values in the forth column and given row number of the arrays from each year, then dividing this by 3 (rounding down)
        print(f'Mean enrollment for Grade 12: {mean_value_gr12}')                                                                                                           #the mean value for students in grade 12 for the past 3 years is printed

        total_grads = int(school_data2018[school_code_index, 3] + school_data2019[school_code_index, 3] + school_data2020[school_code_index, 3])                            #the total number of graduates in the school over the past 3 years is calculated by adding together the number of grade 12s from each year
        print(f'Total number of students who graduated in the past three years: {total_grads}')                                                                             #the total graduates is printed

        # Add data processing and plotting here
        x_axis = [10,11,12]                                                                                                                                                 #the enrollment by year is plotted here. the x axis shows grades 10, 11, and 12
        plt.scatter(x_axis, [school_data2018[school_code_index,1], school_data2018[school_code_index,2], school_data2018[school_code_index,3]])                             #the scatter plot for 2019 is here, showing the students in each grade for that year
        plt.scatter(x_axis, [school_data2019[school_code_index,1], school_data2019[school_code_index,2], school_data2019[school_code_index,3]])                             #the scatter plot for 2020 is here, showing the students in each grade for that year
        plt.scatter(x_axis, [school_data2020[school_code_index,1], school_data2020[school_code_index,2], school_data2020[school_code_index,3]])                             #the scatter plot for 2021 is here, showing the students in each grade for that year
        plt.title('Grade Enrollment by Year')                                                                                                                               #the title of the plot is "Grade Enrollment by Year"
        plt.xlabel("Grade Level")                                                                                                                                           #the label for the x axis of the plot is "Grade Level"
        plt.ylabel("Number of Students")                                                                                                                                    #the label for the y axis of the plot is "Number of Students"
        plt.legend(('2019 Enrollment','2020 Enrollment','2021 Enrollment'))                                                                                                 #the legend helps the user decipher between the different plots for 2019, 2020 and 2021 enrollment
        plt.xticks(np.arange(10,13,1))                                                                                                                                      #this ensures the x axis shows only the values 10, 11, and 12, (with a jump of one) and no extra demimal values in between
        plt.show()                                                                                                                                                          #the plot with the 3 scatter graphs is shown to the user

        #bonus matplotlib plot
        x_baxis = [2019,2020,2021]                                                                                                                                          #the bonus of enrollment by grade is plotted here. the x axis shows the years 2019, 2020, and 2021
        plt.subplot(3,1,1)                                                                                                                                                  #the position of this subplot is in the first spot of the 3 rows (1 column)
        plt.title('Enrollment by Grade')                                                                                                                                    #the title of these plots is "Enrollment by Grade"
        plt.ylabel('Number Students')                                                                                                                                       #the label for the y axis of the subplots is "Number Students"
        plt.plot(x_baxis, [school_data2018[school_code_index,1], school_data2019[school_code_index,1], school_data2020[school_code_index, 1]], 'm--', label = "Grade 10")   #this subplot shows the average students in grade 10 over 2019, 2020, and 2021. the line is a magenta dashed line labeled "Grade 10"
        plt.xticks(np.arange(2019,2022,1))                                                                                                                                  #this ensures the x axis of this subplot shows only the values 2019, 2020, and 2021, (with a jump of 1) and no extra decimal values in between
        plt.legend(shadow=True, loc="upper right")                                                                                                                          #the legend that is labeled "Grade 10" is in the upper right corner of the subplot

        plt.subplot(3,1,2)                                                                                                                                                  #the position of this subplot is in the second spot of the 3 rows (1 column)
        plt.ylabel('Number Students')                                                                                                                                       #the label for the y axis of the subplots is "Number Students"
        plt.plot(x_baxis, [school_data2018[school_code_index,2], school_data2019[school_code_index,2], school_data2020[school_code_index, 2]],'c--', label = "Grade 11")    #this subplot shows the average students in grade 11 over 2019, 2020, and 2021. the line is a cyan dashed line labeled "Grade 11"
        plt.xticks(np.arange(2019,2022,1))                                                                                                                                  #this ensures the x axis of this subplot shows only the values 2019, 2020, and 2021, (with a jump of 1) and no extra decimal values in between
        plt.legend(shadow=True, loc="upper right")                                                                                                                          #the legend that is labeled "Grade 11" is in the upper right corner of the subplot

        plt.subplot(3,1,3)                                                                                                                                                  #the position of this subplot is in the third spot of the 3 rows (1 column)  
        plt.ylabel('Number Students')                                                                                                                                       #the label for the y axis of the subplots is "Number Students"
        plt.xlabel('Enrollment Year')                                                                                                                                       #the label for the x axis of the plot is "Enrollment Year"
        plt.plot(x_baxis, [school_data2018[school_code_index,3], school_data2019[school_code_index,3], school_data2020[school_code_index, 3]],'g--', label = "Grade 12")    #this subplot shows the average students in grade 12 over 2019, 2020, and 2021. the line is a green dashed line labeled "Grade 12"
        plt.xticks(np.arange(2019,2022,1))                                                                                                                                  #this ensures the x axis of this subplot shows only the values 2019, 2020, and 2021, (with a jump of 1) and no extra decimal values in between
        plt.legend(shadow=True, loc="upper right")                                                                                                                          #the legend that is labeled "Grade 12" is in the upper right corner of the subplot
        plt.show()                                                                                                                                                          #all three subplots are shown to the user

    elif user_input in school_names_dict.values():                                                                                                                          #if the input is a valid school code, the mean amount of students, and the enrollment by year/grade is plotted
        
        school_code_index = school_codes_list.index(user_input)                                                                                                             #the index of the school codes list with the user input, gives the row number when searching the arrays for the mean values of students

        mean_value_gr10 = math.floor(int((school_data2018[school_code_index, 1] + school_data2019[school_code_index, 1] + school_data2020[school_code_index, 1])/3))        #the mean value for grade 10 students is calculated by adding together the values in the second column and given row number of the arrays from each year, then dividing this by 3 (rounding down)
        print(f'Mean enrollment for Grade 10: {mean_value_gr10}')                                                                                                           #the mean value for students in grade 10 for the past 3 years is printed

        mean_value_gr11 = math.floor(int((school_data2018[school_code_index, 2] + school_data2019[school_code_index, 2] + school_data2020[school_code_index, 2])/3))        #the mean value for grade 11 students is calculated by adding together the values in the third column and given row number of the arrays from each year, then dividing this by 3 (rounding down)
        print(f'Mean enrollment for Grade 11: {mean_value_gr11}')                                                                                                           #the mean value for students in grade 11 for the past 3 years is printed

        mean_value_gr12 = math.floor(int((school_data2018[school_code_index, 3] + school_data2019[school_code_index, 3] + school_data2020[school_code_index, 3])/3))        #the mean value for grade 12 students is calculated by adding together the values in the forth column and given row number of the arrays from each year, then dividing this by 3 (rounding down)
        print(f'Mean enrollment for Grade 12: {mean_value_gr12}')                                                                                                           #the mean value for students in grade 12 in the past 3 years is printed

        total_grads = int(school_data2018[school_code_index, 3] + school_data2019[school_code_index, 3] + school_data2020[school_code_index, 3])                            #the total number of graduates in the school over the past 3 years is calculated by adding together the number of grade 12s from each year
        print(f'Total number of students who graduated in the past three years: {total_grads}')                                                                             #the total graduates is printed

        # Add data processing and plotting here
        x_axis = [10,11,12]                                                                                                                                                 #the enrollment by year is plotted here. the x axis shows grades 10, 11, and 12
        plt.scatter(x_axis, [school_data2018[school_code_index,1], school_data2018[school_code_index,2], school_data2018[school_code_index,3]])                             #the scatter plot for 2019 is here, showing the students in each grade for that year
        plt.scatter(x_axis, [school_data2019[school_code_index,1], school_data2019[school_code_index,2], school_data2019[school_code_index,3]])                             #the scatter plot for 2020 is here, showing the students in each grade for that year
        plt.scatter(x_axis, [school_data2020[school_code_index,1], school_data2020[school_code_index,2], school_data2020[school_code_index,3]])                             #the scatter plot for 2021 is here, showing the students in each grade for that year
        plt.title('Grade Enrollment by Year')                                                                                                                               #the title of the plot is "Grade Enrollment by Year"
        plt.xlabel("Grade Level")                                                                                                                                           #the label for the x axis of the plot is "Grade Level"
        plt.ylabel("Number of Students")                                                                                                                                    #the label for the y axis of the plot is "Number of Students"
        plt.legend(('2019 Enrollment','2020 Enrollment','2021 Enrollment'))                                                                                                 #the legend helps the user decipher between the different plots for 2019, 2020 and 2021 enrollment
        plt.xticks(np.arange(10,13,1))                                                                                                                                      #this ensures the x axis shows only the values 10, 11, and 12, (with a jump of one) and no extra demimal values in between
        plt.show()                                                                                                                                                          #the plot with the 3 scatter graphs is shown to the user

        #bonus matplotlib plot
        x_baxis = [2019,2020,2021]                                                                                                                                          #the bonus of enrollment by grade is plotted here. the x axis shows the years 
        plt.subplot(3,1,1)                                                                                                                                                  #the position of this subplot is in the first spot of the 3 rows (1 column)
        plt.title('Enrollment by Grade')                                                                                                                                    #the title of these plots is "Enrollment by Grade"
        plt.ylabel('Number Students')                                                                                                                                       #the label for the y axis of the subplots is "Number Students"
        plt.plot(x_baxis, [school_data2018[school_code_index,1], school_data2019[school_code_index,1], school_data2020[school_code_index, 1]], 'm--', label = "Grade 10")   #this subplot shows the average students in grade 10 over 2019, 2020, and 2021. the line is a magenta dashed line labeled "Grade 10"
        plt.xticks(np.arange(2019,2022,1))                                                                                                                                  #this ensures the x axis of this subplot shows only the values 2019, 2020, and 2021, (with a jump of 1) and no extra decimal values in between
        plt.legend(shadow=True, loc="upper right")                                                                                                                          #the legend that is labeled "Grade 10" is in the upper right corner of the subplot
        
        plt.subplot(3,1,2)                                                                                                                                                  #the position of this subplot is in the second spot of the 3 rows (1 column)
        plt.ylabel('Number Students')                                                                                                                                       #the label for the y axis of the subplots is "Number Students"
        plt.plot(x_baxis, [school_data2018[school_code_index,2], school_data2019[school_code_index,2], school_data2020[school_code_index, 2]],'c--', label = "Grade 11")    #this subplot shows the average students in grade 11 over 2019, 2020, and 2021. the line is a cyan dashed line labeled "Grade 11"
        plt.xticks(np.arange(2019,2022,1))                                                                                                                                  #this ensures the x axis of this subplot shows only the values 2019, 2020, and 2021, (with a jump of 1) and no extra decimal values in between
        plt.legend(shadow=True, loc="upper right")                                                                                                                          #the legend that is labeled "Grade 11" is in the upper right corner of the subplot

        plt.subplot(3,1,3)                                                                                                                                                  #the position of this subplot is in the third spot of the 3 rows (1 column)
        plt.ylabel('Number Students')                                                                                                                                       #the label for the y axis of the subplots is "Number Students"
        plt.xlabel('Enrollment Year')                                                                                                                                       #the label for the x axis of the plot is "Enrollment Year"
        plt.plot(x_baxis, [school_data2018[school_code_index,3], school_data2019[school_code_index,3], school_data2020[school_code_index, 3]],'g--', label = "Grade 12")    #this subplot shows the average students in grade 12 over 2019, 2020, and 2021. the line is a green dashed line labeled "Grade 10"
        plt.xticks(np.arange(2019,2022,1))                                                                                                                                  #this ensures the x axis of this subplot shows only the values 2019, 2020, and 2021, (with a jump of 1) and no extra decimal values in between
        plt.legend(shadow=True, loc="upper right")                                                                                                                          #the legend that is labeled "Grade 12" is in the upper right corner of the subplot
        plt.show()                                                                                                                                                          #all three subplots are shown to the user
  
# Do not modify the code below
if __name__ == '__main__':                                                                                                                                                  
    main()                                                                                                                                                                  #the main function is called to begin the program