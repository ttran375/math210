Rscript -e "install.packages(c('rmarkdown', 'reticulate')"
Rscript -e "rmarkdown::render('assignment2.Rmd')"
Rscript -e "reticulate::py_install(c('numpy', 'matplotlib', 'scipy'))"
