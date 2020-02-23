data <- read.csv("model_data.csv", sep="\t")
View(data)
# X1: CPI
# X2: GDP
# X3: Government Spending
# X4: Unemployment Rate
results = lm(X3 ~ X1 + X2 + X4, data)
summary(results)

# Equation: 
# Government spending = -82.753 - 0.284*CPI + 0.009*GDP + 10.369*Unemployment_Rate