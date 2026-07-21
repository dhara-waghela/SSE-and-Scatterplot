# Visualizing Sum of Squared Errors (SSE) vs. Intercept Parameter ($a_0$)

This repository contains a Python script that explores how the **Sum of Squared Errors (SSE)** varies as a function of the intercept parameter ($a_0$) in a simple linear model:

$$\hat{y} = a_0 + 0.7x$$

By fixing the slope at $a_1 = 0.7$ and sweeping $a_0$ from $-0.9$ to $1.7$, the script calculates the resulting SSE for each step and plots the resulting parabolic error curve.

<center>
  <img src="output.png" alt="Scatter Plot Output">
</center>

---

## - Overview & Theory

The goal of this project is to visually demonstrate how optimization algorithms (like gradient descent) find the best-fitting parameter by minimizing the total error.

### Formula
For a dataset of $m$ observations, the SSE is calculated as:

$$\text{SSE}(a_0) = \sum_{i=0}^{m-1} \left(y_i - \hat{y}_i\right)^2 = \sum_{i=0}^{m-1} \left(y_i - (a_0 + 0.7x_i)\right)^2$$

Where:
- **$x$**: Independent variable dataset `[1, 2, 3, 4, 5]`
- **$y$**: Dependent variable dataset `[1, 1, 2, 2, 4]`
- **$\hat{y}$**: Predicted values given intercept $a_0$ and slope $0.7$

---

## 📁 Repository Structure

```text
.
├── plot.py          # Python script with SSE function & matplotlib code
├── output.png       # Generated scatter plot visualization (SSE vs a0)
└── README.md        # Documentation
