##############
### CEBADA ###
##############
library(agricolae)
library(readxl)
datos = read_excel("cebada.xlsx")

datos$Cebada = as.factor(datos$Cebada)
anova_Cosecha = aov(Cosecha ~ Cebada,data = datos)
summary(anova_Cosecha)

duncan_resultado = duncan.test(anova_Cosecha, "Cebada", console = T)
TukeyHSD(anova_Cosecha)
