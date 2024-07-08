<p align="center">
<img src="https://blogs.cappriciosec.com/uploaders/ghostrecon-tool.png" ><br>

</p>

> Cloud-Based, Fast, and Customizable Web Recon Tool.

<p align="left"> <img src="https://komarev.com/ghpvc/?username=karthi-the-hacker&label=Profile%20views&color=0e75b6&style=flat" alt="karthi-the-hacker" /> </p>
<p align="left"> <a href="https://twitter.com/karthithehacker" target="blank"><img src="https://img.shields.io/twitter/follow/karthithehacker?logo=twitter&style=for-the-badge" alt="karthithehacker" /></a> </p>

## Prerequisites

- NodeJs
- Python3
- Go
- pip3 
- npm

### Screen Shots 📸 :
<h1 align="center">
  <h2 align="center">Screen Shot 1</h2>
  <h1 align="center"><img align="center" src="https://github.com/karthi-the-hacker/ghostrecon/raw/main/screenshots/1.png" width="700px" alt="Gh0stR3c0n"></h1>
  <h2 align="center">Screen Shot 2</h2>
 <h1 align="center"> <img align="center" src="https://github.com/karthi-the-hacker/ghostrecon/raw/main/screenshots/2.png" width="700px" alt="Gh0stR3c0n"></h1>


 
</h1>

## Steps to install for Linux  &  Mac🐧 👨🏽‍💻:

<h1 align="center"><img align="center" src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/245f4571-14d4-4069-90a7-259b2971229f/del3rk1-177dea3e-01d6-4c32-bcfd-8927b7bc8364.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzI0NWY0NTcxLTE0ZDQtNDA2OS05MGE3LTI1OWIyOTcxMjI5ZlwvZGVsM3JrMS0xNzdkZWEzZS0wMWQ2LTRjMzItYmNmZC04OTI3YjdiYzgzNjQucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.RDHFl6JxHrJPAZGg1gIyuGEOJCn9WMTLlNYVlu8Ql5E" width="100px" alt="Gh0stR3c0n"></h1>

<h1 align="center">
<img align="center" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Kali-dragon-icon.svg/2048px-Kali-dragon-icon.svg.png" width="100px" alt="kali">
<img align="center" src="https://brandslogos.com/wp-content/uploads/thumbs/debian-logo-vector.svg" width="50px" alt="debian">
<img align="center" src="https://upload.wikimedia.org/wikipedia/commons/4/45/Parrot_Logo.png" width="70px" alt="parrot os">
  <img align="center" src="https://www.backbox.org/wp-content/uploads/2018/09/website_backbox_text_black.png" width="100px"  alt="blackbox">
<img align="center" src="https://assets.ubuntu.com/v1/17b68252-apple-touch-icon-180x180-precomposed-ubuntu.png" style="border-radius: 50%;" width="100px"  alt="ubuntu">
  
  

## Installation and Example

1. Install NodeJS [Instructions Here](https://nodejs.org/en/download/package-manager/) (If you can't figure this out, you shouldn't really be using this)

   - Github
     - click [HERE](https://github.com/karthi-the-hacker/ghostrecon.git) for downloads
   - Change Directory
     - `cd ghostrecon`

2. Setting up `Ghostrecon`

    - Running Setup scripts
      -  `mkdir ~/recon`
      -  `mkdir ~/recon/ghostrecon/`
      -  `chmod +x index.js`
      -  `chmod +x setup.sh`
      -  `./setup.sh` if the setup shows any error install the requirements manually
      -  ` npm i ` If incase setup shows any error run this command

4. Configurations 
   - Telegram Notification
     - `nano config.yaml`
     - `chat_ID: your_ChatID` Replace with your telegram chat id
     - Open your telegram and search for [`@CappricioSecuritiesTools_bot`](https://web.telegram.org/k/#@CappricioSecuritiesTools_bot) and click start
     
   - Github Recon
     - `github_token: your_github_token` Replace with your Github Token
     

   - Deep Recon
     - `Subs_Scan_Fast: True` True disable the Subdomain Brute-forcing & Amass 
     - `Subs_of_Subs: True` True disable the Subdomains of Subdomain discovery
     - By default, changes are saved as 'True' according to your preference.
     - Save and Exit

5. Starting Ghostrecon
   - Run Command
     - `./index.js` To start Ghost Recon run this command
   - Start Recon 
     - `open http://localhost:8090` Open this url in your browser
     - `open http://localhost:8090/new` Start new recon

## Installation in docker

Simply run the following command

```docker compose up --build -d```

```docker exec -it ghostrecon bash```

```npm install```

```npm start```

```http://localhost:8090```

Simply acccess this uri in your browser

## Features ⚙️ :

 - SubDomain Recon.
 - SubDomains of SubDomain Recon.
 - Finding Live with unique open ports.
 - Finding open ports. 
 - WebCrawling.
 - Pattern Matching.
 - GUI Modern Web interface
 - Telegram Bot 🔔 Notification 🔔 [`@CappricioSecuritiesTools_bot`](https://web.telegram.org/k/#@CappricioSecuritiesTools_bot)

### Required tools ⚒️ :

- [Amass](https://github.com/OWASP/Amass)
- [Subfinder](https://github.com/projectdiscovery/subfinder)
- [Naabu](https://github.com/projectdiscovery/naabu)
- [Httpx](https://github.com/projectdiscovery/httpx)
- [Katana](https://github.com/projectdiscovery/katana)
- [gf](https://github.com/tomnomnom/gf)
- [gf-Patterns](https://github.com/1ndianl33t/Gf-Patterns)

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://twitter.com/karthithehacker" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="karthithehacker" height="30" width="40" /></a>
<a href="https://www.linkedin.com/in/karthikeyan--v/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="cyberspartan" height="30" width="40" /></a>
<a href="https://instagram.com/karthithehacker" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="karthithehacker" height="30" width="40" /></a>
<a href="https://www.youtube.com/channel/UCyiZHuoDz8KP3quElBBAmJQ" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="karthithehacker" height="30" width="40" /></a>
</p>

