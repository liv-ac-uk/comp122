
# Version Control with git

Let's get used to storing code in a git repository.
To get you started, what we will do here is configuring git locally on this computer, creating a new empty repository, and adding something to it.

## Installation

If you're on linux of OS X, it is very likely that git is already pre-installed.
To check if it is, just open a terminal and type `git`. 
Otherwise it is best to install it via your package manager (e.g. `sudo apt install git` on ubuntu, homebrew for OS X) You can also download the binaries from <https://git-scm.com/download>.

---

Open a terminal and type 

```
git
```
You should get some output that explains how to use the git command.
You can get help on any subcommand, say `add` by typing `git help add`. Also check out the manpage: `man git`.

{% next %}


## Local set-up

Let's introduce ourselves, using the UoL email address.

```
git config --global user.name "John Doe"
git config --global user.email XXXXX@liverpool.ac.uk
```

You only need to do this once on a computer. Git will remember these values and from now on use them to tag any changes you make using git.

We can also name our preference for a text editor, although that's not strictly necessary:

```
git config --global core.editor vim
```

Or perhaps, if you're on Windows..

```
git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
```

{% next %}


## Creating a repository

Let's initialize a new repository. We can do that by running `git init` in any directory that we want to turn into the main directory of our repository.

```
mkdir demo
cd demo
git init
Initialized empty Git repository in /home/patrick/demo/.git/
```

You now have have an empty and boring repository. Check its status like this
```
git status
```


{% next %}

## Adding stuff

Copy something into this directory and `git add` it to the repository (telling it to "track" this file henceforth).
Take for example your code from the last lab, and copy it into a subdirectory `lastlab`. Then,

```
git add lastlab/Bird.java
```

This will "stage" the files (tell git to include them next time you write to its database).
It does not actually save anything yet and only tells git that you want to also add this file in your next commit.
To make such a commit and save the new file in its current form, you can `git commit` it like this:

```
git commit -m "Add the Bird class"
```

You have just made your first commit. This saved a snapshot of `Bird.java` for prosperity.
Of course you could have committed more than one file at a time.

If you omit the parameter `-m` and its argument, git will open your editor to prompt you for a commit message.
This message allows you to keep a human-readable record of the changes you've made.
You can see all your commits using `git log`.

Add a few more files to your repository.

{% next %}

## Making changes to files and reverting them

Make some changes to one of your files. You can now either

- commit them to add another snapshot for later:
  ```
  git commit -a -m "my changes"
  ```
- revert to the previous snapshot like this:
  ```
  git checkout FILENAME
  ```
  which will overwrite your file with its content at the time you last committed.


You can also resume a file to a particular snapshot from the past.
For example, let's say our commit history looks like this.

```
git log
commit a7ae914cb18db8d43a1aa05dd70c043135ab8f47 (HEAD -> master)
Author: Patrick Totzke <totzke@liverpool.ac.uk>
Date:   Wed Feb 12 13:35:42 2020 +0000

    removed javadoc header

commit 6a1107fb3027bda9c47d622464e2b01a083a1ac9
Author: Patrick Totzke <totzke@liverpool.ac.uk>
Date:   Wed Feb 12 13:30:10 2020 +0000

    add more stuff

commit bc8d4ae00a0efee694edf2d48ff0fff9a20fa56e
Author: Patrick Totzke <totzke@liverpool.ac.uk>
Date:   Wed Feb 12 13:27:23 2020 +0000

    Add the Bird class
```

We can go way back to the oldest version like this

```
git checkout bc8d4ae00a0efee694edf2d48ff0fff9a20fa56e lab-3/Bird.java 
```

You don't actually need to type the full identifier of the commit, as I have. A unique prefix suffices.
Afterwards you will see that the content of `lastlab/Bird.java` was reverted to its initial state.

There are many cool features of git to play with, and which will make your life easier.
There is excellent documentation on git for all levels available online.
I highly recommend the [freely available textbook ProGit](https://git-scm.com/book/en/v2).
