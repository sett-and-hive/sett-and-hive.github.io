# Building a tech-radar on sett-and-hive github.io

Publishing a site inspired by the ThoughtWorks "build-your-own-radar" tool on GitHub Pages (github.io).

## Configure Your Radar Data:

Edit `tech-radar.json` to your requirements.

## Generate the Tech Radar Site:

```bash
yarn build:clean
yarn build:radar
```

## Push to GitHub:

Once you've generated your radar site, you'll have a set of HTML, CSS, and other files in the `tech-radar` folder.
These need to be added to the sett-and-hive.github.io repository.

```bash
git add tech-radar/*
```

Commit these changes and push them to your GitHub repository:

```bash
git commit -m "Add generated radar site"
git push origin master
```

## Configure GitHub Pages:

Go to the `sett-and-hive.github.io` repository on GitHub.
Click on the "Settings" tab.
Scroll down to the "GitHub Pages" section.
In the "Source" dropdown menu, select the "sett-and-hive" branch that contains your radar site.
GitHub Pages will now build and publish your site. You'll see a message with a link to your published site once it's ready.

## Access Your Published Radar Site:

Your radar site should now be accessible at a URL like: https://sett-and-hive.github.io/tech-radar/
