# How to generate ssh key

    ssh-keygen -t ed25519 -C "user@gmail.com"
    //first enter is created directory
    //second enter is password.
    //third enter is password check.
    cat ~\.ssh\id_ed25519.pub //pub mean public key
    //copy and paste things to "New SSH Key"
    //succes generate ssh key
# Clone the project in cmd or terminal
    git clone git@....
# Create project-virtual-environment
    python3 -m venv .venv
    Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
    .\.venv\Scripts\Activate.ps1
## Pip install things...
    //generate requirements.txt and memory your library
    pip freeze > requirements.txt
    pip install -r requirements.txt
    //how to easily install you need library...
    pip install -r requirements.txt
    
# 114_backend
    echo "# 114_backend" >> README.md
    git init
    git add README.md
    git commit -m "init"
    git config --global user.email "user@gmail.com"
    git config --global user.nam "Wasabi7799"
    git commit -m "init"
    git branch -M main
    git remote add origin https://github.com/Wasabi7799/114_backend.git
    git push -u origin main








