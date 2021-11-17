# Class Raven

### Rough Timeline

Weeks 1, 2, 3, 4, 5: Python

**Weeks 6, 7, 8, 9: HTML/CSS/Flask**

Weeks 10, 11: Javascript

Weeks 12, 13, 14, 15: Django

Weeks 16, 17, 18: Capstone project

### Scheduled Holidays (no class)
- **Nov 11** - Veterans Day
- **Nov 25 - 26** - Thanksgiving
- **Dec 24** - Christmas Eve
- **Dec 31** - New Years Eve

### Assigned Labs:

<details>
  <summary>Python</summary>
  <ul>
    <li>Lab 02 - Make Change</li>
    <li>Lab 03 - Average Number</li>
    <li>Lab 05 - Palindrome Checker</li>
    <li>Lab 06 - Credit Card Number Validation</li>
    <li>Lab 07 - Peaks & Valleys</li>
    <li>Lab 08 - Pick 6</li>
    <li>Lab 09 - Blackjack</li>
    <li>Lab 10 - Dad Jokes</li>
    <li>Lab 11 - Rot 13</li>
    <li>Lab 13 - Count Words</li>
    <li>Lab 14 - ATM</li>
    <li>Lab 16 - Searching & Sorting</li>
    <li>Lab 17 - Contact List</li>
    <li>Lab 19 - Trivia API</li>
    <li>Lab 20 - Adventure (mob)</li>
    <li>Mini-Capstone</li>
    <summary>Optional:</summary>
    <ul>
      <li>Stack and Linked List</li>
      <li>15 - Rain Data</li>
      <li>
      Create a Binary Search Tree
        <ul>
            <li>Add elements</li>
            <li>Search</li>
            <li>Delete elements</li>
        </ul>
      </li>
    </ul>
  </ul>
</details>

<details open>
  <summary>HTML/CSS/Flask</summary>
  <ul>
    <li>Lab 01 - Bio</li>
  </ul>
</details>

## Submitting your work

Make sure all labs are located within `Class_Raven/Code/<YourName>`

To emulate a more professional Git workflow, we're going to start creating new branches for each lab starting in the HTML/CSS section.
<h2>Creating a new branch:</h2>
<details>
<summary>Click to expand</summary>



- `git branch` to check that you're on the master branch

- `git status` to check if your local master branch is up to date with origin/master on Github.
  
- `git pull` if needed to pull any recent changes to your local repository

- Create a new branch and switch to it.
  - Option 1:
    - `git branch <YOUR_NAME-SECTION-LAB_NUMBER>`
    - `git checkout <YOUR_NAME-SECTION-LAB_NUMBER>`
  
  - Option 2:
  
    The `-b` flag can be used after the `checkout` command to combine these two steps:

    `git checkout -b <YOUR_NAME-SECTION-LAB_NUMBER>`
  
  **e.g.** My branch for the **"Lab 01 - Bio"** in the **HTML/CSS** section would be named: `keegan-htmlcss-lab01`. The name can vary a bit from this example, but please keep the chosen formatting consistent from one lab to another.

- `git add <FILENAME>` to add a specific file or `git add .` to add everything in the current dicrectory
  
- `git commit -m "your commit message"` to commit your work

- Before pushing your new branch, be sure to check the master branch for any updates. Anything changes that were merged into the master branch while you were working on your branch will need to be pulled and merged into your branch.

- A remote branch will need to be created for each new local branch. Git will usually display the proper command to do this when a new branch is pushed for the first time.

  The command is:

  `git push --set-upstream origin <BRANCH_NAME>`

  **OR**

  `git push -u origin <BRANCH_NAME>`
  
  <details>
    <summary>Screenshot</summary>
    <img src="screenshots/set_upstream_message.png" width=800>
  </details>

- After successfully pushing your new branch to Github, you should see the option to create a Pull Request for your branch on the main repo page.

  <details>
    <summary>Screenshot</summary>
    <img src="screenshots/pull_request_button.png" width=800>
  </details>

- If you don't see that message, you'll have to navigate to your new remote branch
  <details>
    <summary>Screenshot</summary>
    <img src="screenshots/switch_branch.gif" width=800>
  </details>

- Once you've navigated to your individual branch, you'll find the option to create a Pull Request in the "Contribute" dropdown.
  <details>
    <summary>Screenshot</summary>
    <img src="screenshots/open_pull_request_alternative.gif" width=800>
  </details>

- Click the "Open Pull Request" button. Add a comment to your Pull Request like "Submitting Lab 00" and click "Create Pull request"
  <details>
    <summary>Screenshot</summary>
    <img src="screenshots/create_pull_request.png" width=800>
  </details>
</details>

## Updating a branch
<details>
<summary>Click to expand</summary>
After a Pull Request is submitted, the code on that branch will be checked. Necessary corrections or adjustments will be posted as comments on the Pull Request on Github.

Corrections will be made only to that particular branch.

- `git checkout master` to switch to the master branch

- `git pull` to add the changes from the master branch into your branch.

- `git checkout <YOUR_NAME-SECTION-LAB_NUMBER>`

- `git merge master` to pull any updates from the master branch into your branch

- Add and commit updated files.

- `git push` to push your changes up to the remote repository on GitHub

- Only one Pull Request is allowed per branch. A message will be added to the current Pull Request for the new commits.

- Once a lab is complete, its branch will be merged into master.
</details>

---

## Additional Resources

<details>
  <summary>Screen Capture Tools for Creating GIFs for Project READMEs</summary>
  <ul>
    <li>
      Windows - <a href="https://www.screentogif.com">Screen to GIF</a>
    </li>
    <li>
      MacOS - <a href="https://apps.apple.com/us/app/giphy-capture-the-gif-maker/id668208984?mt=12">GIPHY</a>
    </li>
    <li>
      Linux - <a href="https://github.com/phw/peek">Peek</a>
    </li>
  </ul>
</details>


<details>
  <summary>Webpage Styling</summary>

  <p><b>Flexbox Games</b></p>
  <ul>
    <li><a href="https://flexboxfroggy.com/">Flexbox Froggy</a></li>
    <li><a href="https://mastery.games/flexboxzombies/">Flexbox Zombies</a></li>
  </ul>

  <p><b>Color Schemes</b></p>
  <ul>
    <li><a href="https://coolors.co">Coolors</a></li>
    <li><a href="https://color.adobe.com/create/color-wheel">Adobe Color Wheel</a></li>
  </ul>

  <p><b>Design Principles</b></p>
  <ul>
    <li><a href="https://www.canva.com/learn/20-web-design-principles-follow/">20 Web Design Principles</a></li>
    <li><a href="https://blog.tubikstudio.com/anatomy-of-web-page/">Anatomy of a Webpage</a></li>
    <li><a href="https://blog.devgenius.io/what-are-html-semantic-tags-and-why-should-you-care-a0403972a217">What are Semantic HTML Tags and Why You Should Care</a></li>
    <li><a href="https://kinsta.com/blog/html-best-practices/">HTML Best Practices</a></li>
  </ul>
</details>
  
<details>
  <summary>CSS Preprocessors</summary>
  <ul>
    <li><a href="https://youtu.be/RhX2rb10AC4">Intro to & Bootstrap Theming with Sass</a></li>
  </ul>
</details>

<details>
  <summary>Coding Principles</summary>
  <ul>
    <li><a href="https://x-team.com/blog/principles-clean-code/">Principles of Clean Code</a></li>
  </ul>
</details>
  

