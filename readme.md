# showcase: datasette with billboard.js

## about

Demo using [billboard.js](https://naver.github.io/billboard.js/) with [datasette](https://datasette.io/).

This repo is a showcase for a [blogpost](https://madflex.de/add-plots-to-datasette-pages-using-billboard-js/) and will not be updated in the future!

## run

setup / run
```
python init_db.py
datasette demo.db --template-dir templates --plugins-dir plugins --static assets:static
```
