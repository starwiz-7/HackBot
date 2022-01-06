# HackBot 🔥

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->
<!-- ![GitHub repo size](https://img.shields.io/github/repo-size/scottydocs/README-template.md)
![GitHub contributors](https://img.shields.io/github/contributors/scottydocs/README-template.md)
![GitHub stars](https://img.shields.io/github/stars/scottydocs/README-template.md?style=social)
![GitHub forks](https://img.shields.io/github/forks/scottydocs/README-template.md?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/scottydocs?style=social) -->

HackBot is a `Discord Bot` that notifies `hackers, developers` about `upcoming hackathons`.

The bot uses the scraped data from MLH, Devfolio, Devpost and HackerEarth to notify users about new hackathon as soon as it is listed on the website. Users can also see all the hackathons listed on site in discord itself.
(Support for other websites to be added soon)

### HackBot currently serves 50+ discord servers with 10000+ members!
## Prerequisites

Before you begin, ensure you have met the following requirements:

<!--- These are just example requirements. Add, duplicate or remove as required --->

-   You have installed the latest version of `Python`
-   You have a `<Windows/Linux/Mac>` machine.

## Installing HackBot

To install HackBot, follow these steps:

-   First move to the HackBot folder
-   Run these commands

Linux and macOS:

```
python -m pip install -r requirements.txt
```

Windows:

```
py -m pip install -r requirements.txt
```

## Using HackBot

To use HackBot, follow these steps:

-   Move to the HackBot folder
-   Run the following command

```
python bot.py
```

## HackBot Commands

```
;hack notify <channel_name>
Assign a channel for upcoming hackathons notification
```
```
;hack web <website_name>
Fetch all hackathons listed on website.
```
Supported websites:
- MLH
- Devfolio
- Devpost

```
;hack unsub
Unsubscribe for upcoming hackathon notifications.
```
```
;hack issue "Feature/Issue title" "Feature/Issue description"
Report any issue or request any feature
```


## Roadmap
  
- [x]  Deploying the Discord Bot on Heroku
- [ ] Commands for users to retreive hackathon based on date

## Issues, Bugs, Features

-   Have you encountered any issue while using the bot, tell us by creating an issue.
-   Want some more features to be implemented, look no further than the issues section.

## Contributing to HackBot

<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->

To contribute to HackBot, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributor

-   [@starwiz-7](https://github.com/starwiz-7) 📖

## Contact

If you want to contact me you can reach me at aryan2019@iiitkottayam.ac.in

## License

<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: [MIT](https://github.com/starwiz-7/HackBot/blob/main/LICENSE).
