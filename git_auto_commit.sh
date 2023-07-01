fill_message="dockerize service scrape and make auto commit"
commit_user=$(git config user.name)
commit_message='$fill_message $commit_user'

git add . 

git commit -m "$commit_message"

echo "Changes already commited and ready to push, pls do double check to make sure!"