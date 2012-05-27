#!/usr/bin/env Rscript
library(ggplot2)

# read.csv('../queries/middlenames.csv')
m.all <- read.csv('/tmp/middlenames.csv') # In RAM
m.all <- na.omit(m.all)

m.timeline<-function(m.df) {
  ggplot(m.df) +
    aes(x=year, y=(k/n), group=state, size=n, label=state) +
#   scale_x_continuous(label='Birth year') +
    geom_line()
}

# Each state separately
timelines <- dlply(m.all, 'state', function(m.df) {
  m.timeline(m.df) + 
  opts(title=as.character(m.df[1, 'state']))
})

# All of the states
timelines$all <- m.timeline(m.all)
