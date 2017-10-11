![When Lizard has a better commit history then you](https://i.imgur.com/4KvHoEl.jpg)
*When a lizard has a better commit history then you you should Use Github Commit Steak Reminder.*

# Github Commit Streak Reminder

I can find myself getting into weird commit habbits. My main excuses are that i work alone on most of my projects but that's not a valid excuse to not commit your work and keep your projects up to date.
Thats why i made **Streak Reminder** it reminds you to commit to github everyday.

It helps you to maintain a neat green bar on github but also compels you to keep maintaining stuff on github.com.


## I want to use Github Streak reminder as well!
That's not to hard. First make sure you run Linux since the commit reminder uses libnotify notifications.

just open up the `gh_reminder.py` file and replace every instance of my username `DrNotThatEvil` with your username.

(I know this is a crude method but i mainly intend this script to be run by myself that's why it's not fancy or anything.)

After this you need to install the required modules from the `requirements.txt` i recommend doing this in a virtual enviroment.

Next you need to autostart the python script somehow. Since i use `i3` window manager i can just add the script to my `i3` configuration for autostarting.

Your done.

