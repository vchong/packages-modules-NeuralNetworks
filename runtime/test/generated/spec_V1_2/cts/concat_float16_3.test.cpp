// Generated from concat_float16_3.mod.py
// DO NOT EDIT
// clang-format off
#include "TestGenerated.h"


namespace generated_tests::concat_float16_3 {

const ::test_helper::TestModel& get_test_model();

TEST_F(GeneratedTests, concat_float16_3) { execute(get_test_model()); }

TEST_F(DynamicOutputShapeTest, concat_float16_3) { execute(get_test_model()); }

} // namespace generated_tests::concat_float16_3

TEST_AVAILABLE_SINCE(V1_2, concat_float16_3, generated_tests::concat_float16_3::get_test_model());


namespace generated_tests::concat_float16_3 {

const ::test_helper::TestModel& get_test_model_all_inputs_as_internal();

TEST_F(GeneratedTests, concat_float16_3_all_inputs_as_internal) { execute(get_test_model_all_inputs_as_internal()); }

TEST_F(DynamicOutputShapeTest, concat_float16_3_all_inputs_as_internal) { execute(get_test_model_all_inputs_as_internal()); }

} // namespace generated_tests::concat_float16_3

TEST_AVAILABLE_SINCE(V1_2, concat_float16_3_all_inputs_as_internal, generated_tests::concat_float16_3::get_test_model_all_inputs_as_internal());
