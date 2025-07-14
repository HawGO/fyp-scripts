library(ggplot2)

setwd("C:\\Users\\User\\Desktop\\fyp_data")
data <- read.csv("plddtscore.csv")

colors <- c("#e41a1c", # Alpha
            "#377eb8", # Beta
            "#4daf4a", # Delta
		"#984ea3") # Gamma

plot(data	$pLDDT_Score, log10(data$MSA_Depth), main = "pLDDT score against log(MSA depth)", xlab = "pLDDT score", ylab = "log(MSA Depth)", pch=16, xlim = c(0, 100), ylim = c(0, 4), col = colors[factor(data$Genus)])

legend("topleft",
       legend = levels(factor(data$Genus)),
       pch = 19,
       col = colors,
	 cex=0.8)

