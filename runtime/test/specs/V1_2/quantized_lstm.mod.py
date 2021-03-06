#
# Copyright (C) 2017 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.  #

# LSTM Test: No Cifg, No Peephole, No Projection, and No Clipping.

model = Model()

n_batch = 2
n_input = 2
n_cell = 4
n_output = n_cell

InputType = ("TENSOR_QUANT8_ASYMM", [n_batch, n_input], 1 / 128, 128)
input_ = Input("input", InputType)

weights_scale = 0.00408021
weights_zero_point = 100

InputWeightsType = ("TENSOR_QUANT8_ASYMM",
                    [n_output, n_input], weights_scale, weights_zero_point)
input_to_input_weights = Input("inputToInputWeights", InputWeightsType)
input_to_forget_weights = Input("inputToForgetWeights", InputWeightsType)
input_to_cell_weights = Input("inputToCellWeights", InputWeightsType)
input_to_output_weights = Input("inputToOutputWeights", InputWeightsType)

RecurrentWeightsType = ("TENSOR_QUANT8_ASYMM",
                        [n_output, n_output], weights_scale, weights_zero_point)
recurrent_to_input_weights = Input("recurrentToInputWeights", RecurrentWeightsType)
recurrent_to_forget_weights = Input("recurrentToForgetWeights", RecurrentWeightsType)
recurrent_to_cell_weights = Input("recurrentToCellWeights", RecurrentWeightsType)
recurrent_to_output_weights = Input("recurrentToOutputWeights", RecurrentWeightsType)

BiasType = ("TENSOR_INT32", [n_output], weights_scale / 128., 0)
input_gate_bias = Input("inputGateBias", BiasType)
forget_gate_bias = Input("forgetGateBias", BiasType)
cell_gate_bias = Input("cellGateBias", BiasType)
output_gate_bias = Input("outputGateBias", BiasType)

StateType = ("TENSOR_QUANT16_SYMM", (n_batch, n_cell), 1 / 2048, 0)
OutputType = ("TENSOR_QUANT8_ASYMM", (n_batch, n_output), 1 / 128, 128)
prev_cell_state = Input("prevCellState", StateType)
prev_output = Input("prevOutput", OutputType)

cell_state_out = Output("cellStateOut", StateType)
output = Output("output", OutputType)


model = model.Operation("QUANTIZED_16BIT_LSTM",
                        input_,
                        input_to_input_weights,
                        input_to_forget_weights,
                        input_to_cell_weights,
                        input_to_output_weights,
                        recurrent_to_input_weights,
                        recurrent_to_forget_weights,
                        recurrent_to_cell_weights,
                        recurrent_to_output_weights,
                        input_gate_bias,
                        forget_gate_bias,
                        cell_gate_bias,
                        output_gate_bias,
                        prev_cell_state,
                        prev_output
).To([cell_state_out, output])

input_dict = {
    input_: [166, 179, 50,  150],
    input_to_input_weights: [146, 250, 235, 171, 10, 218, 171, 108],
    input_to_forget_weights: [24, 50, 132, 179, 158, 110, 3, 169],
    input_to_cell_weights: [133, 34, 29, 49, 206, 109, 54, 183],
    input_to_output_weights: [195, 187, 11, 99, 109, 10, 218, 48],
    recurrent_to_input_weights: [254, 206, 77, 168, 71, 20, 215, 6, 223, 7, 118, 225, 59, 130, 174, 26],
    recurrent_to_forget_weights: [137, 240, 103, 52, 68, 51, 237, 112, 0, 220, 89, 23, 69, 4, 207, 253],
    recurrent_to_cell_weights: [172, 60, 205, 65, 14, 0, 140, 168, 240, 223, 133, 56, 142, 64, 246, 216],
    recurrent_to_output_weights: [106, 214, 67, 23, 59, 158, 45, 3, 119, 132, 49, 205, 129, 218, 11, 98],
    input_gate_bias: [-7876, 13488, -726, 32839],
    forget_gate_bias: [9206, -46884, -11693, -38724],
    cell_gate_bias: [39481, 48624, 48976, -21419],
    output_gate_bias: [-58999, -17050, -41852, -40538],
    prev_cell_state: [876, 1034, 955, -909, 761, 1029, 796, -1036],
    prev_output: [136, 150, 140, 115, 135, 152, 138, 112],
}

