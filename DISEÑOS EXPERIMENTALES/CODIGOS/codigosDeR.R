###############
### TOROS 6 ###
###############
library(agricolae)
library(readxl)
datos = read_excel("toros6.xlsx")

datos$Toros = as.factor(datos$Toros)
anova_Peso = aov(Peso ~ Toros,data = datos)
summary(anova_Peso)

duncan_resultado = duncan.test(anova_Peso, "Toros", console = T)
TukeyHSD(anova_Peso)


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
