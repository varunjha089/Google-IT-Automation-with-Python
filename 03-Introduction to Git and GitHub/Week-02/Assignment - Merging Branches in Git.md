# Merging Branches in Git

Nothing new from previous one.


### Add a new feature

In this section, we'll be modifying the repository to add a new feature, without affecting the current iteration. This 
new feature is designed to improve the food count (from the file food_count.py) output. So, create a branch named 
improve-output using the following command:

    git branch improve-output

Move to the `improve-output` branch from the master branch.

    git checkout improve-output

Here, you can modify the script file without disturbing the existing code. Once modified and tested, you can update the 
master branch with a working code.

Now, open `food_count.py` in the nano editor using the following command:

    vim food_count.py    

Add the line below before **printing for loop** in the `food_count.py` script:

    print("Favourite foods, from most popular to least popular")

Save the file by pressing *Ctrl-o*, the Enter key, and *Ctrl-x*. Then run the script `food_count.py` again to see the 
output:

    ./food_count.py

After successful execution add the file to tracking

### Fix the script

In this section, we'll fix the script food_question.py, which displayed an error when executing it. You can run the 
file again to view the error.

    ./food_question.py

This script gives us the error: **"NameError: name 'item' is not defined"** but your colleague says that the file was 
running fine before the most recent commit they did.

Type:

    git log

and using the log message revert it. The command is as follows:

    git revert [commit-ID]

***NOTE:-*** **Then continue by clicking Ctrl-o, the Enter key, and Ctrl-x.**

### Merge operation

Before merging the branch `improve-output`, switch to the master branch from the current branch `improve-output` branch 
using the command below:

    git checkout master

Merge the branch improve-output into the master branch.

    git merge improve-output

### Congratulations!

In this lab, you successfully created a branch from the master branch to add a new feature. You also rolled back a 
commit to where the script worked fine, and then merged it to the master branch. This will help as you work with 
colleagues who are simultaneously on the same repository.