output_dict = {
    cell_state_out: [1485, 1177, 1373, -1023, 1019, 1355, 1097, -1235],
    output: [140, 151, 146, 112, 136, 156, 142, 112]
}
Example((input_dict, output_dict), model=model).AddVariations("relaxed")


# TEST 2: same as the first one but only the first batch is tested and weights
# are compile time constants
model = Model()

n_batch = 1
n_input = 2
n_cell = 4
n_output = n_cell

InputType = ("TENSOR_QUANT8_ASYMM", [n_batch, n_input], 1 / 128, 128)
input_ = Input("input", InputType)

weights_scale = 0.00408021
weights_zero_point = 100

InputWeightsType = ("TENSOR_QUANT8_ASYMM",
                    [n_output, n_input], weights_scale, weights_zero_point)
input_to_input_weights = Parameter("inputToInputWeights", InputWeightsType,
                                   [146, 250, 235, 171, 10, 218, 171, 108])
input_to_forget_weights = Parameter("inputToForgetWeights", InputWeightsType,
                                    [24, 50, 132, 179, 158, 110, 3, 169])
input_to_cell_weights = Parameter("inputToCellWeights", InputWeightsType,
                                  [133, 34, 29, 49, 206, 109, 54, 183])
input_to_output_weights = Parameter("inputToOutputWeights", InputWeightsType,
                                    [195, 187, 11, 99, 109, 10, 218, 48])

RecurrentWeightsType = ("TENSOR_QUANT8_ASYMM",
                        [n_output, n_output], weights_scale, weights_zero_point)
recurrent_to_input_weights = Parameter("recurrentToInputWeights", RecurrentWeightsType,
                                       [254, 206, 77, 168, 71, 20, 215, 6, 223, 7, 118, 225, 59, 130, 174, 26])
recurrent_to_forget_weights = Parameter("recurrentToForgetWeights", RecurrentWeightsType,
                                        [137, 240, 103, 52, 68, 51, 237, 112, 0, 220, 89, 23, 69, 4, 207, 253])
recurrent_to_cell_weights = Parameter("recurrentToCellWeights", RecurrentWeightsType,
                                      [172, 60, 205, 65, 14, 0, 140, 168, 240, 223, 133, 56, 142, 64, 246, 216])
recurrent_to_output_weights = Parameter("recurrentToOutputWeights", RecurrentWeightsType,
                                        [106, 214, 67, 23, 59, 158, 45, 3, 119, 132, 49, 205, 129, 218, 11, 98])

BiasType = ("TENSOR_INT32", [n_output], weights_scale / 128., 0)
input_gate_bias = Parameter("inputGateBias", BiasType,
                            [-7876, 13488, -726, 32839])
forget_gate_bias = Parameter("forgetGateBias", BiasType,
                             [9206, -46884, -11693, -38724])
cell_gate_bias = Parameter("cellGateBias", BiasType,
                           [39481, 48624, 48976, -21419])
output_gate_bias = Parameter("outputGateBias", BiasType,
                             [-58999, -17050, -41852, -40538])

StateType = ("TENSOR_QUANT16_SYMM", (n_batch, n_cell), 1 / 2048, 0)
OutputType = ("TENSOR_QUANT8_ASYMM", (n_batch, n_output), 1 / 128, 128)
prev_cell_state = Input("prevCellState", StateType)
prev_output = Input("prevOutput", OutputType)

cell_state_out = Output("cellStateOut", StateType)
output = Output("output", OutputType)

model = model.Operation("QUANTIZED_16BIT_LSTM", input_, input_to_input_weights,
                        input_to_forget_weights, input_to_cell_weights,
                        input_to_output_weights, recurrent_to_input_weights,
                        recurrent_to_forget_weights, recurrent_to_cell_weights,
                        recurrent_to_output_weights, input_gate_bias,
                        forget_gate_bias, cell_gate_bias, output_gate_bias,
                        prev_cell_state,
                        prev_output).To([cell_state_out, output])

input_dict = {
    input_: [166, 179],
    prev_cell_state: [876, 1034, 955, -909],
    prev_output: [136, 150, 140, 115],
}

output_dict = {
    cell_state_out: [1485, 1177, 1373, -1023],
    output: [140, 151, 146, 112]
}
Example((input_dict, output_dict), model=model,
        name="constant_weights").AddVariations("relaxed")
