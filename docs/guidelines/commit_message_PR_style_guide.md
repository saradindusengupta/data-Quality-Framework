# Pull Request and Commit Message Guidelines

## PR Guidelnes
1.  Put the name of the exercise in the subject line of the commit. E.g.  `hamming: Add test case for strands of unequal length`
2.  The subject line should be a one-sentence summary, and should not include the word  _and_  (explicitly or implied).
3.  Any extra detail should be provided in the body of the PR.
4.  Don't submit unrelated changes in the same pull request.
5.  If you had a bit of churn in the process of getting the change right, squash your commits. Refer to the guidelines on  squashing commits.
6.  If you had to refactor in order to add your change, then we'd love to see two commits: First the refactoring, then the added behavior. It's fine to put this in the same pull request, unless the refactoring is huge and would make it hard to review both at the same time.
7.  If you are referencing another issue or pull-request, for instance  `_closes #XXX`_  or  `_see #XXX`_, please include the reference in the body of the PR, rather than the subject line. This is simply because the subject line doesn't support markdown, and so these don't get turned into clickable links. It makes it harder to follow and to go look at the related issue or PR.
8.  Please also refer to the guidelines for  commit messages.
## Squashing

Squashing commits into a single commit is particularly useful when the change happened in lots of little (sometimes confusing) steps, but it really is one change.

There are a number of ways to accomplish this, and many people like to use an  interactive rebase, but it can be tricky if you haven't set git up to open your favorite editor.

An easier way to do this is to un-commit everything, putting it back into the staging area, and then committing it again.

Using the example from above, we have 5 commits that should be squashed into one.

    433a0e1 added spinning wheel tests
    1f7d4aa pass spinning wheel
    cf21737 oops
    be4c410 rename example file
    bb89a77 update config

To un-commit them, use the following incantation:

    $ git reset --soft HEAD^^^^^

Notice that there are 5 carets, one for each commit that you want to un-commit. You could also say:

    $ git reset --soft HEAD~5

If you do a  `git status`  now, you'll see all the changed files, and they're staged and ready to commit. If you do a  `git log`, you'll see that the most recent commit is from someone else.

Next, commit, as usual:

    $ git commit -m "Add spinning wheel problem"

Now if you do a  `git status`  you may get a warning saying that your origin and your branch have diverged. This is completely normal, since the origin has 5 commits and you have 1 (different) one.

The next step is to force push this up to your branch, which will automatically update the pull request, replacing the old commits with the new one.

    $ git push --force origin spinning-wheel

## Commit Messages

Commit messages are communication and documentation. They're a log of more than just  _what_  happened, they're about  _why_  it was done.

The longer a project is active, the more people involved, the larger the codebase, the more important it is to have good commit messages.

There's an excellent lightning talk by Ryan Geary called  [Do Your Commit Messages Suck?](https://www.youtube.com/watch?v=8YjSty6bfog). It's funny and enlightening, and you should watch it.

Two articles that have very clear guidelines about how to write excellent commit messages are Tim Pope's  [A Note About Git Commit Messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)  and Chris Beams'  [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/). Please read them.

### [](https://github.com/exercism/docs/blob/master/contributing/git-basics.md#examples)Examples

Imagine that you're submitting a new problem called "spinning-wheel" to the Ruby track.

Here's a fairly typical set of commits that you might end up making:

    433a0e1 added spinning wheel tests
    1f7d4aa pass spinning wheel
    cf21737 oops
    be4c410 rename example file
    bb89a77 update config

All of these commits are about a single thing: adding a new problem. They should be a single commit. They don't have to start out that way (life is messy), but once you're done, you should squash everything into one commit, and rename it cohesively:

    f4314e5 add spinning wheel problem
