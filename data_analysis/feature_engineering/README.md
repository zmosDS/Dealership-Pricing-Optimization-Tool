# Feature Engineering for Car Price Prediction

## Introduction

In this notebook, I perform feature engineering to enhance the predictive power of the machine learning models used for car price prediction. The focus is on exploring the impact of different numbers of predictors on model performance, evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), and R2 Score.

## Summary of Results

### Key Findings

- **6 Predictors:**
  - Mean Absolute Error (MAE): 2236.81
  - Mean Squared Error (MSE): 10459830.55
  - R2 Score: 0.9396

- **7 Predictors:**
  - Mean Absolute Error (MAE): 2216.44
  - Mean Squared Error (MSE): 10367387.06
  - R2 Score: 0.9402

- **8 Predictors:**
  - Mean Absolute Error (MAE): 2201.78
  - Mean Squared Error (MSE): 10192004.88
  - R2 Score: 0.9412

## Conclusion

The analysis shows that using 7 predictors strikes the best balance between model performance and simplicity, with a slightly lower MAE and MSE than 6 predictors, while maintaining a high R2 score. Although the model with 8 predictors provides marginally better performance, the difference is minimal, and reducing the number of predictors can help prevent overfitting. I will therefore proceed with 7 predictors for the final model, ensuring optimal results with a reduced risk of overfitting.

