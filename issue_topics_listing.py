import os #working with the files

path = "./savedIssues" #folder with data files for issues objects
file_extension = '.txt' #and their extension

def topics_listing(): #A FUNCTION THAT GIVES A LIST OF TOPICS FROM THE FOLDER
    topics = []
    for dir_name, subdirs, filenames in os.walk(path): #loop to fill the list of topics
        for filename in filenames:
            if filename.endswith(file_extension):
                topics.append(filename[:-len(file_extension)])

    topics.sort(key=str.lower) #sort and show the topics

    return topics