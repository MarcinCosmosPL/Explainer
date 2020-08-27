QuitButton = "quit"

def conf(question):
    while True: ##Ask the question and return True or False. Accepts only yes/no answer
        print(question)
        ans = input()
        if ans.lower() in ["yes", "no", QuitButton]:
            break
        else:
            print("Sorry! Yes/no answer required to continue")
    if ans.lower() == "yes":
        return True
    elif ans.lower() == QuitButton:
        quit()
    else:
        return False

class issue:
    '''An objects of this class has a topic and several possible explanations and method giving explanations in loop as long as the user does not confirm understanding
    explanations are sorted from shortest to longest
    '''

    def __init__(self, topic, explanationsList):
        if type(topic) is str:
            if topic.lower() == QuitButton:
                raise Exception("topic cannot be named quit")
            else:
                self.topic = topic
        else:
            raise Exception("topic must be a single string of characters")
        if type(explanationsList) is list:
            if len(explanationsList) > 0:
                explanationsList.sort(key=len)
                self.explanations = explanationsList
            else:
                raise Exception("list of explanations cannot be empty")
        else:
            raise Exception("explanations must be given in list")

    def explaining(self):
        no=1
        for i in self.explanations:
            print("\n Explaining the topic: {}\nExplanation numer: {} of {}".format(self.topic.upper(), no, len(self.explanations)))
            print(i)
            no+=1
            confirmation = conf('Did you understand? (put yes or no and press enter) \n')
            if confirmation:
                print("\nGood for YOU!!!!!\n")
                break
        else:
            print("\nSorry! No more explanations!\n")
