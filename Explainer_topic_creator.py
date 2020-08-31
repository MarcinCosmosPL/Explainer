from issue import *  # we require object issue, QuitButton and confirmation function
from issue_topics_listing import *  # we require objects path and file extension and a function to list the topics

print("HELLO! Here you can create new issues to be explained by the program")

running = True
while running:
    topics = topics_listing()
    while True:
        NewTopic = input("put in topic of the new issue or quit to quit:\n")
        if NewTopic == QuitButton:
            quit()
        elif NewTopic == '':
            print("You cannot add empty topic")
        if NewTopic in topics:
            print("this topic is already taken by some saved file")
            rewriting = conf("do you want to rewrite it? (yes/no)")
            if rewriting:
                break
            else:
                continue
        else:
            print("You have chosen: {}".format(NewTopic))
            confContinue = conf("Do you want to add this topic (yes/no)?")
            if confContinue:
                break

    print("Now time to get some explanations to the topic and create an issue object!!")
    newExplanations = []

    while True:
        explanation = input("give explanation or put {} to stop: \n".format(QuitButton))
        if explanation == QuitButton:
            break
        elif explanation == '':
            print("you cannot add empty explanation")
        else:
            confExplanation = conf("add this explanation? (yes/no)")
            if confExplanation:
                newExplanations.append(explanation)
                print("explanation added")
                confContinue = conf("Do you want to add more explanations? (yes/no)")
                if not confContinue:
                    break

    print("given topic: {}".format(NewTopic))
    print("number of given explanations: {}".format(len(newExplanations)))
    confContinue = conf("Do you want to continue? (yes/no)")
    if confContinue:
        print("creating file")
        try:
            if len(newExplanations) < 1:
                raise Exception("there is no expanations - file will not be created")
            else:
                with open(os.path.join(path, NewTopic+file_extension), 'w') as file:
                    for expl in newExplanations:
                        file.write(expl+'\n')
        except OSError as e:
            print("Error! Invalid topic name - Issue cannot be created (tip: do not use characters like \" in your topic name")
        except Exception as e:
            print("There is an error: {}".format(e))
        else:
            print("file created!")
        finally:
            running = conf("Want to create another one? (yes/no?)")

