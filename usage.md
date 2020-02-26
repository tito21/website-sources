---
nav: false
---

# YASSG (yet another static site generator)


Usage:

 1. Write a post in Markdown under the `_post` directory and include all assets
    in `_assets`.
 2. Run `python yassg.py`.
 3. cd into `public` and commit&push all changes
 4. cd back into the root directory and commit&push

The `public` folder is a manage as a git submodule as the instructions on the
(hugo docs)[https://gohugo.io/hosting-and-deployment/hosting-on-github/].
**Do not delate the folder or any of its contents**

The steps 2 and 3 are know manage by `deploy.sh`. Only writing post and
committing to the root repo should be done manually.