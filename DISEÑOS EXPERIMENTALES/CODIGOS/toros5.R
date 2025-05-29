###############
### TOROS 5 ###
###############
library(agricolae)
library(readxl)
datos = read_excel("toros5.xlsx")

datos$Toros = as.factor(datos$Toros)
anova_Peso = aov(Peso ~ Toros,data = datos)
summary(anova_Peso)

duncan_resultado = duncan.test(anova_Peso, "Toros", console = T)
TukeyHSD(anova_Peso)
