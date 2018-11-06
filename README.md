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

Then install python dependencies :

```
pipenv install
pipenv shell 
```

And use `md2pdf`
