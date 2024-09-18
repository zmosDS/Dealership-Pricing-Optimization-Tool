# Feature Engineering for Vehicle Price Prediction

## Objective
The objective of this notebook is to evaluate various combinations of features for predicting vehicle prices using the LightGBM model. The goal is to identify the optimal feature set that balances **Mean Absolute Error (MAE)** and **Mean Squared Error (MSE)** while ensuring the model can generalize effectively to unseen data.

## Process

1. **Feature Selection**:
   - Tested different combinations of features from the dataset, ranging from 2 to 8 features.
   - Each combination was evaluated on the test set using MAE, MSE, R² score, and execution time.
   
2. **Feature Combinations Tested**:
   - **2 Features**: `Year`, `Model`
   - **3 Features**: `Year`, `Model`, `Trim`
   - **4 Features**: `Year`, `Model`, `Mileage`, `Trim`
   - **Up to 8 Features**: Full feature set, including `Body Style`, `Make`, and `City`.

3. **Results**:
   - The model with **7 features** demonstrated the best balance between generalization and accuracy.
   - While the **8-feature model** had a slightly better MAE, the **7-feature model** showed a better MSE, indicating that it handles large errors more effectively.
   - Removing the `City` feature improved the model's efficiency without sacrificing accuracy due to the high cardinality of that column (~3,000 unique values).

4. **Validation**:
   - Both the 7- and 8-feature models were applied to the validation set to assess generalization.
   - The **7-feature model** was chosen as the final feature set for further optimization due to its ability to generalize better when exposed to new data.

## Conclusion
The **7-feature model** is the best candidate for moving forward in the project. It strikes an optimal balance between reducing errors (MAE and MSE) and efficiently managing the high cardinality of the dataset's categorical features. The next steps involve applying hyperparameter optimization to further improve the model's performance.
