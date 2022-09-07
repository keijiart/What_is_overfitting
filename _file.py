load_file_in_context('script.py')
# Tests go here
compare_mse = np.mean((pred_test - y_test)**2)
if compare_mse != MSE_test:
  fail_tests('Did you set MSE_test to `np.mean((pred_test - y_test)**2)`?')
  
pass_tests()