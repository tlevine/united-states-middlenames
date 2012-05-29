#!/usr/bin/env Rscript
library(ggplot2)

m.all <- read.csv('../queries/middlenames.csv')
#m.all <- read.csv('/tmp/middlenames.csv') # In RAM
m.all <- na.omit(m.all)
#m.all <- subset(m.all, n >= 10)

m.timeline<-function(m.df) {
  ggplot(m.df) +
    aes(x=year, y=(k/n), group=state, size=n, label=state) +
    labs(size='Births', group='State',
      x='Birth year',
      y='Proportion with middle names'
    ) +
    opts(title='Prevalence of Middle Names over time by state\nEach dot represents birth for a particular year and state.') +
#   scale_color_manual(values='black') +
    geom_point(alpha=1/5)
}

# Each state separately
timelines <- dlply(m.all, 'state', function(m.df) {
  m.timeline(m.df) +
  opts(title=paste(
    'Prevalence of Middle Names over time for',
     as.character(m.df[1, 'state'])
  ))
})
# All of the states
timelines$all <- m.timeline(m.all)

# A book to flip through
m.book <- function(){
  pdf('middle_names_over_time_by_state.pdf',
    width=17, height=11,
    fonts='Helvetica', family='Helvetica'
  )
  print(timelines)
  dev.off()
}

# A flashy image to put in a blog post
m.flashy <- function(width=1680, height=1050){
  jpeg(paste('middle_names_over_time_by_state', width, height, 'jpeg', sep='.'),
    width=width, height=height)
  print(timelines$all) 
  dev.off()
}

m.flashy(1680, 1050)
m.flashy(1280, 720)
m.flashy(800, 640)
m.flashy(640, 480)
m.flashy(851, 315)
