###############
### ALFALFA ###
###############
library(agricolae)
library(readxl)
datos = read_excel("alfalfa.xlsx")

datos$Parcela = as.factor(datos$Parcela)
anova_Dosis = aov(Dosis ~ Parcela,data = datos)
summary(anova_Dosis)

duncan_resultado = duncan.test(anova_Dosis, "Parcela", console = T)
TukeyHSD(anova_Dosis)
