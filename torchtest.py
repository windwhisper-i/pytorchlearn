import torch  # 如正常则静默
a = torch.Tensor([1.])    # 如正常则静默
s=torch.cuda.is_available()
print(s)
print(torch.__version__)