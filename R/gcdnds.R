library(ggplot2)

setwd("C:\\Users\\User\\Desktop\\fyp_data")
data1 <- read.csv("dnds_mean.csv")
data2 <- read.csv("dnds_median.csv")

colors <- c("#e41a1c", # Alpha
            "#377eb8", # Beta
            "#4daf4a", # Delta
		"#984ea3") # Gamma

par(mfrow = c(1, 2))

plot(data1$GC_content, data1$Mean_dnds, main = "GC content against mean dN/dS", xlab = "GC Content (%)", ylab = "Mean dN/dS Ratio", xlim = c(30, 50), ylim = c(0.075, 0.2), pch=16, col = colors[factor(data$Genus)])

legend("bottomright",
       legend = levels(factor(data$Genus)),
       pch = 19,
       col = colors,
	 cex=0.8)
#
#plot(data2$GC_content, data2$Median_dnds, main = "GC content against median dN/dS", xlab = "GC Content (%)", ylab = "Median dN/dS Ratio", xlim = c(30, 50), ylim = c(0.05, 0.2), pch=16, col = colors[factor(data$Genus)])
#
#legend("bottomright",
#      legend = levels(factor(data$Genus)),
#      pch = 19,
#      col = colors,
#	 cex=0.8)