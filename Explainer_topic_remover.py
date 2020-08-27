from issue import * #we require object issue and QuitButton
from issue_topics_listing import * #we require objects path and file extension and a function to list the topics

print("HELLO! Here you can remove some of the stored issues by selecting the topic from the list")

print("loading the topics... \n")
topics = topics_listing()
for topic in topics:
    print(topic)

print(20*"#")

while True: #loop that allows to choose the issue saved in files to be removed by typing the right topic
    print("Do you want to remove any of the topics above?")
    print("put the name of the topic here and press enter or type {} to quit".format(QuitButton))
    answer = input()
    if answer == QuitButton.lower():
        break
    elif answer in topics:
        print("removing the file: {}".format(answer+file_extension))
        topics.remove(answer)
        os.remove(os.path.join(path, answer+file_extension))
        print("removing complete")
    else:
        print("error! Issue not found in the topics list")



