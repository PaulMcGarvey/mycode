#!/usr/bin/env python3
"""Trying to format according to best practices """

def main():

    # Import the shell utilities
    import shutil

    # Import the OS module
    import os

    # set the directory to /home/student/mycode/
    os.chdir("/home/student/mycode/")

    # use shutil to make a copy of the .txt file in the same location
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # use shutil to copy the entire 5g research folder - including all child items
    shutil.copytree("5g_research/", "5g_research_backup/")

    main()


