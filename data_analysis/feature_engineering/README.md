# Feature Engineering for Car Price Prediction

## Summary of Results

### Key Findings

- **Final 7 Features Chosen:**
  - `Year`, `Model`, `State`, `Mileage`, `Trim`, `Make`, `Body Style`

- **6 Features:**
  - Mean Absolute Error (MAE): 2236.81
  - Mean Squared Error (MSE): 10459830.55
  - R2 Score: 0.9396
<img width="785" alt="Screenshot 2024-08-11 at 4 01 46 PM" src="https://github.com/user-attachments/assets/a9f772c5-702a-45a7-86b8-c7ee501be942">


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
