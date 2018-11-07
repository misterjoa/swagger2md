# What is this project ?

No simple swagger to markdown converter currently exists in python.
In order not to introduce java dependencies from popular projects when doing a python project, I created a very simple converter.

```
./swagger2md.py swagger.json swagger.md
```

# Convert md to pdf 

Then you can use a md to pdf converter like pandoc to produce a pdf file !

## Debian 9

```
apt-get install pandoc texlive-latex-recommended texlive-fonts-recommended
```

# Usage

## Basic styling

```
pandoc -s swagger.md -o swagger.pdf
```

## css styling

If you want to style using md -> html converter

```
apt install wkhtmltopdf
pandoc -t html5 -c swagger.css --toc -s swagger.md -o swagger.pdf
```

An example `swagger.css` is included, modify it if you need to !
