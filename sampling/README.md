## Cách lấy mẫu hiệu quả để huấn luyện mô hình ngôn ngữ

- Lấy mẫu hiệu quả để cover được nhiều dữ liệu trong cùng một epoch
  - Có sự trùng lặp giữa các mẫu hay hay không?
  - Trùng lặp bao nhiêu là vừa? 1/2, 2/3 ...

- Huấn luyện trên news (phổ thông) trước rồi tới lawpedia (hiếm) hay trộn lẫn theo 1 tỉ lên ưu tiên hiếm?

- Đang chạy phải dừng lại cần quản biết đã lấy mẫu tới đâu


TODOs

- [x] Tìm hiểu cách lấy mẫu của [cramming](https://github.com/JonasGeiping/cramming)
  - Chọn mẫu tốt train trước
  - Trải các mẫu trên một pipeline, cách nhau bởi `<sep>` token
  - Chạy một lượt từ đầu tới cuối cửa sổ dịch chuyển là ctx_len (1-epoch: mỗi token chỉ train 1 lần)

- [-] Tìm hiểu cách lấy mẫu của [gpt-neox](https://github.com/EleutherAI/gpt-neox)

- [-] Tìm hiểu cách lấy mẫu của [rwkv_the_pile](https://github.com/BlinkDL/RWKV-LM/blob/main/RWKV-v4neo/src/dataset.py)
