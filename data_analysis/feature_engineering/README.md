# Feature Engineering for Car Price Prediction

## Summary of Results

### Key Findings

- **Final 7 Features Chosen:**
  - `Year`, `Model`, `State`, `Mileage`, `Trim`, `Make`, `Body Style`

- **6 Features:**
  - Mean Absolute Error (MAE): 2236.81
  - Mean Squared Error (MSE): 10459830.55
  - R2 Score: 0.9396

- **7 Features:**
  - Mean Absolute Error (MAE): 2216.44
  - Mean Squared Error (MSE): 10367387.06
  - R2 Score: 0.9402

- **8 Features:**
  - Mean Absolute Error (MAE): 2201.78
  - Mean Squared Error (MSE): 10192004.88
  - R2 Score: 0.9412

## Conclusion

The analysis shows that using 7 features strikes the best balance between model performance and simplicity, with a slightly lower MAE and MSE than 6 features, while maintaining a high R2 score. Although the model with 8 features provides marginally better performance, the difference is minimal, and reducing the number of features can help prevent overfitting. I will therefore proceed with 7 features for the final model, ensuring optimal results with a reduced risk of overfitting.
