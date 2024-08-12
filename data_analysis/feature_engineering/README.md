# Feature Engineering for Car Price Prediction

## Summary of Results

### Key Findings

- **Final 7 Features Chosen:**
  - `Year`, `Model`, `State`, `Mileage`, `Trim`, `Make`, `Body Style`

- **6 Features:**
  - Mean Absolute Error (MAE): 2236.81
  - Mean Squared Error (MSE): 10459830.55
  - R2 Score: 0.9396
<img width="779" alt="Screenshot 2024-08-11 at 10 24 24 PM" src="https://github.com/user-attachments/assets/a8c7f886-8856-4e3b-8a82-d20d90bf28c8">

- **7 Features:**
  - Mean Absolute Error (MAE): 2216.44
  - Mean Squared Error (MSE): 10367387.06
  - R2 Score: 0.9402
<img width="776" alt="Screenshot 2024-08-11 at 10 25 02 PM" src="https://github.com/user-attachments/assets/c8c22af9-b9b7-4b9d-91ac-4b87bf726229">

- **8 Features:**
  - Mean Absolute Error (MAE): 2201.78
  - Mean Squared Error (MSE): 10192004.88
  - R2 Score: 0.9412
<img width="776" alt="Screenshot 2024-08-11 at 10 25 33 PM" src="https://github.com/user-attachments/assets/f62ed221-ecda-4cf1-ac47-a2dfc8ad736a">

## Conclusion

The analysis shows that using 7 features strikes the best balance between model performance and simplicity, with slightly lower MAE and MSE than 6 features while maintaining a high R2 score. Although the model with 8 features provides marginally better performance, the difference is minimal, and reducing the number of features can help prevent overfitting. Moreover, the 8th feature, "City," introduces over 3,200 unique values, which, when one-hot encoded, expands the feature set to 4,191 columns. In contrast, using 7 features limits the number of columns to 980, significantly smaller than the 4,191 columns with 8 features. This reduction keeps the model more efficient and manageable, ensuring optimal performance without unnecessary complexity. Therefore, I will proceed with 7 features for the final model, balancing model accuracy and computational efficiency.
