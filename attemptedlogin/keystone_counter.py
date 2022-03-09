#! /usr/bin/python3

""" """

def main():

    # counter for failed logins
    loginfail = 0

    # open the file for reading
    keystone_file = open('/home/student/mycode/attemptedlogin/keystone.common.wsgi', 'r')

    # turn the file into a list of lines in memory
    keystone_file_lines = keystone_file.readlines()

    # loop through all the lines looking for lines that match our pattern
    for line in keystone_file_lines:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # adds 1 to the failed login counter

    print("The number of failed logins is ", loginfail)

main()
