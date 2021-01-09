#Importing the regex library
import re

#enter the file address which has raw data
f = open("C:/Users/Admin/Desktop/Python Projects/email_addresses.txt", "r")

#this variable hold the raw data from your raw data file 
email = f.read()

#email = "jfdk jkfdkj anwar.shaikh@gmail.com apple_u@gmail.com Apple-pie@gmail.net "

#Give a parameter to search for email address. In this example we have seperated every word with plus sign. 
#So we are going to search for a word which has ".", "-", "_" followed by @ sign where in we again have words which could have all these three signs.
#Rest of the sign will be ignored. 
scrape = re.compile("[a-zA-Z0-9\.\-\_]+\@+[a-zA-Z0-9\.\-\_]+")

#This will find all the email address with above parameters 
result_scrape = scrape.findall(email) 

#This will pring the list of email addresses
print(result_scrape)

#This will convert the list to normail string seperated by ",".
def liststostring(s):
    #initialize empty string
    string1=", "

    #Join the list to string by .join method.
    return(string1.join(s))


s = result_scrape
emails_string = liststostring(s)

#This will print the email address seperated by ","
print(emails_string)

#Below commands will save the email address in the file
f = open("C:/Users/Admin/Desktop/Python Projects/emails_result.csv", "w")
f.write(emails_string)
f.close()
