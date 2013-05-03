import os, sys, thread, time
import localCGIServer

print "HIT ENTER TO SHUTDOWN THE SIMULATED SERVER\n"

if(sys.argv.__len__() > 1 and sys.argv[1].lower == "help"):
    quit();

thread.start_new_thread(localCGIServer.run_server, ());

print sys.argv

import webbrowser

if(sys.argv.__len__()==5):
    webbrowser.open('localhost:8080/' + sys.argv[1] + "?condition=" + sys.argv[2] + "&assignmentId=" + sys.argv[3] + "&workerId="+ sys.argv[4])
elif(sys.argv.__len__()==4):
    webbrowser.open('localhost:8080/' + sys.argv[1] + "?condition=" + sys.argv[2] + "&assignmentId=" + sys.argv[3] + "&workerId=RESEARCHTESTER1")
elif(sys.argv.__len__()==3):
    webbrowser.open('localhost:8080/' + sys.argv[1] + "?condition=" + sys.argv[2] + "&assignmentId=2&workerId=RESEARCHTESTER1")
elif(sys.argv.__len__() == 2):
    webbrowser.open('localhost:8080/' + sys.argv[1] + "?condition=1&assignmentId=2&workerId=RESEARCHTESTER1")
else:
    webbrowser.open('localhost:8080/readme.txt')

raw_input()