# Team Documentation - Cloning Repo

## One-time Instructions
The following are instructions that only need to be done the first time around. Following the 2-13-2025 upload, these should not need to be repeated.

1. Navigate to the source repo
2. You will need to create a destination to the remote repo with the following command
```
git remote add destination https://github.com/destination-username/destination-repo.git
```
In our case, during the 24-25 challenge, our URL is `https://github.com/NASA-SUITS-Teams/Selene-2025`
3. Since the repo is empty, this isn't strictly necessary, but good practice to fetch anything from the destination to ensure you're in sync.
```
git fetch destination
```
wth that being said, if there are any changes, you will need to run
```
git merge destination/main
```
> Please note this will throw an error if the repo is empty

4. I initially ran into trouble trying to merge from the repo, so I added a file indicating the date of the upload. I'm unsure whether this step helped or made the folowing process more complicated

5. You will need to allow merging of branches with different commit histories with the following command
```
git pull destination main --allow-unrelated-histories
```
### Continued Use
Since the above have already been set up and done once, the following are the only things you should have to run.

1. Fetch anything from the destination to ensure you're in sync.
```
git fetch destination
```
If there are any changes, you will need to run
```
git merge destination/main
```

2. Ensure you are on the main branch
```
git branch
```
> Ensure `main` appears highlighted with an asterisk `*`

If not on main, transition to main with `git checkout main`

3. Push changes from source to remote repo (main branch)
```
git push destination main
```


<br>
Once all of that is accomplished, it should be good to go!