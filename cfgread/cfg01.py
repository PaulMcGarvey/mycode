#!/usr/bin/env python3

""" """

def main():
    # create a file object in 'read' mode
    config_file = open('vlanconfig.cfg', 'r')

    # display file to the screen - .read() method
    print(config_file.read())

    # close the config file
    config_file.close()

    # re-create file object to explore new method
    config_file = open('vlanconfig.cfg', 'r')

    # make a list of file lines - .readlines()
    config_list = config_file.readlines()
    print(config_list)

    # iterate through config_list
    for x in config_list:
        print(x.strip())

    # close the file
    config_file.close()










main()
