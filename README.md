#How to generate ssh key

    ssh-keygen -t ed25519 -C "gordonkao0709@gmail.com"
    //first enter is created directory
    //second enter is password.
    //third enter is password check.
    cat ~\.ssh\id_ed25519.pub //pub mean public key
    //copy and paste things to "New SSH Key"
    //succes generate ssh key

 
# 114_backend

echo "# 114_backend" >> README.md

git init

git add README.md

git commit -m "init"

git config --global user.email "gordonkao0709@gmail.com"

git config --global user.nam "Wasabi7799"

git commit -m "init"

git branch -M main

git remote add origin https://github.com/Wasabi7799/114_backend.git

git push -u origin main



