# Feature Engineering for Car Price Prediction

## Summary of Results

### Key Findings

- **Final 7 Features Chosen:**  
  `Year`, `Model`, `State`, `Mileage`, `Trim`, `Make`, `Body Style`

- **Performance of the Final Model (7 Features):**
  - Mean Absolute Error (MAE): 2216.44
  - Mean Squared Error (MSE): 10367387.06
  - R2 Score: 0.9402  
  ![Boxplot for 7 Features](https://github.com/user-attachments/assets/c8c22af9-b9b7-4b9d-91ac-4b87bf726229)

## Conclusion

The analysis demonstrates that using 7 features strikes the best balance between model performance and simplicity. The final model, with 7 features, achieves a slightly lower MAE and MSE than the model with 6 features while maintaining a high R2 score. Although adding an 8th feature provides marginally better performance, the complexity introduced by the "City" feature, which expands the feature set to 4,191 columns, outweighs the benefits. Limiting the model to 7 features results in a more efficient model with 980 columns, balancing accuracy and computational efficiency. Therefore, the 7-feature model is selected for the final implementation.
