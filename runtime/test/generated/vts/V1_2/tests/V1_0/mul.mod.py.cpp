// Generated from mul.mod.py
// DO NOT EDIT
// clang-format off
#include "GeneratedTests.h"

namespace generated_tests::mul {

std::vector<::test_helper::MixedTypedExample>& get_examples();

} // namespace generated_tests::mul

namespace android::hardware::neuralnetworks::V1_2::generated_tests::mul {

Model createTestModel();
bool is_ignored(int);

TEST_F(NeuralnetworksHidlTest, mul) {
  Execute(device,
          createTestModel,
          is_ignored,
          ::generated_tests::mul::get_examples());
}

TEST_F(ValidationTest, mul) {
  const Model model = createTestModel();
  const std::vector<Request> requests = createRequests(::generated_tests::mul::get_examples());
  validateEverything(model, requests);
}

} // namespace android::hardware::neuralnetworks::V1_2::generated_tests::mul

namespace generated_tests::mul {

std::vector<::test_helper::MixedTypedExample>& get_examples_dynamic_output_shape();

} // namespace generated_tests::mul

namespace android::hardware::neuralnetworks::V1_2::generated_tests::mul {

Model createTestModel_dynamic_output_shape();
bool is_ignored_dynamic_output_shape(int);

TEST_F(DynamicOutputShapeTest, mul_dynamic_output_shape) {
  Execute(device,
          createTestModel_dynamic_output_shape,
          is_ignored_dynamic_output_shape,
          ::generated_tests::mul::get_examples_dynamic_output_shape(), true);
}

TEST_F(ValidationTest, mul_dynamic_output_shape) {
  const Model model = createTestModel_dynamic_output_shape();
  const std::vector<Request> requests = createRequests(::generated_tests::mul::get_examples_dynamic_output_shape());
  validateEverything(model, requests);
}

} // namespace android::hardware::neuralnetworks::V1_2::generated_tests::mul
