// Libtorchのインクルード
// #include <torch/script.h>
// #include <iostream>

// using namespace std;
// using namespace torch;

// int main()
// {
// // torch::jit::script::Module 型で module 変数の定義
//   torch::jit::script::Module module;
//   // 変換した学習済みモデルの読み込み
//   module = torch::jit::load("traced_model.pt");
//   // モデルへのサンプル入力テンソル
//   torch::Tensor input = torch::ones({1, 3, 128, 128}).to("cpu");

//   // 推論と同時に出力結果を変数に格納
//   auto elements = module.forward(input).toTuple() -> elements();
//   // 出力結果
//   auto output = elements[0].toTensor();

//   return 0;
// }

#include <iostream>
#include <torch/torch.h>

using namespace std;
using namespace torch;

int main(void){
    torch::Tensor x = torch::full({3, 3}, 1.5, torch::TensorOptions().dtype(torch::kFloat));
    std::cout << x << std::endl;
    return 0;
}