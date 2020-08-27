from issue import * #we require object issue and QuitButton
from issue_topics_listing import * #we require objects path and file extension and a function to list the topics
#import os #imported in issue_topics_listing script

print("\n", 10*"-", "WELCOME TO EXPLAINER", 10*"-") #greetings
print("loading the topics... \n")

#at the begining we will show available topics of the issues
topics = topics_listing() #we will refer to that list later on
for topic in topics:
    print(topic)

print(20*"#")

while True: #main loop of user's decisions
    selection = input("put in Your topic and press enter, type quit if You want to finish\n")
    if selection.lower() == QuitButton: #condition for ending the loop
        break
    elif selection not in topics:
        print("error! Issue not found in the topics list")
    else: #creating the object based on user's selection and executing its main method
        loadedExplanations = [] #list that will have the explanations of the topic
        with open(os.path.join(path, selection+file_extension)) as file:
            for line in file:
                loadedExplanations.append(line)
        selectedIssue = issue(selection, loadedExplanations)
        selectedIssue.explaining()

