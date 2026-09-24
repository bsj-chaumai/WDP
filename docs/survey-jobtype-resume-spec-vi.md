# Spec: Resume từ dữ liệu途中保存 — kiểm tra câu hỏi職種（câu 4）

## Khi resume từ dữ liệu途中保存
Khi resume trả lời từ dữ liệu途中保存, thực hiện check:
- Câu hỏi職種（câu 4）đã trả lời hay chưa
- Nghề được chọn là **「単一」** hay **「複数」**

- **Câu hỏi職種（câu 4）chưa trả lời:** giữ logic hiện tại, kế thừa dữ liệu途中保存 và tiếp tục trả lời được.
- **Câu hỏi職種（câu 4）đã trả lời, và đang chọn「単一職種」:** giữ logic hiện tại, kế thừa dữ liệu途中保存 và tiếp tục trả lời được.
- **Câu hỏi職種（câu 4）đã trả lời, và đang chọn「複数職種」:** khi chọn dữ liệu途中保存, hiển thị thông báo xác nhận dưới đây.

## Nội dung dialog
```
職種は1つのみ選択可能なため
再度の回答をお願いします
OK
```

- Bấm ra ngoài phạm vi dialog thì **không đóng**.
- Bấm nút **「OK」** trên dialog thì **chuyển tới câu hỏi職種（câu 4）**.
- Default là **trạng thái chưa chọn**.

## Nút trên câu hỏi職種（câu 4）
- **Chỉ khi đã thay đổi câu hỏi職種（câu 4）** thì mới hiển thị nút **「元の設問に戻る」**.
- Trường hợp thông thường: hiển thị **「previous」** và **「complete」** (xem trang tiếp theo).
- Sau khi đổi sang chọn **単一職種** và trả lời xong, bấm **「元の設問に戻る」** thì quay về câu hỏi đã途中保存 lần trước.

## Thay đổi UI / lựa chọn của câu hỏi職種（câu 4）
- Đổi option từ dạng chọn nhiều sang **radio button**.
  - Trạng thái chưa chọn / đã chọn: tham chiếu **※1** và **※2**.
- Đổi từ **複数選択** sang **単一選択**.
- Các câu hỏi khác **giữ logic hiện tại**.
- Default là **chưa chọn**.
