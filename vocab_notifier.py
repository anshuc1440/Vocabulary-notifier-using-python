#import library
from plyer import notification
import time
if __name__ == "__main__":
        #specify parameters
        while True:
            title = "New Word for the day !!"
            #use the following function to read the file
            with open("C:\\Users\\hp\\Documents\\Projects\\Desktop_notifier\\Vocabulary.txt") as f:
                lines = f.readlines()
                #Iterate over these line to get one line at a tie
                for vocab in lines:
                    #Now create notifier
                    notification.notify(title= title, message= vocab.strip() , timeout= 10)
                    time.sleep(60*60) #it will notify each hour  